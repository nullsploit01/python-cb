class Library:
    def __init__(self):
        self.books = {}  

    def add_book(self, title):
        if title in self.books:
            print(f"The book '{title}' already exists in the library.")
        else:
            self.books[title] = True
            print(f"Added the book '{title}' to the library.")

    def checkout_book(self, title):
        if title in self.books and self.books[title]:
            self.books[title] = False
            print(f"Checked out the book '{title}'.")
        else:
            print(f"Cannot checkout '{title}'. It may not exist or is already checked out.")

    def return_book(self, title):
        if title in self.books and not self.books[title]:
            self.books[title] = True
            print(f"Returned the book '{title}' to the library.")
        else:
            print(f"Cannot return '{title}'. It may not have been checked out or does not exist in the library.")

library = Library()
while True:
    print("\nLibrary Menu")
    print("1. Add a book")
    print("2. Checkout a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        book_title = input("Enter the title of the book to add: ")
        library.add_book(book_title)
    elif choice == '2':
        book_title = input("Enter the title of the book to checkout: ")
        library.checkout_book(book_title)
    elif choice == '3':
        book_title = input("Enter the title of the book to return: ")
        library.return_book(book_title)
    elif choice == '4':
        print("Exiting the Library system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

