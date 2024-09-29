import sqlite3
import json
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Step 1: Database and Cab class
def init_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Airplane (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT NOT NULL,
            seats_Available TEXT NOT NULL,
            ticket_Price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class Airplane:
    def __init__(self,flight_number, seats_Available,ticket_Price):
        self.flight_number =    flight_number
        self.seats_Available = seats_Available
        self.ticket_Price =    ticket_Price

    @staticmethod
    def create(flight_number, seats_Available, ticket_Price):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Airplane(flight_number, seats_Available,ticket_Price) VALUES (?, ?, ?)',(flight_number, seats_Available,ticket_Price))
        conn.commit()
        conn.close()

    @staticmethod
    def read_by_id(id):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Airplane WHERE id = ?', (id,))
        cab = cursor.fetchone()
        conn.close()
        return cab

# Step 2: Write JSON file
def write_product_json(id):
    product =Airplane.read_by_id(id)
    if product:
        product_dict = {
            'id': product[0],
            'flight_number': product[1],
            'seats_Available': product[2],
            'ticket_Price': product[3]
        }
        with open('product.json', 'w') as f:
            json.dump(product_dict,f)
        return 'product.json'
    else:
        print("Product not found")
        return None

# Step 3: Send email with JSON attachment
def send_mail(product_json, recipient_email):
    sender_email = 'nandhinikalimuthu05@gmail.com'
    password = 'efkh zsqt xobg cfcj'  # App Password
    subject = 'Airplane Booking Confirmation'

    # Setup MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body = 'Your Airplane booking has been confirmed. Please find the details attached.'

    # Attach body and file
    msg.attach(MIMEText(body, 'plain'))

    # Attach JSON file
    with open(product_json, 'rb') as f:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(f.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={product_json}')
        msg.attach(mime_base)

    try:
        # Send the email
        connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        connection.login(sender_email, password)
        connection.sendmail(sender_email, recipient_email, msg.as_string())
        connection.close()
        print('Mail sent successfully')
    except Exception as e:
        print(f'Failed to send mail: {e}')

# Example usage

# Initialize DB and add sample product if needed
init_db()
Airplane.create("AIR123", "30", '500')  # Add a product if DB is empty

# Write product to JSON file and send an email
file = write_product_json(1)
if file:
    send_mail(file, "mleena029@gmail.com")
    


from flask import Flask, jsonify, request
from db1 import AirplaneTablesCreate, Airplane, createTicket, readAllPassengers     
from db1 import search, update, delete, readById         
AirplaneTablesCreate()                                                 
app = Flask(__name__)

@app.route('/notes',methods=['POST'])
def notes_create():
    body = request.get_json()
    new_note = Airplane(flight_Number=body['flight_Number'], seats_Available=body['seats_Available'],ticket_Price=body['ticket_Price'])
    id = createTicket(new_note)
    note = readById(id)
    note_dict = {'id':note.id, 'flight_Number':note.flight_Number, 'seats_Available':note.seats_Available,'ticket    ticket_Price':note.ticket_Price}
    return jsonify(note_dict)

@app.route('/notes/<id>',methods=['GET'])
def notes_read_by_id(id):
    note = readById(id)
    note_dict = {'id':note.id, 'flight_Number':note.flight_Number, 'seats_Available':note.seats_Available,'ticket_Price':note.ticket_Price}
    return jsonify(note_dict)

@app.route('/notes',methods=['GET'])
def notes_read_all():
    notes = readAllPassengers()
    notes_dict = []
    for note in notes:
        notes_dict.append({'id':note.id, 'flight_Number':note.flight_Number, 'seats_Available':note.seats_Available,'ticket_Price':note.ticket_Price})
    return jsonify(notes_dict)

@app.route('/notes/<id>',methods=['PUT'])
def notes_update(id):
    body = request.get_json()
    old_note = readById(id)
    if not old_note:
        return jsonify({'message': 'Note is not found'}),404
    old_note.flight_Number = body['flight_Number']
    old_note.seats_Available = body['seats_Available']
    old_note.ticket_Price = body['ticket    ticket_Price']
    update(old_note)
    note = readById(id)
    note_dict = {'id':note.id, 'flight_Number':note.flight_Number, 'seats_Available':note.seats_Available,'ticket_Price':note.ticket_Price}
    return jsonify(note_dict)

@app.route('/notes/<id>',methods=['DELETE'])
def notes_delete(id):
    old_note = readById(id)
    if not old_note:
        return jsonify({'message': 'Note is not found', 'is_error': 1})
    delete(id)
    return jsonify({'message': 'Note is successfully deleted', 'is_error': 0})

@app.route('/notes_search',methods=['POST'])
def notes_search():
    body = request.get_json()
    notes = search(body.get('flight_Number',''))
    notes_dict = []
    for note in notes:
        notes_dict.append({'id':note.id, 'flight_Number':note.flight_Number, 'seats_Available':note.seats_Available,'ticket_Price':note.ticket_Price})
    return jsonify(notes_dict)


if __name__ == '__main__':
    AirplaneTablesCreate()
    app.run(debug=True)
