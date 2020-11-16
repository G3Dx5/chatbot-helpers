# Chatbot Helper Modules 

## spacy_chatbot_sentences.py

When talking with a chatbot, will take the text, use spacy to extract entities then search the entities on wikipedia. The
return text is then saved to a csv file with epoch_time of the request, clock time of the reques, date, MD5 hash of the summary and the text summary itself.  

Required libraries include gensim, spacy and wikipedia.  









GaDayas November 2020