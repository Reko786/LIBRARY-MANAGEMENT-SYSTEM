class Library:
    def __init__(self):
        self.books = {}

 ##### Below Is The Function To Add A Book #####      
        def add_book(self):
            while True:
                title = input("Enter Name Of Book To Add: ").strip()

                if not title:
                    print("Invalid Option!! The Book Title Cannot Be Empty. Please Try Again.")
                    continue

                if len(title) > 100:
                    print("Invalid Option!! The Book Title Is Too Long. Please Keep It Under 100 Characters.")
                    continue

                if any(char.isdigit() for char in title):
                    print("Invalid Option!! The Book Title Should Not Contain Numbers. Please Try Again.")
                    continue

                if title in self.books:
                    print("Book Already Exists. Please Add A Different book.")
                    return

                self.books[title] = 'available'
                print(f"Book '{title}' Added To The Library.")
                break

 ##### Below Is The Function To Borrow A Book ##### 
    
    def borrow_book(self):
        title = input("Enter Name Of Book To Borrow: ").strip()
        if not title:
            print("Invalid Option!!. Please try again.")
            return

        if title not in self.books:
            print("Book Not Found!! Please Check The Title And Try Again.")
        elif self.books[title] == 'Borrowed':
            print("Book Is Currently Borrowed. Please Try Another Book.")
        else:
            self.books[title] = 'Borrowed'
            print(f"You Have Borrowed '{title}'.")

     ##### Below Is The Function To Remove A Book ##### 

    def remove_book(self):
        title = input("Enter Book Name To Remove: ").strip()
        if not title:
            print("Invalid Option!! Please Try Again.")
            return

        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' Removed From The Library.")
        else:
            print("Book Not Found!! Please Check The Book Name And Try Again.")

 ##### Below Is The Function To Search A Book ##### 
    
    def search_book(self):
        title = input("Enter Book Name To Search: ").strip()
        if not title:
            print("Invalid Option!! Please Try Again.")
            return

        if title in self.books:
            status = self.books[title]
            print(f"Book '{title}' is {status}.")
        else:
            print("Book Not Found. Please Check The Book Name And Try Again.")

     ##### Below Is The Function To List All Books ##### 

    def list_books(self):
        if not self.books:
            print("No Books In The Library.")
        else:
            print("Listing All Books In The Library:")
            for title, status in self.books.items():
                print(f"Title: {title}, Status: {status}")


 ##### Below Is The Main Menu ##### 

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
            print("Exiting the Library Management System. Thanks For Visiting!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()






