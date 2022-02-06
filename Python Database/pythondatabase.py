import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignmentDatabase(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_string TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')

#list of things
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the list to find the names that end in txt
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #The value for each row will be one namee of the tuple therefore (x,)
            #will denonate a one element tuple for each name ending with y.
            cur.execute("INSERT INTO tbl_assignmentDatabase(col_string) VALUES (?)",(x,))
            print(x)

conn.close()
