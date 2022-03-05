import os

fname = 'Hello.txt'

fPath = 'C:\\A\\'

abPath = os.path.join(fPath, fname)

print(abPath)
