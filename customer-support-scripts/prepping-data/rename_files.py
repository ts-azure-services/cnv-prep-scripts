"""Helper function to rename files in a specified directory
Example of original filename: 'New Recording 1.wav'
Example of renamed filename: '1.wav'
Command line statement to run: 'python rename_files.py -d "<specify directory>"'
"""
import os
import argparse

def rename_files(file_list=None, directory=None):
    """Rename files function"""
    for file in file_list:
        if ".wav" in file:
            original_filename = file
            new_filename = file.split()[2]
            print(f"Original filename is: {original_filename}, new filename is: {new_filename}")
            os.rename(directory + '/' + original_filename, directory + '/' + new_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get directory for files to rename.")
    parser.add_argument("-d", "--directory", type=str, help="The directory to rename files.")
    args = parser.parse_args()

    # Get directory
    list_of_files = os.listdir(args.directory)
    rename_files(file_list=list_of_files, directory=args.directory)
