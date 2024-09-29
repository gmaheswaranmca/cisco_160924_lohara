import smtplib as smtp
from email.mime.text import MIMEText

def send_mail(to_email, body):
    """Send an email notification."""
    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    email_addr = 'deevsurya14@gmail.com'
    email_passwd = 'fqhw xeie oajm wspc'
    
    connection.login(email_addr, email_passwd)
    connection.sendmail(from_addr=email_addr, to_addrs=to_email, msg=body)
    connection.close()

    print('Mail sent successfully')
