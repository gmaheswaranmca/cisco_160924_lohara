import sqlite3

class BookDB:
    def __init__(self, db_name='library.db'):
        self.db_name = db_name

    def display_stock(self):
        """Display stock information for all books."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, stock FROM books')
            books = cursor.fetchall()
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Stock: {book[2]}")

    def calculate_total_stock(self):
        """Calculate and return the total stock of all books in the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SUM(stock) FROM books')
            total_stock = cursor.fetchone()[0]
        return total_stock if total_stock is not None else 0  
