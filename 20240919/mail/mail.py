import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
subject = "Test Email from Python"
body = "This is a test email sent from Python!"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body
msg.attach(MIMEText(body, 'plain'))

# SMTP server details
smtp_server = "smtp.gmail.com"
port = 587  # For TLS (or use 465 for SSL)
password = "your_email_password"

# Create a secure connection with the SMTP server
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection with TLS
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
