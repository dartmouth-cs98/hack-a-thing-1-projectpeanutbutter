import numpy
import nltk
import urllib
import re
import heapq


sentence = """The White House announced that President Trump would travel to the southern border this week.CreditCreditSarah Silbiger/The New York Times

President Trump announced on Monday that he would address the nation from the Oval Office on Tuesday evening to discuss what he called the crisis at the southern border, and the White House said that later in the week he would travel to the border as part of his effort to persuade Americans of the need for a wall — the sticking point in negotiations with Democrats which caused a government shutdown.

It was not immediately clear which outlets would carry his address. The four major broadcast networks — ABC, CBS, FOX and NBC — confirmed receiving the White House request on Monday for Mr. Trump to speak during the 9 p.m. Eastern Standard Time slot, but producers had not decided whether to grant him the time. Pre-empting prime-time coverage is an expensive proposition for television executives, who have sold millions of dollars’ worth of advertising against entertainment programming. Mr. Trump’s remarks could also be covered by cable news networks, which have a much smaller audience. CNN has agreed to air the address, a spokeswoman said on Monday. But cable news stations are accustomed to cutting in for breaking news, and they reach a far smaller audience than traditional broadcast stations.

In the recent past, White House requests to interrupt prime-time programming on the nation’s broadcast networks were rare and usually reserved for moments of national import, like the death of Osama bin Laden, and networks usually granted the requests. There have been instances, however, where such requests were rejected by producers as insufficiently newsworthy.

In an effort to justify his demands for a border wall, Mr. Trump has tried to paint the situation at the southern border as an imminent humanitarian and national security crisis, which Democrats and several immigration advocates argue is inaccurate.

The acting White House chief of staff, Mick Mulvaney, has for days told other White House officials that a presidential address would be a way for Mr. Trump to try and recast the narrative around the shutdown fight.

Sarah Huckabee Sanders, the White House press secretary, on Monday announced Mr. Trump’s plans to travel Thursday to the border, which would be the 20th day of the partial government shutdown if an agreement between Congress and the White House is not reached in the meantime.

So far, there has been little progress in the negotiations between congressional Democrats and the White House. The shutdown is the second longest in the nation’s history and affects about 800,000 federal workers, many of whom will not get paid for the first time this week.

Mr. Trump has said he would not sign legislation to fund shuttered agencies — and reopen the government — unless it includes funding for a border wall between the United States and Mexico. Nancy Pelosi, the new speaker of the House, which came under Democratic control last week, has asserted that the president is “not going to get a wall.”

Ms. Pelosi has said the House this week would start considering individual funding bills to reopen the government. One such bill would be to fund the Treasury Department so that employees for the Internal Revenue Service could return to work as tax filing season begins.

Other bills would provide funding to reopen the Agriculture, Housing and Urban Development and Interior Departments."""
tokens = nltk.word_tokenize(sentence)

# Adapted from https://stackabuse.com/text-summarization-with-nltk-in-python/


# Where we start
def summarize(audio_text):

    article_text = re.sub(r'\[[0-9]*\]', ' ', audio_text)  
    article_text = re.sub(r'\s+', ' ', audio_text)  

    formatted_article_text = re.sub('[^a-zA-Z]', ' ', audio_text )  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text) 
    
    sentence_list = nltk.sent_tokenize(audio_text)
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):  
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


    summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    print(summary)

summarize(sentence)










