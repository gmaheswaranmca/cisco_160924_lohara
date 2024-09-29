import atexit
from db_manager import create_table, is_database_filled, insert_books, load_books, update_book, borrow_book, find_book_by_id, add_book
from scraper import scrape_books
from email_manager import send_mail
from utils import export_books_to_json
from tabulate import tabulate
import stock_manager

class LibrarySystem:
    def __init__(self):
        self.db_name = 'library.db'
        create_table(self.db_name)

       
        if not is_database_filled(self.db_name):
            print("Database is empty. Scraping data from the website...")
            books = scrape_books(limit=50)
            insert_books(self.db_name, books)

        self.books = load_books(self.db_name)

      
        atexit.register(self.export_books)

    def export_books(self):
        """Export books to a JSON file."""
        export_books_to_json(self.books)

    def reload_books(self):
        """Reload books from the database to refresh in-memory data."""
        self.books = load_books(self.db_name)

    def display_books_in_table(self):
        """Display all books in a table format."""
        books_list = [(book_id, book['title'], book['price'], book['stock']) for book_id, book in self.books.items()]
        headers = ["ID", "Title", "Price", "Stock"]
        
       
        print(tabulate(books_list, headers, tablefmt="fancy_grid", stralign="center", numalign="center"))

 



    def run(self):
        """Main program loop."""
        while True:
            print("\nMenu:")
            print("1. Add Book")
            print("2. Find Book by ID")
            print("3. Display All Books")
            print("4. Update Book by ID")
            print("5. Borrow Book by ID")
            print("6. Send Mail")
            print("7. Calculate Total Stock")
            
            print("8. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                price = input("Enter Price: ")
                stock = int(input("Enter Stock Quantity: "))
                add_book(self.db_name, book_id, title, price, stock)
                print('The book was added successfully.')
                self.reload_books()  

            elif choice == '2':
                book_id = input("Enter Book ID: ")
                book = find_book_by_id(self.db_name, book_id)
                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif choice == '3':
                self.display_books_in_table()

            elif choice == '4':
                book_id = input("Enter Book ID: ")
                title = input("Enter new Title (leave blank to skip): ")
                price = input("Enter new Price (leave blank to skip): ")
                stock = input("Enter new Stock (leave blank to skip): ")
                update_book(self.db_name, book_id, title or None, price or None, int(stock) if stock else None)
                print('The book details were updated successfully.')
                self.reload_books() 

            elif choice == '5':
                book_id = input("Enter Book ID: ")
                success = borrow_book(self.db_name, book_id)
                if success:
                    self.reload_books()  

            elif choice == '6':
                to_email = input("Enter recipient email: ")
                body = input("Enter email body: ")
                send_mail(to_email, body)

            elif choice == '7':
                db = stock_manager.BookDB()
                total_stock = db.calculate_total_stock()
                print(f"Total stock of all books: {total_stock}")



            elif choice == '8':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
   
    library_system = LibrarySystem()
    library_system.run()
