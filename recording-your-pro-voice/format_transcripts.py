"""Example of formatting the consolidated transcript list to fit the upload format.

Transcript sourced from https://github.com/Azure-Samples/Cognitive-Speech-TTS\
        /blob/master/CustomVoice/script/English%20(United%20States)_enUS/\
        3000000001-3000000300_Chat.txt
"""
import re

if __name__ == "__main__":

    # Open original transcript file
    with open('./original_transcript.txt', 'r', encoding='utf-8') as f:
        script = f.readlines()

    # Iterate through lines
    with open('./modified_transcript.txt', 'w', encoding='utf-8') as mt:
        for i,val in enumerate(script):
            temp_list = re.split(r'\t', val)
            statement = f"{str(i+1)}\t{temp_list[1]}"
            mt.write(statement)
