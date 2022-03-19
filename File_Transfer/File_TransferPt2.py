import shutil
import os
import datetime
from datetime import timedelta

##set where the source of the files are
source = './Part2_AllFiles/'

##set the destination path to Folder_B
destination = './Part2_NewFiles/'
files = os.listdir(source)
today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

for i in files:
    modTime = datetime.datetime.fromtimestamp(os.path.getmtime(source+i))
    if modTime < yesterday:
        print('This file is old. Didn\'t do anything')
    else:
        shutil.copy(source+i,destination)
        print('This file is new. Copied to destination.')
