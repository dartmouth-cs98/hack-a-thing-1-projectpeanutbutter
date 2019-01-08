# CS98 cs98HackAThing1
## Andrew Alini, John Kotz, CS98 Winter 2019

### SpeechSummary

'SpeechSummary.py' is a program that takes either a recording in a '.wav' or '.flac' file or a user input dication through
the microphone and returns a summary of the dictation. This code uses watson developer cloud for speech recognition and 
the NLTK package for summarizing the topic. John Kotz predominantly worked on Speech recongition code while Andrew Alini 
predominantly worked on natural language processing. 'README.md' was written by both Alini and John.

### Usage

(JOHN TODO)
### Examples
(JOHN TODO)
### Assumptions

User is speaking clearly with minimal background noise. 
User has internet capability.
User speaks within 100minutes as that is the maximum number of minutes per month for the watson developer cloud free account.

### What we learned
We learned the basics of natural language processing and speech recognition. Natural Language Processing takes in text and breaks
it down into its individual words. Then for summarizing a text, it finds the weighted frequency of each word. Ignoring things like
stopwords, punctuation and etcetera, it then sums the weighted frequency to obtain the sentence score. it finally sorts the sentences
based on score and returns the sentences with the top score as the summary of the original text.

(JOHN TODO)

> Peanut Butter is an excellent source of nutrition. In addition, there can be bugs in peanut butter which is an excellent source of protein.
Overall, Peanut Butter should be in the diet of every american, unless allergic :'( 
### What didn't work
google speech api didn't have enough time for recordings

Discovered speech to text api would not insert api in transcripts. this is a problem because our nlp system requires punctuation for 
diliniation between sentences and phrases. However, we recognized that we could fix this (JOHN KOTZ WRITE)