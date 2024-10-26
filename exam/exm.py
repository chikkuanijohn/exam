book=[]
def add_book(library, book):
    library.append(book)
    print(f'Book "{book["title"]}" added successfully.')

def update_book(library, title, new_details):
    for book in library:
        if book["title"].lower() == title.lower():
            book.update(new_details)
            print(f'Book "{title}" updated successfully.')
            return
    print(f'Book "{title}" not found.')

def remove_book(library, title):
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f'Book "{title}" removed successfully.')
            return
    print(f'Book "{title}" not found.')

def view_books(library):
    if library:
        print("Books in the library:")
        for book in library:
            print(f"- Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print("No books in the library.")

def search_book(library, title):
    for book in library:
        if book["title"].lower() == title.lower():
            print(f'Book "{title}" is available in the library.')
            print(f"Details - Author: {book['author']}, Year: {book['year']}")
            return
    print(f'Book "{title}" is not available in the library.')

def library_management_system():
    library = []
    while True:
        print('\nWelcome to the Library Management System')
        print("1. Add a book")
        print("2. Update a book")
        print("3. Remove a book")
        print("4. View all books")
        print("5. Search for a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the year of publication: ")
            book = {"title": title, "author": author, "year": year}
            add_book(library, book)
        elif choice == '2':
            title = input("Enter the title of the book to update: ")
            new_title = input("Enter the new title (leave blank to keep the same): ")
            new_author = input("Enter the new author (leave blank to keep the same): ")
            new_year = input("Enter the new year (leave blank to keep the same): ")
            new_details = {}
            if new_title:
                new_details["title"] = new_title
            if new_author:
                new_details["author"] = new_author
            if new_year:
                new_details["year"] = new_year
            update_book(library, title, new_details)
        elif choice == '3':
            title = input("Enter the title of the book to remove: ")
            remove_book(library, title)
        elif choice == '4':
            view_books(library)
        elif choice == '5':
            title = input("Enter the title of the book to search: ")
            search_book(library, title)
        elif choice == '6':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_management_system()
