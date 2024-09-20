#https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'pystud19@gmail.com'
email_passwd = 'yaxb hoco fihc prnn'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Sent from my IDE. Hehe")
connection.close()