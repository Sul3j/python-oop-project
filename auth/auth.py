import hashlib
import sqlite3
import colors.colors as color


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, db):
        try:
            db.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
            db.connection.commit()
            print(color.green("Zarejestrowano użytkownika"))
        except sqlite3.IntegrityError:
            print(color.red("Nazwa użytkownika już istnieje wybierz inną"))

    @staticmethod
    def login(db, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = db.cursor.fetchone()
        if user:
            print(color.green("Zalogowano!"))
            return True
        else:
            print(color.red("Nieprawidłowe dane logownia"))
            return False