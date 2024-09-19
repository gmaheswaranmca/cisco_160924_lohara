from flask import Flask, jsonify, request
from db import Note, noteTablesCreate, createNote, readAllNotes     ###
from db import search, updateNote, deleteNote, readNoteById         ###
noteTablesCreate()                                                  ###
app = Flask(__name__)

@app.route('/notes',methods=['POST'])
def notes_create():
    body = request.get_json()
    new_note = Note(title=body['title'], notes=body['notes'])
    id = createNote(new_note)
    note = readNoteById(id)
    note_dict = {'id':note.id, 'title':note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route('/notes/<id>',methods=['GET'])
def notes_read_by_id(id):
    note = readNoteById(id)
    note_dict = {'id':note.id, 'title':note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route('/notes',methods=['GET'])
def notes_read_all():
    notes = readAllNotes()
    notes_dict = []
    for note in notes:
        notes_dict.append({'id':note.id, 'title':note.title, 'notes':note.notes})
    return jsonify(notes_dict)

@app.route('/notes/<id>',methods=['PUT'])
def notes_update(id):
    body = request.get_json()
    old_note = readNoteById(id)
    if not old_note:
        return jsonify({'message': 'Note is not found'})
    old_note.title = body['title']
    old_note.notes = body['notes']
    updateNote(old_note)
    note = readNoteById(id)
    note_dict = {'id':note.id, 'title':note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route('/notes/<id>',methods=['DELETE'])
def notes_delete(id):
    old_note = readNoteById(id)
    if not old_note:
        return jsonify({'message': 'Note is not found', 'is_error': 1})
    deleteNote(id)
    return jsonify({'message': 'Note is successfully deleted', 'is_error': 0})

@app.route('/notes_search',methods=['POST'])
def notes_search():
    body = request.get_json()
    notes = search(body.get('title',''), body.get('notes_text',''))
    notes_dict = []
    for note in notes:
        notes_dict.append({'id':note.id, 'title':note.title, 'notes':note.notes})
    return jsonify(notes_dict)

app.run(debug=True)