import nltk, requests, heapq, configparser, re
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API']['KEY']
DO_SPEECH = bool(config['SPEECH']['USE_IBM'])
NUM_SENTENCES = int(config['SUMAMRY']['NUM_SENTENCES'])

# MARK: Convert from speech to text
transcripts = []

if DO_SPEECH:
    # MARK: Get a WAV file
    fileName = raw_input("Enter a file name: ").strip()
    print('Processing audio')
    
    # Adapted from Watson example code: https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/speech_to_text_v1.py
    service = SpeechToTextV1(url="https://stream.watsonplatform.net/speech-to-text/api", iam_apikey=API_KEY)

    models = service.list_models().get_result()
    model = service.get_model('en-US_BroadbandModel').get_result()

    with open(fileName, 'rb') as audio_file:
        recognition = service.recognize(audio=audio_file, content_type='audio/wav').get_result()
    transcripts = list(map(lambda x: x['alternatives'][0]['transcript'], recognition["results"]))
else:
    transcripts = ['good evening my fellow citizens this government as promised has maintains the closest surveillance of the Soviet military buildup on the island of Cuba within the past week unmistakable evidence has established the fact that I see reserve offensive missile sites is now in preparation on the imprisoned island the purpose of these bases can be none other than to provide a nuclear strike capability against the western hemisphere ',
        'upon receiving the first preliminary hard information of this nature last Tuesday morning at nine AM I directed that our surveillance be stepped up ',
        'ends having now confirmed and completed our evaluation of the evidence and our decision on a course of action this government feels obliged to report this new crisis you in the fullest detail ',
        'the characteristics of these new missile sites indicate two distinct type of insulations several of them include medium range ballistic missiles capable of carrying a nuclear warhead for a distance of more than one thousand knocked tore all miles ']

text = ''.join(transcripts)

# Get rid a bunch of extranious characters
text = text.replace('%HESITATION', '')
text = re.sub(r'\[[0-9]*\]', ' ', text)  
text = re.sub(r'\s+', ' ', text)  

# MARK: Adding punctation
print("Text received. Punctuating...")
text = requests.post("http://bark.phon.ioc.ee/punctuator?text=" + text).text
print(text)

print("==================================")

# MARK: Summarize
# Adapted from https://stackabuse.com/text-summarization-with-nltk-in-python/

# Make a special version with no uppercase letters
formatted_text = re.sub('[^a-zA-Z]', ' ', text)  
formatted_text = re.sub(r'\s+', ' ', formatted_text) 

sentence_list = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

# Calculate the frequency of every word in the text
word_frequencies = {}  
for word in nltk.word_tokenize(formatted_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Generate a score for each sentence as a sumation of the word frequencies
sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

# Get the top # of sentences
summary_sentences = heapq.nlargest(NUM_SENTENCES, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print(summary)