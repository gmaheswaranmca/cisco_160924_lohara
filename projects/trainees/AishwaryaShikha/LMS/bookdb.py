import sqlite3

# 1. Connect to the SQLite database
def connect():
    con = sqlite3.connect('books_db.db')
    return con

# 2. Create the books table with an additional 'copies' column
def bookTableCreate():
    sql = """CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        price REAL NOT NULL,
        copies INTEGER NOT NULL  -- Adding the 'copies' column
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

# 3. Book class
class Book:
    def __init__(self, id=None, title='', price=0.0, copies=0):
        self.id = id
        self.title = title
        self.price = price
        self.copies = copies  # Adding 'copies' as a new attribute
    
    def __str__(self):
        return f'[{self.id}, {self.title}, {self.price}, {self.copies}]'  # Including 'copies' in string representation
    
    def __repr__(self):
        return self.__str__()

# 4. Create a book (insert a new record into the database, including copies)
def createBook(book):
    sql = """INSERT INTO books(title, price, copies)
    VALUES(?,?,?)"""  # Including 'copies' in the query
    params = (book.title, book.price, book.copies)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    id = cur.lastrowid
    con.commit()
    con.close()
    return id

# 5. Read all books (fetch all records, including copies)
def readAllBooks():
    sql = """SELECT id, title, price, copies FROM books"""  # Including 'copies' in the query
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchall()
    con.close()

    books = []
    for row in result:
        books.append(Book(id=row[0], title=row[1], price=row[2], copies=row[3]))  # Fetching 'copies'
    return books

# 6. Search books by title, price, or copies
def searchBooks(title, price, copies):
    title = title.strip()
    sql = """SELECT id, title, price, copies FROM books
             WHERE (? == '' OR title=?) AND 
                   (? == 0 OR price=?) AND
                   (? == 0 OR copies=?)"""  # Including 'copies' in search
    params = (title, title, price, price, copies, copies)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchall()
    con.close()

    books = []
    for row in result:
        books.append(Book(id=row[0], title=row[1], price=row[2], copies=row[3]))  # Fetching 'copies'
    return books

# 7. Update a book (including updating copies)
def updateBook(book):
    sql = """UPDATE books
    SET title=?, price=?, copies=?  -- Updating the 'copies' field
    WHERE id=?"""
    params = (book.title, book.price, book.copies, book.id)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()

# 8. Delete a book
def deleteBook(id):
    sql = """DELETE FROM books WHERE id=?"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()

# 9. Read a book by its ID (including fetching copies)
def readBookById(id):
    sql = """SELECT id, title, price, copies FROM books WHERE id=?"""  # Including 'copies' in the query
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql, params)
    result = response.fetchone()
    con.close()

    if result:
        book = Book(id=result[0], title=result[1], price=result[2], copies=result[3])  # Fetching 'copies'
    else:
        book = None
    return book

# Initialize the database and table
bookTableCreate()
