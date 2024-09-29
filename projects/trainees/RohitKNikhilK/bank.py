# Step 1: Create and Initialize the Database

def create_database():
    import sqlite3  # Import only needed for this function
    conn = sqlite3.connect('bank_db')  # Create a connection to 'bank.db' SQLite database
    cursor = conn.cursor()             # Create a cursor object to interact with the database
    
    # Create a 'bank_account' table if it doesn't exist already
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_account (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    ''')
    
    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

# Step 2: Add a New Bank Account
def add_account(account_name, initial_balance):
    import sqlite3  # Import only needed for this function
    conn = sqlite3.connect('bank_db')  # Connect to the SQLite database
    cursor = conn.cursor()             # Create a cursor object
    
    # Insert a new account with a name and initial balance
    cursor.execute('INSERT INTO bank_account (account_name, balance) VALUES (?, ?)', 
                   (account_name, initial_balance))
    
    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

# Step 3: Check Account Balance
def check_balance(account_id):
    import sqlite3  # Import only needed for this function
    conn = sqlite3.connect('bank_db')  # Connect to the database
    cursor = conn.cursor()             # Create a cursor object
    
    # Retrieve balance for a specific account using account_id
    cursor.execute('SELECT balance FROM bank_account WHERE account_id = ?', (account_id,))
    balance = cursor.fetchone()[0]     # Fetch the first result (balance)
    
    conn.close()   # Close the connection
    return balance # Return the balance

# Step 4: Deposit Money into the Account
def deposit(account_id, amount):
    import sqlite3  # Import only needed for this function
    conn = sqlite3.connect('bank_db')  # Connect to the database
    cursor = conn.cursor()             # Create a cursor object
    
    # Update the balance by adding the deposit amount
    cursor.execute('UPDATE bank_account SET balance = balance + ? WHERE account_id = ?', 
                   (amount, account_id))
    
    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

# Step 5: Withdraw Money from the Account
def withdraw(account_id, amount):
    import sqlite3  # Import only needed for this function
    conn = sqlite3.connect('bank_db')  # Connect to the database
    cursor = conn.cursor()             # Create a cursor object
    
    # Check current balance before withdrawing
    cursor.execute('SELECT balance FROM bank_account WHERE account_id = ?', (account_id,))
    balance = cursor.fetchone()[0]     # Get the current balance
    
    if balance >= amount:
        # If there are enough funds, update the balance by subtracting the withdrawal amount
        cursor.execute('UPDATE bank_account SET balance = balance - ? WHERE account_id = ?', 
                       (amount, account_id))
        conn.commit()  # Commit the transaction
    else:
        print("Insufficient funds")    # If not enough balance, display a message
    
    conn.close()  # Close the connection

# Step 6: Simulate File Transfer
def transfer_file(source, destination):
    import shutil  # Import only needed for this function
    try:
        shutil.copy(source, destination)  # Simulate copying a file from source to destination
        print(f"File transferred from {source} to {destination}")
    except Exception as e:
        print(f"Failed to transfer file: {e}")

# Step 7: Send Email Alert
# Step 7: Send Email Alert
def send_email_alert(subject, message, to_email):
    import smtplib                    # Import only needed for this function
    from email.mime.text import MIMEText   # Import only needed for this function
    
    from_email = 'kadadinikhil2000@gmail.com'   # Sender email
    password = 'eojh cako hdit rwhn'             # Replace with sender email password (use an app password if using Gmail)
    
    msg = MIMEText(message)                     # Create the email body
    msg['Subject'] = subject                    # Set the email subject
    msg['From'] = from_email                    # Set the sender's email
    msg['To'] = to_email                        # Set the recipient's email
    
    try:
        # Connect to Gmail's SMTP server using SSL encryption
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)      # Log in to the SMTP server
        server.sendmail(from_email, to_email, msg = "HDFC Bank Alerts !!!") # Corrected line for sending the email
        server.quit()  # Close the SMTP server connection
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Step 8: Multithreading for Deposits and Withdrawals
import threading
def process_transactions(account_id, deposit_amount, withdraw_amount):
    #import threading
    t1 = threading.Thread(target=deposit, args=(account_id, deposit_amount))
    t2 = threading.Thread(target=withdraw, args=(account_id, withdraw_amount))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# Step 9: Run Concurrent Tasks (Email and File Transfer)
def run_concurrent_tasks():
    t1 = threading.Thread(target=transfer_file, args=('statement.txt', 'backup_statement.txt'))
    t2 = threading.Thread(target=send_email_alert, args=(
        'Account Balance Update',                
        'Hello Rohit, your account balance has been updated.',  
        'kaldaterohit2611@gmail.com'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# Initialize database and add an account for demonstration
create_database()
add_account("Rohit kaldate's Account", 1000.0)

# Check balance before transactions
print("Initial Balance:", check_balance(1))



# Step 8: Run deposit and withdraw concurrently using multithreading
#process_transactions(1, 500.0, 200.0)  # Deposit 500 and Withdraw 200 concurrently

# Check balance after transactions
print("Balance after transactions:", check_balance(1))

# Step 9: Run file transfer and email alert concurrently
run_concurrent_tasks()