import sqlite3

from database import Database
from models.book import Book


class Loan:
    def __init__(self,book_id, member_id, loan_date, due_date, returned, id=None):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.returned = returned

    def __str__(self):
        return f"Loan(id={self.id}, book_id={self.book_id}, member_id={self.member_id}, loan_date={self.loan_date}, due_date={self.due_date}, returned={self.returned})"

    def loan_out(self):
        db = Database("library.db")
        query1 = """INSERT INTO loans (book_id, member_id, loan_date, due_date, returned) VALUES (?, ?, ?, ?, ?)"""
        self.id = db.execute(query1, (self.book_id, self.member_id, self.loan_date, self.due_date, 0))
        query2 = """UPDATE books SET copies = copies - 1 WHERE id = ?"""
        db.execute(query2, (self.book_id,))
        print("Loan Out Successful")

    def return_book(self):
        db = Database("library.db")
        query = """UPDATE books SET copies = copies + 1 WHERE id = ?"""
        db.execute(query, (self.book_id,))
        query2 = """UPDATE loans SET returned = 1 WHERE id = ?"""
        db.execute(query2, (self.id,))
        print("Book returned successfully")

    @staticmethod
    def get_all():
        db = Database("library.db")
        query = """SELECT * FROM loans"""
        rows = db.fetchall(query, None)
        loans = []
        for row in rows:
            loan = Loan.from_db_row(row)
            loans.append(loan)
        return loans

    @staticmethod
    def from_db_row(row):
        id, book_id, member_id, loan_date, due_date, returned = row
        return Loan(book_id, member_id, loan_date, due_date, returned, id)

    @staticmethod
    def find_overdue():
        db = Database("library.db")
        query = """SELECT * FROM loans WHERE due_date < date('now') AND returned = 0"""
        rows = db.fetchall(query, None)
        loans = []
        for row in rows:
            loan = Loan.from_db_row(row)
            loans.append(loan)
        return loans

    @staticmethod
    def find_by_id(loan_id):
        db = Database("library.db")
        query = """SELECT * FROM loans WHERE id = ?"""
        rows = db.fetchall(query, (loan_id,))
        for row in rows:
            loan = Loan.from_db_row(row)
            return loan
