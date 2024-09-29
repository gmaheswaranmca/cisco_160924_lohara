import sqlite3

def create_table(db_name):
    """Create the books table in the SQLite database if it doesn't exist."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id TEXT PRIMARY KEY,
                title TEXT,
                price TEXT,
                stock INTEGER
            )
        ''')
        conn.commit()

def is_database_filled(db_name):
    """Check if the database is already filled with books."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM books')
        count = cursor.fetchone()[0]
    return count > 0

def insert_books(db_name, books):
    """Insert books into the database."""
    print(f"Inserting books: {books}")  
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.executemany('INSERT OR IGNORE INTO books (id, title, price, stock) VALUES (?, ?, ?, ?)', books)
        conn.commit()


def add_book(db_name, book_id, title, price, stock):
    """Insert or replace a single book in the database."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO books (id, title, price, stock) VALUES (?, ?, ?, ?)', 
                       (book_id, title, price, stock))
        conn.commit()

def load_books(db_name):
    """Load books from the database into memory."""
    books = {}
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        print(f"Loaded books from DB: {rows}") 
        for row in rows:
            books[row[0]] = {'title': row[1], 'price': row[2], 'stock': row[3]}
    return books


def update_book(db_name, book_id, title=None, price=None, stock=None):
    """Update a book in the database."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        if title:
            cursor.execute('UPDATE books SET title = ? WHERE id = ?', (title, book_id))
        if price:
            cursor.execute('UPDATE books SET price = ? WHERE id = ?', (price, book_id))
        if stock is not None:
            cursor.execute('UPDATE books SET stock = ? WHERE id = ?', (stock, book_id))
        conn.commit()

def delete_book(db_name, book_id):
    """Delete a book by ID."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()

def find_book_by_id(db_name, book_id):
    """Find a book by its ID."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        return cursor.fetchone()


def borrow_book(db_name, book_id):
    """Borrow a book by ID, decrementing its stock by 1."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
       
        cursor.execute('SELECT stock FROM books WHERE id = ?', (book_id,))
        book = cursor.fetchone()
        
        if book is None:
            print("Book not found.")
            return False

        current_stock = book[0]

        if current_stock > 0:
           
            cursor.execute('UPDATE books SET stock = stock - 1 WHERE id = ?', (book_id,))
            conn.commit()
            print(f"Borrowed 1 copy of the book (ID: {book_id}). New stock: {current_stock - 1}")
            return True
        else:
            print("No stock available to borrow.")
            return False
