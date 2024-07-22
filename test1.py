class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        title = input("Enter Name Of Book To Add: ").strip()
        if not title:
            print("Invalid Option!! Please Try Again.")
            return

        if title in self.books:
            print("Book Already Exists. Please Add A Different Book.")
        else:
            self.books[title] = 'available'
            print(f"Book '{title}' Added To The Library.")

    def borrow_book(self):
        title = input("Enter Name Of Book To Borrow: ").strip()
        if not title:
            print("Invalid Option!!. Please try again.")
            return

        if title not in self.books:
            print("Book not found. Please check the title and try again.")
        elif self.books[title] == 'borrowed':
            print("Book is currently borrowed. Please try another book.")
        else:
            self.books[title] = 'borrowed'
            print(f"You have borrowed '{title}'.")

    def remove_book(self):
        title = input("Enter book title to remove: ").strip()
        if not title:
            print("Book title cannot be empty. Please try again.")
            return

        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed from the library.")
        else:
            print("Book not found. Please check the title and try again.")

    def search_book(self):
        title = input("Enter book title to search: ").strip()
        if not title:
            print("Book title cannot be empty. Please try again.")
            return

        if title in self.books:
            status = self.books[title]
            print(f"Book '{title}' is {status}.")
        else:
            print("Book not found. Please check the title and try again.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Listing all books in the library:")
            for title, status in self.books.items():
                print(f"Title: {title}, Status: {status}")

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
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.borrow_book()
        elif choice == '3':
            library.remove_book()
        elif choice == '4':
            library.search_book()
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()






