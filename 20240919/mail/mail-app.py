#https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''

import subprocess
serial = subprocess.check_output('wmic bios get serialnumber').decode("utf-8").replace('SerialNumber','').strip() 

import smtplib as smtp
from datetime import datetime
connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'pystud19@gmail.com'
email_passwd = 'yaxb hoco fihc prnn'
connection.login(email_addr, email_passwd)

receiver='gmaheswaranmca@gmail.com'
mail_body="I develop app to send mails"
dt_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
subject = f'my app {dt_time} @{serial}'

from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
msg['From'] = email_addr
msg['To'] = receiver
msg['Subject'] = subject
connection.sendmail(email_addr, receiver, msg.as_string())
connection.close()