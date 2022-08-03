"""Helper function to convert m4a files to wav files.
Command line statement to run: 'python conversion.py -m  "<specify filepath> -w "<specify wav filename>"'
"""
import argparse
from pydub import AudioSegment

def create_wav_file(m4a_file=None, wav_filename=None):
    """Create a wav file from an m4a file."""
    track = AudioSegment.from_file(m4a_file,  format= 'm4a')
    file_handle = track.export(wav_filename, format='wav')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load files to convert, from m4a to wav.")
    parser.add_argument("-m", "--m4a_filepath", type=str, help="The m4a file to load.")
    parser.add_argument("-w", "--wav_filename", type=str, help="The wav filename to create.")
    args = parser.parse_args()
    create_wav_file(m4a_file= args.m4a_filepath, wav_filename=args.wav_filename)
