import os

folder = os.listdir('SampleFolder')

def findTXT():
    for f in folder:
        if '.txt' in f:
            getTime(f)

def getTime(f):
    fPath = os.path.join('SampleFolder', f)
    modTime = os.path.getmtime(fPath)
    print('{} was last modified at {}.'.format(f,modTime))

if __name__ == "__main__":
    findTXT()
