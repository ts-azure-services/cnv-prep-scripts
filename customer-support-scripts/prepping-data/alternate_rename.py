# To be used in the folder where the files are to be renamed
import os
file_list = os.listdir()
counter = 0
for i in file_list:
    if ".wav" in i:
        counter += 1
        new_filename = 'sample' + str(counter) + '.wav'
        print(f"Original filename is: {i}, new filename is: {new_filename}")
        os.rename(i, new_filename)
