from Patient import Patient 
#patient = Patient(100,'Rohit')
#print(patient)

#2. patients[]
patients = []

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
    print('Patient created successfully')
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
#5. patient_display()
def patient_display():
    global patients
    for patient in patients:
        print(patient)
#patient_display_byid(id)
def patient_display_byid(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            return 
        #endif
    #endfor 
    print('Invalid id')
#patient_update(id)
def patient_update(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            name = input(f'Enter new name({patient.name}):')
            patient.name = name 
            print('Patient updated successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
