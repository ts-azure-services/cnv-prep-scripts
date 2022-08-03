"""Helper function to zip up files in a specified directory
Command line statement to run: 'python zip_files.py -d "<specify directory>"'
"""
import os
import argparse
from zipfile import ZipFile

def create_zip_file(dirname=None):
    """Function to zip up files."""
    complete_files = os.listdir(str(dirname) + '/')
    zfile = './' + str(dirname) + '/' + "complete.zip"  # zip file name
    with ZipFile(zfile, 'w') as zip:
        for file in complete_files:
            zip.write('./' + str(dirname) + '/' + file)
    print(f"Files in {dirname} successfully zipped in the same folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get directory for files to zip.")
    parser.add_argument("-d", "--directory", type=str, help="The directory to zip up files.")
    args = parser.parse_args()
    create_zip_file(dirname=args.directory)
