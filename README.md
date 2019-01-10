# CS98 cs98HackAThing1 (Winter 2019)
> Andrew Alini, John Kotz

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
