"""
check.py: A module containing classes for managing book checkouts.
"""

class Checkout:
    """
    Represents a book checkout with attributes such as user ID and ISBN.

    Attributes:
        user_id (str): The ID of the user who checked out the book.
        isbn (str): The ISBN of the book being checked out.
    """

    def __init__(self, user_id, isbn):
        """
        Initializes a Checkout object with given user ID and ISBN.

        """
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        """
        Returns a string representation of the checkout.

        """
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"


class CheckoutManager:
    """
    Manages a collection of Checkout objects.

    """

    def __init__(self):
        """
        Initializes a CheckoutManager object with an empty list of checkouts.
        """
        self.checkouts = []

    def checkout_book(self, checkout):
        """
        Adds a Checkout object to the list of checkouts managed by the CheckoutManager.

        """
        self.checkouts.append(checkout)

    def list_checkouts(self):
        """
        Lists all the checkouts managed by the CheckoutManager.
        """
        for checkout in self.checkouts:
            print(checkout)
