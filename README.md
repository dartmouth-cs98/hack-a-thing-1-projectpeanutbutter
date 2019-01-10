# CS98 cs98HackAThing1
## Andrew Alini, John Kotz, CS98 Winter 2019

### SpeechSummary

'speechSummary.py' is a program that takes either a recording in a '.wav' or '.flac' file or a user input dication through
the microphone and returns a summary of the dictation. This code uses watson developer cloud for speech recognition and 
the NLTK package for summarizing the topic. John Kotz predominantly worked on Speech recongition code while Andrew Alini 
predominantly worked on natural language processing. 'README.md' was written by both Alini and John.

### Getting Started
To get started, clone this repository and `cd` into the destination.
First, make sure you have pip installed (instalation guide: `https://pip.pypa.io/en/stable/installing/`)

The easyest way to run this project is to use a virtual environment. Use this command to install `virtualenv`: (you might add sudo at the beginning if you run into problems)
```bash
pip install virtualenv
```

Setup the local virtual environment. This will create an env folder in the current directory which will act as your virtual environment:
```bash
python -m virtualenv env
```

Once that's done, just activate it and then install the python packages necesary:
```
source ./env/bin/activate
pip install -r requirements.txt
```

Now you should be all set!

> NOTE: to exit the virual environment, just execute the `deactivate` command

#### Usage

To run the code, run the following command while the virtual environment is activated:
```bash
python speechSummary.py
```

### Examples

There are a bunch of `.wav` files in the examples folder. When you run the program, enter one of those example files (you may also need to enable USE_IBM in 'config.ini' if you are using any of those examples).

### Assumptions

User is speaking clearly with minimal background noise. 
User has internet capability.
User speaks within 100minutes as that is the maximum number of minutes per month for the watson developer cloud free account.

### What we learned
During what we call Project-Peanut-Butter learned the basics of natural language processing and speech recognition.

The first step for the summarization is the speech recognition. We use IBM Watson's API to analyze a sound file, split it into what it recognizes as words and make an 'educated' guess about the text form of the word. We then receive all those words strung together back from the API.

The recognized text is passed on to the natural language processing section. This breaks the text down into its individual words. It then finds the weighted frequency of each word, ignoring things like stopwords, punctuation etc., and sums the weighted frequency of the words in each sentence to obtain the sentence score. It finally sorts the sentences based on score and returns the sentences with the top score as the summary of the original text.

> Peanut Butter is an excellent source of nutrition. In addition, there can be bugs in peanut butter which is an excellent source of protein. Overall, Peanut Butter should be in the diet of every american, unless allergic :'( 

### What didn't work
Unfortunately, the default Google Speech API seemed to have a maximum time limit on its use, so we spent a lot of time trying to figure out why it would only recognize some of the message.

We also found that our chosen Speech-to-Text API (IBM Watson) would not insert punctuation in transcripts. Our NLP system requires punctuation to diliniate between sentences, so this was a major problem for our product. After some research we found an API that would allow us to post text and receive punctuated text, thus solving our problem.