# Library_Management_system

﻿The entire Library Management System as follows:

1. Book Management:

    • The Book class represents a book with attributes such as title, author, and ISBN.
    • The BookManager class manages a collection of Book objects, providing methods to add and list books.

2. User Management:

    • The User class represents a user with attributes such as name and user ID.
    • The UserManager class manages a collection of User objects, providing methods to add and list users.
      
3. Checkout Management:

    • The Checkout class represents a book checkout with attributes such as user ID and ISBN.
    • The CheckoutManager class manages a collection of Checkout objects, providing methods to checkout books and list checkouts.

4. Storage Management:

    • The Storage class provides methods for saving and loading data to/from JSON files.
    • It includes methods for saving and loading books, users, and checkouts to/from JSON files.

5. Main Program Execution:

    • The main.py module serves as the main program.
   
    • It imports classes from book.py, user.py, check.py, and storage.py.
   
    • It contains the main_menu() function to display the main menu options and prompt for user input.
   
    • The main() function executes the main program loop, allowing users to interact with the system:
   
    • Users can add books, list books, add users, list users, checkout books, list checkouts, and exit the program.
   
    • Data is loaded from JSON files (books.json, users.json, checkouts.json) at the start of the program and saved back to these files after       any modifications.
   
    • The program runs until the user chooses to exit.


Overall, the pipeline ensures effective management of books, users, and checkouts in the Library Management System, with data persistently stored and retrievable from JSON files.
