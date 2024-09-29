import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'muskanmalhotra2910@gmail.com'
email_passwd = 'tnvk jbgx ezru skdy'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='akharche45@gmail.com', msg="Sent from Muskan. Hehe")
connection.close()
print('Mail sent successfully')