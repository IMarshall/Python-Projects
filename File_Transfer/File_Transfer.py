import shutil
import os

##set where the source of the files are
source = './Folder_A/'

##set the destination path to Folder_B
destination = './Folder_B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
