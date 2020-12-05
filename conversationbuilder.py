#!/usr/bin/env python
import csv

def message_saver(format, message):
    with open("chat_builder.csv", "a", newline='') as fp:
        #start_format = "- - "
        csvRow = [format + message]
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(csvRow)


def aiml_file_builder(message):
     with open("aiml_builder.csv", "a", newline='') as aimlbuilder:
        start_pattern_tag = "<category><pattern>"
        end_pattern_tag = "</pattern>"
        bot_return = "<template></template></category>"
        message = message
        message = message.upper()
        user_message = [start_pattern_tag + message + end_pattern_tag]
        bot_return = [bot_return]
        wr = csv.writer(aimlbuilder, dialect='excel')
        wr.writerow(user_message)
        wr.writerow(bot_return)
