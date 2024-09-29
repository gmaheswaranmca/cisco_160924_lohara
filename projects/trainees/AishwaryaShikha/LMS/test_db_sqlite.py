from bookdb import bookTableCreate, createBook, readAllBooks, Book
# Create the books table if it doesn't already exist
bookTableCreate()

# Insert books into the database
id = createBook(Book(title='The Great Gatsby', price=300.0))
print(f'{id} is inserted')

id = createBook(Book(title='1984', price=250.0))
print(f'{id} is inserted')

# Read all books from the database
books = readAllBooks()
print(books)