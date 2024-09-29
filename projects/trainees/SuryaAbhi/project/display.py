import sqlite3
from tabulate import tabulate


def load_books(db_name='library.db'):
    """Load the books from the database."""
    books = {}
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        for row in cursor.fetchall():
            books[row[0]] = {'title': row[1], 'price': row[2], 'stock': row[3]}
    return books


def display_books():
    """Display the books in a formatted table."""
    books = load_books()


    books_list = [
        (book_id, details['title'], details['price'], details['stock'])
        for book_id, details in books.items()
    ]


    headers = ["ID", "Title", "Price", "Stock"]
    print(tabulate(books_list, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center"))


if __name__ == "__main__":
    display_books()

    
