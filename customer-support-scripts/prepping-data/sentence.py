# Identify scripts with multiple sentences
# Pre-loading, a utterance should only be a sentence
import csv
import re
with open('./../transcripts_edited.csv', 'r') as f:
    reader = csv.DictReader(f)
    transcripts = []
    audio_files = []
    for row in reader:
        audio_files.append(row['filename'])
        transcripts.append(row['display_edited'])

# Find number of periods and question marks in sentences
summary = []
for i,v in enumerate(transcripts):
    periods = len(re.findall(r'\.', v))
    question_marks = len(re.findall(r'\?', v))
    exclamations = len(re.findall(r'\!', v))
    # Have to create a list of dictionaries
    temp_dict = {"filename": audio_files[i], "transcript": v, "periods": periods, "questions": question_marks,
            "exclamations": exclamations}
    summary.append(temp_dict)

## Likely race condition
#for item in summary:
#    if item['periods'] == 1 and item['questions'] == 0:
#        summary.remove(item)

# Filtering for certain combinations
transcripts_to_delete = []
for item in summary:
    if item['periods'] == 1 and item['questions'] == 0:
        transcripts_to_delete.append(item)
    if item['periods'] == 0 and item['questions'] == 1:
        transcripts_to_delete.append(item)
    if item['periods'] == 0 and item['questions'] == 0 and item['exclamations'] == 1:
        transcripts_to_delete.append(item)

# Edit summary to exclude items
summary = [x for x in summary if x not in transcripts_to_delete]

with open('summary.csv', 'w', newline='') as csvfile:
    fieldnames = ['filename','transcript', 'periods', 'questions', 'exclamations']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for line in summary:
        writer.writerow(line)
