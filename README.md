# Chatbot Helper Modules 

## spacy_chatbot_sentences.py


When talking with a chatbot the code will take the text, use spacy to extract entities then search the entities on wikipedia. The
return text is then saved to a csv file with epoch_time of the request, clock time of the reques, date, MD5 hash of the summary and the text summary itself.  

Required libraries include gensim, spacy and wikipedia.  

# 5 December 2020: coversation_builder.py

This module takes in sentences sent by the user to an AIML chatbot and puts them in AIML sentence / data format to be integrated into conversation files.  Designed to allow a continuous learning loops for file based AIML chatbots. 



G3Dx5 November 2020