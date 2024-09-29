import smtplib
from email.mime.text import MIMEText
import os
import json
import requests
from bs4 import BeautifulSoup

# Email Alerts
class EmailAlerts:
    def __init__(self, smtp_server, port):
        self.smtp_server = smtp_server
        self.port = port
        self.username = "ishaghule@gmail.com"
        self.password = "tiwu rkrn dwbe vedp"

    def send_email(self, to_email, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email

        try:
            print(f"Connecting to SMTP server: {self.smtp_server} on port {self.port}")
            server = smtplib.SMTP_SSL(self.smtp_server, self.port)
            server.login(self.username, self.password)
            print(f"Logged in as {self.username}")
            server.sendmail(self.username, to_email, msg.as_string())
            server.quit()
            print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def find_product_in_email(self, email_body):
        product_info = {}
        lines = email_body.split('\n')
        for line in lines:
            if "Product:" in line:
                product_info['product'] = line.split("Product:")[1].strip()
        return product_info

    def write_product_to_json(self, product_info, filename='product_info.json'):
        try:
            with open(filename, 'w') as json_file:
                json.dump(product_info, json_file)
            print(f"Product information written to {filename}")
        except Exception as e:
            print(f"Failed to write product information to JSON file: {e}")

# Patient Management
class Patient:
    def __init__(self, patient_id, name, email, age, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.age = age
        self.medical_history = medical_history if medical_history else []

    def update_medical_history(self, record):
        self.medical_history.append(record)
        print(f"Updated medical history for {self.name}.")

    def send_email_alert(self, subject, body):
        if self.email:
            email_alerts = EmailAlerts("smtp.gmail.com", 465)
            email_alerts.send_email(self.email, subject, body)
            product_info = email_alerts.find_product_in_email(body)
            email_alerts.write_product_to_json(product_info)

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print("Medical History:")
        for record in self.medical_history:
            print(record)

class PatientManagementSystem:
    def __init__(self):
        self.patients = {}

    def register_patient(self, patient_id, name, email, age):
        if patient_id in self.patients:
            print("Patient already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, email, age)
            print(f"Patient {name} registered with ID {patient_id}.")

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

# Network Communication
class NetworkDevice:
    def __init__(self, ip_address, device_type):
        self.ip_address = ip_address
        self.device_type = device_type

    def communicate(self):
        print(f"Communicating with {self.device_type} at {self.ip_address}")

    def send_data(self, data):
        print(f"Sending data to {self.device_type}: {data}")

    def receive_data(self):
        print(f"Receiving data from {self.device_type}")

# Web Scraper
class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch data from {self.url}: {e}")
            return None

    def parse_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Example: Extracting all paragraph texts
        data = [p.text for p in soup.find_all('p')]
        return data

    def write_data_to_json(self, data, filename='web_data.json'):
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
            print(f"Web data written to {filename}")
        except Exception as e:
            print(f"Failed to write web data to JSON file: {e}")

def main():
    # Patient Management
    pms = PatientManagementSystem()

    # Register patients
    pms.register_patient("001", "Isha Ghule", "ishaghule@gmail.com", 30)
    pms.register_patient("002", "Girish Chaudhari", "girishchaudhari251@gmail.com", 25)

    # Accessing patient information
    patient = pms.get_patient("001")
    if patient:
        patient.update_medical_history("Diagnosed with hypertension.")
        patient.send_email_alert("Medical Alert", "Your recent test results are available.\nProduct: Blood Pressure Monitor")
        patient.display_info()

    patient2 = pms.get_patient("002")
    if patient2:
        patient2.update_medical_history("Annual check-up completed.")
        patient2.display_info()

    # Network Communication
    router = NetworkDevice("192.168.1.1", "Router")
    router.communicate()
    router.send_data("Hello, Router!")
    router.receive_data()

    # Web Scraping
    scraper = WebScraper("https://www.apollopharmacy.in/")
    html_content = scraper.fetch_data()
    if html_content:
        web_data = scraper.parse_data(html_content)
        scraper.write_data_to_json(web_data)

if __name__ == "__main__":
    main()
