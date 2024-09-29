import json
import requests

class PatientsApp:
    def __init__(self):
        self.url='http://localhost:5000'
    def read_all(self):
        res=requests.get(f'{self.url}/patients')
        return res.json()
    def read_by_id(self,id):
        res=requests.get(f'{self.url}/patients/{id}')
        return res.json()
    def create(self,patient_json_str):
        headers={'Content-type':'application/json'}
        res=requests.post(f'{self.url}/patients',data=patient_json_str,headers=headers)
        return res.json()
    def update(self,id,patient_json_str):
        headers={'Content-type':'application/json'}
        res=requests.put(f'{self.url}/patients/{id}',data=patient_json_str,headers=headers)
        return res.json()
    def delete(self,id):
        res=requests.delete(f'{self.url}/patients/{id}')
        return res.json()
    def search(self,patient_json_str):
        headers={'Content-type':'application/json'}
        res=requests.post(f'{self.url}/patients',data=patient_json_str,headers=headers)
        return res.json()
    #enddef
#endclass

app=PatientsApp()
def menu():
    print('<---------------------Healthcare Patient Management System----------------------->\n')
    print('Choose one of the options below...')
    choice=int(input('''1.Display Patient Records
                        2.Get Patient Record By ID,
                        3.Add a patient record, 
                        4.Update an existing patient record, 
                        5.Delete an existing record, 
                        6.Search Patient record by the disease
                        7.Mail the patient records to Business Owner
                        8.Web Scraping
                        9.Write Patients Records to JSON file
                        10.Display ID's using Threading
                        11.Exit\n 
                        ENTER YOUR CHOICE:'''))
    if choice==1:
        patients=app.read_all()
        print(patients)
    elif choice==2:
        id=int(input('Enter ID:'))
        patient=app.read_by_id(id)
        print(patient)
    elif choice==3:
        name=input('Enter Name:')
        age=input('Enter age:')
        disease=input('Enter disease that you are diagnosed with:')
        patient_dict={'name':name,'age':age,'disease':disease}
        patient_json_str=json.dumps(patient_dict)
        patient=app.create(patient_json_str)
        print(patient)
    elif choice==4:
        id=int(input('Enter the ID that you wish to update:'))
        old_record=app.read_by_id(id)
        name=input(f'Name({old_record["name"]}): ')
        age=input(f'Age({old_record["age"]}): ')
        disease=input(f'Enter disease patient is diagnosed with({old_record["disease"]}):')
        patient_dict={'name':name,'age':age,'disease':disease}
        patient_json_str=json.dumps(patient_dict)
        patient=app.update(id,patient_json_str)
        print('Updated Succesfully')
        print(patient)
    elif choice==5:
        id=int(input('Enter ID you wish to delete:'))
        old_record=app.read_by_id(id)
        print(old_record)
        if input('Are you sure you want to delete this patient record?')=='yes':
            app.delete(id)
            print('Deleted Successfully!')
    elif choice==6:
        name=input('Enter Name:')
        age=input('Enter age:')
        disease=input('Enter disease that you are diagnosed with:')
        patient_dict={'name':name,'age':age,'disease':disease}
        patient_json_str=json.dumps(patient_dict)
        patient=app.search(patient_json_str)
        print(patient)
    elif choice==7:
        try:
            import smtplib as smtp
            connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
            email_addr = 'bhavana9678@gmail.com'
            email_passwd = 'oqtc afjh sgop eglz'
            connection.login(email_addr, email_passwd)
            patients=app.read_all()
            patient_json_str=json.dumps(patients)
            subject = "Patient Records"
            body = f'Hi! all the patient records are sent in json format..\n{patient_json_str}'
            message = f'Subject: {subject}\n\n{body}'
            connection.sendmail(from_addr=email_addr, to_addrs='bhavanaa9678@gmail.com',msg=message)
            connection.close()
            print("Email sent successfully!")
        except Exception as e:
            print("Server is not responsing!")
    elif choice==8:
        import requests
        from bs4 import BeautifulSoup
        url='https://www.sakraworldhospital.com/' 
        news_res=requests.get(url)
        soup=BeautifulSoup(news_res.content,'html.parser')
        headings=soup.find_all('html')
        with open('headings.txt','w',encoding='UTF-8') as news_file:
            for h in headings:
                news_file.write(h.text)
                news_file.write('\n')
        print("INFORMATION GATHERED!!!")
    elif choice==9:
        patients=app.read_all()
        patient_json_str=json.dumps(patients)
        with open('patients.json','w') as patients_data:
            json.dump(patients,patients_data)
        print("JSON File created using Patients data!")
    elif choice==10:
        import time
        import threading
        def print_id():
            thread_id = threading.get_ident()
            for i in range(3):
                print(f'{i}@{thread_id}')
            # time.sleep(0.025)
        threads=[]
        for i in range(3):
            thread = threading.Thread(target=print_id)
            threads.append(thread)
            thread.start()  # Start the thread
        for i in range(3):
            thread.join()   # Wait for the thread to finish
        print_id()
    elif choice==11:
            pass
    else:
        print('''Invalid input''')
    return choice

def menus():
    choice=menu()
    while choice!=11:
        choice=menu()
    print('''Thanks for using the Application!''')

#driver program
menus()




