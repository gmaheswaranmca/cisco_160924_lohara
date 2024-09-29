import sqlite3

class Database:
    def __init__(self, db_name='data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                patient_id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                age INTEGER,
                medical_history TEXT
            )
        ''')
        self.connection.commit()

    def insert_patient(self, patient_id, name, email, age, medical_history):
        self.cursor.execute('''
            INSERT INTO patients (patient_id, name, email, age, medical_history)
            VALUES (?, ?, ?, ?, ?)
        ''', (patient_id, name, email, age, medical_history))
        self.connection.commit()

    def get_patient(self, patient_id):
        self.cursor.execute('''
            SELECT * FROM patients WHERE patient_id = ?
        ''', (patient_id,))
        return self.cursor.fetchone()

    def update_medical_history(self, patient_id, medical_history):
        self.cursor.execute('''
            UPDATE patients SET medical_history = ? WHERE patient_id = ?
        ''', (medical_history, patient_id))
        self.connection.commit()

    def close(self):
        self.connection.close()
