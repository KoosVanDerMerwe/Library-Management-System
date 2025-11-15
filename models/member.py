import sqlite3

from database import Database


class Member:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Member(id={self.id}, name='{self.name}', email='{self.email}')"

    def save(self):
        db = Database("library.db")

        if self.id is None:
            query = """INSERT INTO members (name, email) VALUES(?, ?)"""
            self.id = db.execute(query, (self.name, self.email))
        else:
            query = """UPDATE members SET name=?, email=? WHERE id=?"""
            db.execute(query, (self.name, self.email, self.id))
        print("Member Saved Successfully")

    def delete(self):
        db = Database("library.db")
        if self.id is None:
            print("Member does not exist")
            return
        else:
            query = """DELETE FROM members WHERE id=?"""
            db.execute(query, (self.id,))
        print("Member Deleted Successfully")

    @staticmethod
    def get_all():
        db = Database("library.db")
        query = """SELECT * FROM members"""
        rows = db.fetchall(query, None)
        members = []
        for row in rows:
            member = Member.from_db_row(row)
            members.append(member)
        return members

    @staticmethod
    def from_db_row(row):
        id, name, email = row
        return Member(name=name, email=email, id=id)
