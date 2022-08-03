# All run from the prepping data folder
import os, subprocess, csv

def transcript_length():
    wd = os.getcwd()
    os.chdir('./../')
    ts = subprocess.run(['wc','-l','transcripts_edited.csv'],check=True, stdout=subprocess.PIPE,universal_newlines=True)
    ts = ts.stdout
    return int(ts.lstrip()[:3])

def files_length():
    """In audio directory, get count of files"""
    # Get count
    wd = os.getcwd()
    os.chdir('./prepping-data/audio-files-edited/')
    p1 = subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE,universal_newlines=True)
    p2 = subprocess.run(['wc','-l'],check=True, stdin=p1.stdout, stdout=subprocess.PIPE,universal_newlines=True)
    p2 = p2.stdout

    # Get list of files
    audio_files = os.listdir()
    return int(p2), audio_files

def get_transcript_list(source=None):
    with open(source, 'r') as f:
        reader = csv.DictReader(f)
        audio_files = []
        for row in reader:
            audio_files.append(row['filename'])
    return audio_files

ts = transcript_length()
fl, audio_files = files_length()
print(f"Current working directory: {os.getcwd()}")
transcripts = get_transcript_list(source="./../../transcripts_edited.csv")
audio_files = [x.replace('.wav','') for x in audio_files]
print(f"Length of audio files: {len(audio_files)}, length of transcripts: {len(transcripts)}")
if len(audio_files) > len(transcripts):
    print('Audio files are greater than transcripts...')
    delta = [x for x in audio_files if x not in transcripts]
    print(delta)
elif len(transcripts) > len(audio_files):
    print('Transcripts are greater than audio files...')
    delta = [x for x in transcripts if x not in audio_files]
    print(delta)
elif len(transcripts) == len(audio_files):
    print("All reconciled.. No delta..")
