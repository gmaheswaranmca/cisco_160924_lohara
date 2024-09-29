import multiprocessing
import threading
import requests
from bs4 import BeautifulSoup
import subprocess
import smtplib as smtp
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

# Book class definition
class Book:
    def __init__(self, id, title, price, copies):
        self.id = id
        self.title = title
        self.price = price
        self.copies = copies
        
    def __str__(self):
        return f'[id={self.id}, title={self.title}, price={self.price}, copies={self.copies}]'
    
    def __repr__(self):
        return self.__str__()


# Global book list
books = []


# Functions to manage books
def book_add(id, title, price, copies):
    global books
    book = Book(id, title, price, copies)
    books.append(book)


def book_remove(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
            if input('Are you sure to delete (yes/no)? ').lower() == 'yes':
                books.remove(book)
                print('Book deleted successfully')
            return
    print(f'No such book with id {id}')


def book_readbyid(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
            return
    print(f"Book with id {id} not found.")


def book_updatebyid(id):
    global books
    for book in books:
        if book.id == id:
            title = input("Enter new title for the book: ")
            price = float(input("Enter new price for the book: "))
            copies = int(input("Enter new number of copies: "))
            book.title = title
            book.price = price
            book.copies = copies
            print(f"Book with id {id} has been updated.")
            return
    print(f"Book with id {id} not found.")


def book_display():
    global books
    for book in books:
        print(book)


# Web scraping function
def scrape_books():
    print("Scraping books...")
    url = 'https://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all('h3')

    books_info = []
    for heading in headings:
        book_title = heading.find('a')['title']
        books_info.append(book_title)

    # Save book titles to a text file
    with open('books_info.txt', 'w', encoding='UTF-8') as book_file:
        for book in books_info:
            book_file.write(book + '\n')

    print('Books information gathered and saved to books_info.txt')
    return books_info


# Email sending function
def send_email(books_info):
    print("Sending email...")
    serial = subprocess.check_output('wmic bios get serialnumber').decode("utf-8").replace('SerialNumber', '').strip() 

    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    email_addr = 'akharche45@gmail.com'
    email_passwd = 'hdkf ucnk ppzu thqw'  # replace with your actual password
    connection.login(email_addr, email_passwd)

    receiver = 'kannushikha15@gmail.com'
    dt_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    subject = f'Books Info {dt_time} @{serial}'
    body = "Here are the scraped book titles:\n\n" + "\n".join(books_info)

    msg = MIMEMultipart()
    msg['From'] = email_addr
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    connection.sendmail(email_addr, receiver, msg.as_string())
    connection.close()
    print('Email sent successfully.')


# Multithreading function to perform scraping and email sending in parallel
def threaded_scrape_and_email():
    books_info = scrape_books()

    # Create a new thread for sending email
    email_thread = threading.Thread(target=send_email, args=(books_info,))
    email_thread.start()

    # Meanwhile, we can perform other tasks
    print("Other tasks can proceed while email is being sent.")

# Multi-processing demonstration
def print_numbers():
    pid = os.getpid()
    for i in range(5):
        print(f'{i}@{pid}')
        time.sleep(0.125)


# Main menu
def menu():
    choice = int(input('''1 - Add book
2 - Delete book by id
3 - Display all books
4 - Read book by id
5 - Update book by id
6 - Scrape books and send email (single-thread)
7 - Scrape books and send email (multi-threaded)
8 - Run multiprocessing example
9 - End
Your choice: '''))
    
    if choice == 1:
        id = int(input('Enter book id: '))
        title = input('Enter book title: ')
        price = float(input('Enter book price: '))
        copies = int(input('Enter number of copies: '))
        book_add(id, title, price, copies)
    elif choice == 2:
        id = int(input('Enter book id to delete: '))
        book_remove(id)
    elif choice == 3:
        book_display()
    elif choice == 4:
        id = int(input('Enter book id to read: '))
        book_readbyid(id)
    elif choice == 5:
        id = int(input('Enter book id to update: '))
        book_updatebyid(id)
    elif choice == 6:
        books_info = scrape_books()
        send_email(books_info)
    elif choice == 7:
        # Multithreaded scraping and email sending
        threaded_scrape_and_email()
    elif choice == 8:
        # Demonstrating multiprocessing
        processes = []
        for i in range(5):
            process = multiprocessing.Process(target=print_numbers)
            processes.append(process)
            process.start()

        # Optionally, join the processes to wait for their completion
        for process in processes:
            process.join()

    elif choice == 9:
        pass
    else:
        print('Invalid menu')
    
    return choice


def menus():
    choice = menu()
    while choice != 9:
        choice = menu()
    print('Thank you for using the library management system.')


# Driver program
if __name__ == "__main__":
    menus()