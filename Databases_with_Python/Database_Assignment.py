import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

##CREATE DATABASE AND TABLE
conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()

##FIND ALL TEXT FILES IN THE FILE LIST
def findTXT():
    for f in fileList:
        if f.endswith('.txt'):
            addFiles(f)

##ADD TXT FILES TO THE TABLE
def addFiles(f):
    conn = sqlite3.connect('files.db')

    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", (f,))
        conn.commit()
    conn.close()

##PRINT ALL FILENAMES FOR TEXT FILES FROM THE TABLE
def printTXT():
    conn = sqlite3.connect('files.db')

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT file_name FROM tbl_files")
        txtFiles = cur.fetchall()
        for f in txtFiles:
            msg = "{} is a text file.".format(f)
            print(msg)
    conn.close()


if __name__ == "__main__":
    findTXT()
    printTXT()
