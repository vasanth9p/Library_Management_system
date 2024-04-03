"""
book.py: A module containing classes for managing books.
"""

class Book:
    """
    Represents a book with attributes such as title, author, and ISBN.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN (International Standard Book Number) of the book.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a Book object with given title, author, and ISBN.
        
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """
        Returns a string representation of the book.

        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class BookManager:
    """
    Manages a collection of Book objects.

    """

    def __init__(self):
        """
        Initializes a BookManager object with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book object to the list of books managed by the BookManager.

        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all the books managed by the BookManager.
        """
        for book in self.books:
            print(book)
