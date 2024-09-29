
import json

def export_books_to_json(books):
    """Export books data to a JSON file."""
    with open('books.json', 'w') as json_file:
        json.dump(books, json_file, indent=4)
