from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../frontend')

# In-memory database for demonstration purposes
patients = {}

# Patient class
class Patient:
    def __init__(self, patient_id, name, email, age, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.age = age
        self.medical_history = medical_history if medical_history else []

    def update_medical_history(self, record):
        self.medical_history.append(record)

# Routes for CRUD operations
@app.route('/')
def index():
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        patients[patient_id] = Patient(patient_id, name, email, age)
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/edit/<patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    patient = patients.get(patient_id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.email = request.form['email']
        patient.age = request.form['age']
        return redirect(url_for('index'))
    return render_template('edit_patient.html', patient=patient)

@app.route('/delete/<patient_id>')
def delete_patient(patient_id):
    if patient_id in patients:
        del patients[patient_id]
    return redirect(url_for('index'))

@app.route('/view/<patient_id>')
def view_patient(patient_id):
    patient = patients.get(patient_id)
    return render_template('view_patient.html', patient=patient)

if __name__ == '__main__':
    app.run(debug=True)
