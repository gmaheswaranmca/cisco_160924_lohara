from db import noteTablesCreate, createNote, readAllNotes, Note

noteTablesCreate()

id = createNote(Note(title='flask',notes='flask is web dev framework and python package'))
print(f'{id} is inserted')
id = createNote(Note(title='django',notes='django is also web dev framework and python package. It includes all the batteries.'))
print(f'{id} is inserted')

notes = readAllNotes()
print(notes)

