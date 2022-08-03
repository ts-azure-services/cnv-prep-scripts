# To be run in the folder where the files need to be removed
import os
file_list = os.listdir()

# Duplicate transcripts
files_to_remove= ['sample368.wav','sample449.wav','sample465.wav','sample88.wav','sample470.wav','sample64.wav','sample515.wav','sample84.wav','sample53.wav','sample460.wav','sample534.wav','sample582.wav','sample415.wav','sample694.wav','sample718.wav','sample651.wav','sample477.wav','sample598.wav','sample593.wav','sample523.wav','sample61.wav','sample32.wav','sample273.wav','sample419.wav','sample353.wav','sample636.wav','sample31.wav','sample666.wav','sample50.wav','sample667.wav','sample697.wav','sample433.wav','sample404.wav','sample639.wav','sample81.wav','sample211.wav','sample540.wav','sample683.wav','sample719.wav','sample664.wav','sample401.wav','sample74.wav','sample383.wav','sample122.wav','sample624.wav','sample327.wav','sample58.wav','sample396.wav','sample634.wav','sample426.wav','sample480.wav','sample251.wav','sample605.wav','sample390.wav','sample756.wav','sample378.wav','sample14.wav','sample687.wav','sample6.wav','sample7.wav','sample712.wav','sample463.wav','sample600.wav','sample308.wav','sample498.wav','sample567.wav','sample456.wav','sample631.wav','sample556.wav','sample711.wav','sample392.wav','sample395.wav']

# No audio in the recording
#files_to_remove = ['sample751.wav','sample745.wav','sample744.wav','sample740.wav','sample730.wav','sample726.wav','sample723.wav','sample706.wav','sample700.wav','sample674.wav','sample661.wav','sample659.wav','sample644.wav','sample618.wav','sample617.wav','sample604.wav','sample597.wav','sample533.wav','sample509.wav','sample483.wav','sample478.wav','sample454.wav','sample445.wav','sample432.wav','sample391.wav','sample387.wav','sample385.wav','sample363.wav','sample338.wav','sample332.wav','sample323.wav','sample301.wav','sample294.wav','sample29.wav','sample283.wav','sample276.wav','sample275.wav','sample270.wav','sample27.wav','sample267.wav','sample260.wav','sample246.wav','sample241.wav','sample228.wav','sample225.wav','sample224.wav','sample217.wav','sample200.wav','sample197.wav','sample196.wav','sample188.wav','sample173.wav','sample164.wav','sample158.wav','sample138.wav','sample127.wav']

for file in files_to_remove:
    if ".wav" in file:
        os.remove(file)
        #print(file)

