# Identify scripts with multiple sentences
# Pre-loading, a utterance should only be a sentence
import os
import csv
import re

# Open the transcripts file, and populate current values
def load_file():
    with open('./../transcripts_edited.csv', 'r') as f:
        reader = csv.DictReader(f)
        transcripts = []
        audio_files = []
        for row in reader:
            audio_files.append(row['filename'])
            transcripts.append(row['display_edited'])
    return transcripts, audio_files

# Open a new file, and overwrite new audio files, with new labels
def create_new_transcript(audio_files=None, transcripts=None):
    with open('./final-script.txt', 'w') as mt:
        for i,val in enumerate(audio_files):
            current_audio_file_name = str(audio_files[i])
            new_audio_file_name = str(i+1)
            current_audio_file = current_audio_file_name + '.wav'
            new_audio_file = new_audio_file_name + '.wav'

            # Rename the files in the audio folder
            print(f"Original filename is: {current_audio_file}, new filename is: {new_audio_file}")
            filepath = './test-samples/'
            os.rename(filepath + current_audio_file, filepath + new_audio_file)

            # Write out to final script file
            statement = f"{new_audio_file_name}\t{transcripts[i]}\n"
            mt.write(statement)

if __name__ == "__main__":
    transcripts, audio_files = load_file()
    create_new_transcript(audio_files=audio_files, transcripts=transcripts)
