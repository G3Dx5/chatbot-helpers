#!/usr/bin/env python3

'''
python3 Text processing functions for user message input to a chatbot

When talking with a chatbot, will take the text, use spacy to extract entities then search the entities on wikipedia. The
return text is then saved to a csv file with epoch_time of the request, clock time of the reques, date, MD5 hash of the summary and the 
text summary itself.  

You may get: "UserWarning: No parser was explicitly specified, so I'm using the
best available HTML parser for this system ("lxml").", If you're relying on the pip package still,
you need to manually edit the wikipedia.py file yourself.  At a command line prompt, find where the package is installed:
pip show wikipedia
It should be 'anaconda3/lib/python3.6/site-packages/wikipedia'. Go there, find wikipedia.py and lo' and edit line 389 and make
the new line: lis = BeautifulSoup(html, 'html.parser').find_all('li')
:args - Nil
'''

import datetime
from gensim.summarization import summarize
from gensim.summarization import keywords
import hashlib
import spacy
import time
import wikipedia as wikipedia
import csv


#message = "Sir Richard Francis Burton was one of the greatest explorers to have visited Africa in 1879"
#message = "Elizabeth Taylor was an actress in California in 1983"
message = "I saw the movie gone with the wind starring Vivien Leigh, made in 1939"

extracted_entities = []

def entity_extraction(message):
    nlp = spacy.load('en')
    user_sentence = nlp(message)
    for entity in user_sentence.ents:
        print(entity.text, entity.label_, entity.label)
        if entity == None:
            break
        else:
            extracted_entities.append(entity.text)
    return extracted_entities

entity_extraction(message)

def hash_paragraph(paragraph):
    hash_text = hashlib.md5()
    hash_text.update(paragraph.encode('utf-8'))
    return hash_text.hexdigest()

def get_wikipedia_summary():
    for entity in extracted_entities:
        summary = wikipedia.summary(entity).replace('\n',' ')
        summary_hash = hash_paragraph(summary)
        epoch_time = time.time()
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        clock_time = datetime.datetime.now().strftime("%H%M" + "hrs") 
        with open("wikistuff.csv", "a", newline='') as filedata:
            fileinfo = [epoch_time, clock_time, date, summary_hash, summary]
            wr = csv.writer(filedata, dialect='excel')
            wr.writerow(fileinfo)

get_wikipedia_summary()

