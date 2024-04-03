"""
storage.py: A module containing a Storage class for saving and loading data to/from JSON files.
"""

import json
from book import Book  # Importing Book class from book.py
from user import User
from check import Checkout  

class Storage:
    """
    Provides methods for saving and loading data to/from JSON files.
    """

    @staticmethod
    def save_books(books, filename):
        """
        Saves a list of Book objects to a JSON file.

        """
        with open(filename, 'w') as file:
            json.dump([vars(book) for book in books], file)

    @staticmethod
    def load_books(filename):
        """
        Loads a list of Book objects from a JSON file.

        Returns:
            list: List of Book objects loaded from the JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            print("Failed to load books.Please check the json file. Error....")
            return []

    @staticmethod
    def save_checkouts(checkouts, filename):
        """
        Saves a list of Checkout objects to a JSON file.

        """
        with open(filename, 'w') as file:
            json.dump([vars(checkout) for checkout in checkouts], file)

    @staticmethod
    def load_checkouts(filename):
        """
        Loads a list of Checkout objects from a JSON file.

        Returns:
            list: List of Checkout objects loaded from the JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Checkout(**checkout) for checkout in data]
        except FileNotFoundError:
            print("Failed to load checkouts.Please check the json file. Error....")
            return []

    @staticmethod
    def save_users(users, filename):
        """
        Saves a list of User objects to a JSON file.

        """
        with open(filename, 'w') as file:
            json.dump([vars(user) for user in users], file)

    @staticmethod
    def load_users(filename):
        """
        Loads a list of User objects from a JSON file.

        Returns:
            list: List of User objects loaded from the JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [User(**user) for user in data]
        except FileNotFoundError:
            print("Failed to load users.Please check the json file. Error....")
            return []
