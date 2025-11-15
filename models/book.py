from database import Database

class Book:
    def __init__(self, title, author, isbn, copies, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', copies={self.copies})"

    def save(self):
        db = Database("library.db")

        if self.id is None:
            query = """INSERT INTO books (title, author, isbn, copies) VALUES (?, ?, ?, ?)"""
            self.id = db.execute(query, (self.title, self.author, self.isbn, self.copies))
        else:
            query = """UPDATE books SET title=?, author=?, isbn=?, copies=? WHERE id=?"""
            db.execute(query, (self.title, self.author, self.isbn, self.copies, self.id))
        print("Book saved successfully")

    def delete(self):
        if self.id is None:
            print("Book does not exist")
            return

        db = Database("library.db")

        query = """DELETE FROM books WHERE id = ?"""
        db.execute(query, (self.id,))
        print("Book deleted successfully")

    @staticmethod
    def get_all():
        db = Database("library.db")
        query = """SELECT * FROM books"""
        rows = db.fetchall(query, None)
        books = []
        for row in rows:
            book = Book.from_db_row(row)
            books.append(book)
        return books

    @staticmethod
    def from_db_row(row):
        id, title, author, isbn, copies = row
        return Book(title, author, isbn, copies, id)

