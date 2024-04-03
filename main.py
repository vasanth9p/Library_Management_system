"""
main.py: A module containing the main program for a Library Management System.
"""
from book import Book, BookManager
from check import Checkout, CheckoutManager
from user import User, UserManager
from storage import Storage

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. List Checkouts")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    """
    Executes the main program loop for managing books, users, and checkouts.
    """
    # loads the exsisting data from the json files.

    book_manager = BookManager()
    checkout_manager = CheckoutManager()
    user_manager = UserManager()

    books = Storage.load_books("books.json")
    for book in books:
        book_manager.add_book(book)

    users = Storage.load_users("users.json")
    for user in users:
        user_manager.add_user(user)

    checkouts = Storage.load_checkouts("checkouts.json")
    for checkout in checkouts:
        checkout_manager.checkout_book(checkout)

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            book_manager.add_book(book)
            Storage.save_books(book_manager.books, "books.json")
            print("--------------------------Book added ---------------------------")
        elif choice == '2':
            print("--------------------------Book list ---------------------------")
            book_manager.list_books()
            print("------------------------------------------------------")
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            user_manager.add_user(user)
            Storage.save_users(user_manager.users, "users.json")
            print("----------------------User added ------------------")
        elif choice == '4':
            print("----------------------User list------------------")
            user_manager.list_users()
            print("--------------------------- --------------------")
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout = Checkout(user_id, isbn)
            checkout_manager.checkout_book(checkout)
            Storage.save_checkouts(checkout_manager.checkouts, "checkouts.json")
            print("-------------------------Book checked out --------------------")
        elif choice == '6':
            print("------------------------- checkout books list --------------------")
            checkout_manager.list_checkouts()
            print("----------------------------------------------")
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

