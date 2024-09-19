import sqlite3

def connect():
    con = sqlite3.connect('notes_db.db')
    return con 
def noteTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS notes(
        id integer primary key AUTOINCREMENT,
        title varchar(255) not null,
        notes varchar(2000) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Note:
    def __init__(self, id=None,
        title='',
        notes=''):
        self.id = id 
        self.title = title 
        self.notes = notes
    def __str__(self):
        return f'[{self.id},{self.title},{self.notes}]'
    def __repr__(self):
        return self.__str__()

def createNote(note):
    sql = """INSERT INTO notes(title, notes)
    VALUES(?,?)"""
    params = (note.title, note.notes,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  #
    con.commit()
    con.close()
    return id           #

def readAllNotes():
    sql = """SELECT id,title, notes FROM notes"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    notes = []
    for row in result:
        notes.append(Note(id=row[0],title=row[1],
                notes=row[2]))
    return notes 

def search(title, notes_text):
    title = title.strip()
    notes_text = notes_text.strip()
    sql = """SELECT id,title, notes FROM notes
        WHERE ( ? == '' OR title=?) AND 
              ( ? == '' OR notes like ('%' || ? || '%'))"""
    params = (title,title, notes_text,notes_text)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    notes = []
    for row in result:
        notes.append(Note(id=row[0],title=row[1],
                notes=row[2]))
    return notes 

def updateNote(note):
    sql = """UPDATE notes
    set title=?,notes=?
    WHERE (id=?)"""
    params = (note.title, note.notes,
              note.id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def deleteNote(id):
    sql = """DELETE from notes
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readNoteById(id):
    sql = """SELECT id,title, notes FROM notes
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        note = Note(id=result[0],title=result[1],
                    notes=result[2])
    else:
        note = None 
    return note

