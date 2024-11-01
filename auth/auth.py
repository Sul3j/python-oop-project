import hashlib
import colors.colors as color

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, db):
        db.add_user(self.username, self.password)

    @staticmethod
    def login(db, username, password):
        user = db.get_user(username)
        if user and user[2] == hashlib.sha256(password.encode()).hexdigest():
            print(color.green("Zalogowano pomyślnie!"))
            return True
        else:
            print(color.red("Błędna nazwa użytkownika lub hasło."))
            return False