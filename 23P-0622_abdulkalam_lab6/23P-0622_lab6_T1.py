import random
from datetime import datetime, timedelta

#book class, member class, library class with methods for add/remove book, register/remove member, borrow/return book, search books, show overdue books. Menu for user interaction.
class Book:
    def __init__(self, book_no, title, author, quantity):
        self.book_no = book_no
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available_quantity = quantity


class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name
        self.borrowed_books = {}  # book_no -> borrow date
        self.max_books = 3


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    # Add Book
    def add_book(self, book_no, title, author, quantity):
        if book_no in self.books:
            self.books[book_no].quantity += quantity
            self.books[book_no].available_quantity += quantity
        else:
            self.books[book_no] = Book(book_no, title, author, quantity)

        print("Book added successfully.")

    # Remove Book
    def remove_book(self, book_no):
        if book_no in self.books:
            del self.books[book_no]
            print("Book removed.")
        else:
            print("Book not found.")

    # Register Member
    def register_member(self, member_id, name):
        if member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member_id] = Member(member_id, name)
            print("Member registered successfully.")

    # Remove Member
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member removed.")
        else:
            print("Member not found.")

    # Borrow Book
    def borrow_book(self, member_id, book_no):

        if member_id not in self.members:
            print("member is not ofund.")
            return

        if book_no not in self.books:
            print("book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_no]

        if len(member.borrowed_books) >= member.max_books:
            print("limit to borrow book is reached.")
            return

        if book.available_quantity <= 0:
            print("Not available.")
            return

        borrow_date = datetime.now() - timedelta(days=random.randint(0,20))
        member.borrowed_books[book_no] = borrow_date

        book.available_quantity -= 1

        print("Book borrowed successfully!.")

    # Return Book
    def return_book(self, member_id, book_no):

        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if book_no not in member.borrowed_books:
            print("This book was not borrowed by the member.")
            return

        del member.borrowed_books[book_no]
        self.books[book_no].available_quantity += 1

        print("Book returned successfully.")

    # Search Books
    def search_books(self, keyword):

        keyword = keyword.lower()

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(book.title, "-", book.author, "| Available:", book.available_quantity)

    # Show Overdue Books
    def show_overdue(self):

        today = datetime.now()

        for member in self.members.values():

            for book_no, date in member.borrowed_books.items():

                days = (today - date).days

                if days > 14:
                    book = self.books[book_no]
                    print(member.name, "has overdue book:", book.title)


# MENU

def menu():

    library = Library("FAST Library management system")

    while True:

        print("\n===== Library Menu =====")

        print("1 Add Book")
        print("2 Remove Book")
        print("3 Register Member")
        print("4 Remove Member")
        print("5 Borrow Book")
        print("6 Return Book")
        print("7 Search Books")
        print("8 Show Overdue Books")
        print("0 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_no = input("book_no: ")
            title = input("Title: ")
            author = input("Author: ")
            quantity = int(input("Quantity: "))
            library.add_book(book_no, title, author, quantity)

        elif choice == "2":
            book_no = input("book_no: ")
            library.remove_book(book_no)

        elif choice == "3":
            mid = input("Member ID: ")
            name = input("Name: ")
            library.register_member(mid, name)

        elif choice == "4":
            mid = input("Member ID: ")
            library.remove_member(mid)

        elif choice == "5":
            mid = input("Member ID: ")
            book_no = input("book_no: ")
            library.borrow_book(mid, book_no)

        elif choice == "6":
            mid = input("Member ID: ")
            book_no = input("book_no: ")
            library.return_book(mid, book_no)

        elif choice == "7":
            keyword = input("Enter title or author: ")
            library.search_books(keyword)

        elif choice == "8":
            library.show_overdue()

        elif choice == "0":
            print("exiting......")
            break

        else:
            print("wrong choice.")


menu()