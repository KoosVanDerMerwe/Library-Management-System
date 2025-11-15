from traceback import print_tb

from models.book import Book
from models.member import Member
from models.loan import Loan
from database import Database
import datetime


class LibraryManager:
    def __init__(self):
        pass

    def __str__(self):
        return "Library Manager"

    def main_menu(self):
        while True:
            print("\n" + "=" * 40)
            print("        LIBRARY MANAGEMENT SYSTEM")
            print("=" * 40)
            print("1. Book Management")
            print("2. Member Management")
            print("3. Loan a Book")
            print("4. Return a Book")
            print("5. Exit System")
            print("-" * 40)

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.book_menu()
            elif choice == "2":
                self.member_menu()
            elif choice == "3":
                self.loan_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                print("\nThank you for using Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("\n" + "=" * 30)
            print("         BOOK MANAGEMENT")
            print("=" * 30)
            print("1. Add New Book")
            print("2. Remove Book")
            print("3. View All Books")
            print("4. Back to Main Menu")
            print("-" * 30)

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("\n--- Add New Book ---")
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the ISBN of the book: ")
                copies = input("Enter the number of copies of the book: ")
                book = Book(title, author, isbn, copies)
                book.save()
                print(f"Book '{title}' added successfully.")

            elif choice == "2":
                print("\n--- Remove Book ---")
                print("Available Books:")
                print("-" * 50)
                books = Book.get_all()
                for book in books:
                    print(f"ID: {book.id} - {book.title} by {book.author}")

                book_id = input("\nEnter book ID to delete: ")
                book = Book("", "", "", "", id=int(book_id))
                book.delete()
                print(f"Book with ID {book_id} deleted successfully.")

            elif choice == "3":
                print("\n--- All Books in Library ---")
                print("-" * 50)
                books = Book.get_all()
                for book in books:
                    print(book)
            elif choice == "4":
                return
            else:
                print("Invalid choice. Please try again.")

    def member_menu(self):
        while True:
            print("\n" + "=" * 30)
            print("       MEMBER MANAGEMENT")
            print("=" * 30)
            print("1. Add New Member")
            print("2. Remove Member")
            print("3. View All Members")
            print("4. Back to Main Menu")
            print("-" * 30)

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("\n--- Add New Member ---")
                name = input("Enter the name of the member: ")
                email = input("Enter the email of the member: ")
                member = Member(name, email)
                member.save()

            elif choice == "2":
                print("\n--- Remove Member ---")
                print("Registered Members:")
                print("-" * 50)
                members = Member.get_all()
                for member in members:
                    print(f"ID: {member.id} - {member.name} ({member.email})")

                member_id = input("\nEnter member ID to delete: ")
                member = Member("", "", id=int(member_id))
                member.delete()

            elif choice == "3":
                print("\n--- All Library Members ---")
                print("-" * 50)
                members = Member.get_all()
                for member in members:
                    print(member)
            elif choice == "4":
                return
            else:
                print("Invalid choice. Please try again.")

    def loan_book(self):
        print("\n" + "=" * 30)
        print("         LOAN A BOOK")
        print("=" * 30)

        print("\nAvailable Books:")
        print("-" * 50)
        books = Book.get_all()
        available_books = [b for b in books if b.copies > 0]
        for book in available_books:
            print(f"ID: {book.id} - {book.title} by {book.author}")

        book_id = int(input("\nEnter book ID to loan: "))

        print("\nRegistered Members:")
        print("-" * 50)
        members = Member.get_all()
        for member in members:
            print(f"ID: {member.id} - {member.name}")

        member_id = int(input("\nEnter member ID to loan to: "))

        loan_date = datetime.datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        loan = Loan(book_id, member_id, loan_date, due_date, False)
        loan.loan_out()
        print("\nBook loaned successfully!")

    def return_book(self):
        print("\n" + "=" * 30)
        print("        RETURN A BOOK")
        print("=" * 30)

        print("\nActive Loans:")
        print("-" * 50)
        loans = Loan.get_all()
        for loan in loans:
            if not loan.returned:
                print(f"Loan ID: {loan.id} - Book ID: {loan.book_id}")

        book_id = int(input("\nEnter book ID to delete: "))
        loan = Loan(0, 0, "", "", True, id=book_id)
        loan.return_book()
        print("\nBook returned successfully!")