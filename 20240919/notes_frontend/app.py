import json 
import requests 

class NotesApp:
    def __init__(self):
        self.url = 'http://localhost:5000'
    def read_all(self):
        res = requests.get(f'{self.url}/notes')
        return res.json()
    def read_by_id(self, id):
        res = requests.get(f'{self.url}/notes/{id}')
        return res.json()
    def create(self, note_json_str):
        headers = {'Content-type':'application/json'}
        res = requests.post(f'{self.url}/notes',data=note_json_str,headers=headers)
        return res.json()
    def update(self, id, note_json_str):
        headers = {'Content-type':'application/json'}
        res = requests.put(f'{self.url}/notes/{id}',data=note_json_str,headers=headers)
        return res.json()
    def delete(self, id):
        res = requests.delete(f'{self.url}/notes/{id}')
        return res.json()
    #enddef
#endclass

app = NotesApp()
choice = int(input('1-all,2-read_by_id,3-create,4-update,5-delete,6-search\nchoice:'))
if choice == 1:
    notes = app.read_all()
    print(notes)
elif choice == 2:
    id = int(input('id:'))
    note = app.read_by_id(id)
    print(note)
elif choice == 3:
    title = input('title:')
    notes = input('notes:')
    note_dict = {'title':title,'notes':notes}
    note_json_str = json.dumps(note_dict)
    note = app.create(note_json_str)
    print('Created successfully')
    print(note)
elif choice == 4:
    id = input('id:')
    old_note = app.read_by_id(id)
    title = input(f'title({old_note["title"]}):')
    notes = input(f'notes({old_note["notes"]}):')
    note_dict = {'title':title,'notes':notes}
    note_json_str = json.dumps(note_dict)
    note = app.update(id,note_json_str)
    print('Updated successfully')
    print(note)
elif choice == 5:
    id = input('id:')
    old_note = app.read_by_id(id)
    print(old_note)
    if (input('Are you sure to delete?') == 'yes'):
        app.delete(id)
        print('Deleted Successfully')