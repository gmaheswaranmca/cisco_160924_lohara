import re

class Search:
    def __init__(self, filename='default.txt'):
        """Initialize with the filename and load the lines into a list."""
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.lines = file.readlines()  # Read all lines into a list
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.filename} was not found.")
    
    def clean(self):
        """Clean special characters from each line using regex."""
        self.lines = [re.sub(r'[^\w\s]', '', line) for line in self.lines]
    
    def getLines(self, word):
        """Extract lines that contain the specified word or pattern."""
        result = [word]  # Start with the word being searched
        for i, line in enumerate(self.lines, 1):
            if re.search(word, line, re.IGNORECASE):  # Case-insensitive search
                result.append((i, line.strip()))  # Add (line_number, line_content)
        return result