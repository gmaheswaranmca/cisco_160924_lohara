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
        CREATE TABLE IF NOT EXISTS cab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            type TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class Cab:
    def __init__(self, number, cab_type, price):
        self.number = number
        self.cab_type = cab_type
        self.price = price

    @staticmethod
    def create(number, cab_type, price):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cab (number, type, price) VALUES (?, ?, ?)', (number, cab_type, price))
        conn.commit()
        conn.close()

    @staticmethod
    def read_by_id(id):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cab WHERE id = ?', (id,))
        cab = cursor.fetchone()
        conn.close()
        return cab

# Step 2: Write JSON file
def write_product_json(id):
    product = Cab.read_by_id(id)
    if product:
        product_dict = {
            'id': product[0],
            'number': product[1],
            'type': product[2],
            'price': product[3]
        }
        with open('product.json', 'w') as f:
            json.dump(product_dict, f)
        return 'product.json'
    else:
        print("Product not found")
        return None

# Step 3: Send email with JSON attachment
def send_mail(product_json, recipient_email):
    sender_email = 'bhargavidasari528@gmail.com'
    password = 'dmfn peul mjgq qjpk'  
    subject = 'Cab Booking Confirmation'

    # Setup MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body = 'Your cab booking has been confirmed. Please find the details attached.'

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
Cab.create("CAB123", "SUV", 50.0)  # Add a product if DB is empty

# Write product to JSON file and send an email
file = write_product_json(1)
if file:
    send_mail(file, "kavyashanmugavadivel@gmail.com")
    