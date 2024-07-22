class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def borrow_book(self, isbn):
        book = self.find_book(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            print(f"Book '{book.title}' borrowed successfully.")
        elif not book:
            print(f"Book with ISBN {isbn} not found.")
        else:
            print(f"Book '{book.title}' is already borrowed.")

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print(f"Books matching '{title}':")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")

    def list_all_books(self):
        if self.books:
            print("Listing all books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. List All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == '3':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == '4':
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == '5':
            library.list_all_books()
        elif choice == '6':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




