"""
user.py: A module containing classes for managing users.
"""

class User:
    """
    Represents a user with attributes such as name and user ID.

    Attributes:
        name (str): The name of the user.
        user_id (str): The ID of the user.
    """

    def __init__(self, name, user_id):
        """
        Initializes a User object with given name and user ID.

        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """
        Returns a string representation of the user.

        """
        return f"Name: {self.name}, User ID: {self.user_id}"


class UserManager:
    """
    Manages a collection of User objects.

    Attributes:
        users (list): A list to store User objects.
    """

    def __init__(self):
        """
        Initializes a UserManager object with an empty list of users.
        """
        self.users = []

    def add_user(self, user):
        """
        Adds a User object to the list of users managed by the UserManager.

        """
        self.users.append(user)

    def list_users(self):
        """
        Lists all the users managed by the UserManager.
        """
        for user in self.users:
            print(user)
