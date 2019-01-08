import nltk, requests, heapq
import speech_recognition as sr
import bs4 as bs
import re

# r = sr.Recognizer()
# mic = sr.Microphone()

# with mic as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     print("Say something!")
#     audio = r.listen(source)
# print("Got the audio. Working on it...")
# text = r.recognize_google(audio)

transcripts = ['good evening my fellow citizens this government as promised has maintains the closest surveillance of the Soviet military buildup on the island of Cuba within the past week unmistakable evidence has established the fact that I see reserve offensive missile sites is now in preparation on the imprisoned island the purpose of these bases can be none other than to provide a nuclear strike capability against the western hemisphere ', 'upon receiving the first preliminary hard information of this nature last Tuesday morning at nine AM I directed that our surveillance be stepped up ', 'ends having now confirmed and completed our evaluation of the evidence and our decision on a course of action this government feels obliged to report this new crisis you in the fullest detail ', 'the characteristics of these new missile sites indicate two distinct type of insulations several of them include medium range ballistic missiles capable of carrying a nuclear warhead for a distance of more than one thousand knocked tore all miles ']
text = ''.join(transcripts)
print("Got the text. Continuing...")
text = requests.post("http://bark.phon.ioc.ee/punctuator?text=" + text).text

# Adapted from https://stackabuse.com/text-summarization-with-nltk-in-python/
print(text)

print("==================================")

text = re.sub(r'\[[0-9]*\]', ' ', text)  
text = re.sub(r'\s+', ' ', text)  

formatted_text = re.sub('[^a-zA-Z]', ' ', text )  
formatted_text = re.sub(r'\s+', ' ', formatted_text) 

sentence_list = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print(summary)