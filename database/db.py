import sqlite3
import colors.colors as color

class Database:
    def __init__(self, db_name="app.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_user_table()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                balance INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                wins INTEGER DEFAULT 0
            )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_player_ranking_value(self, name, wins):
        c = self.connection.cursor()
        try:
            c.execute('INSERT INTO ranking (name, wins) VALUES (?, ?)', (name, wins))
        except sqlite3.IntegrityError:
            c.execute('UPDATE ranking SET wins = ? WHERE name = ?', (wins, name))
        self.connection.commit()

    def show_top(self):
        c = self.connection.cursor()
        c.execute('SELECT name, wins FROM ranking ORDER BY wins DESC LIMIT 100')
        rows = c.fetchall()
        print(color.yellow("\nTOP 100 Graczy:"))
        for row in rows:
            print(f"{row[0]}: {row[1]} PLN")
        print()

    def add_user(self, username, password):
        c = self.connection.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(color.red("Użytkownik już istnieje!"))

    def get_user(self, username):
        c = self.connection.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        return c.fetchone()

    def get_user_balance(self, username):
        c = self.connection.cursor()
        c.execute("SELECT balance FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        return result[0] if result else None

    def update_user_balance(self, username, balance):
        c = self.connection.cursor()
        c.execute("UPDATE users SET balance = ? WHERE username = ?", (balance, username))
        self.connection.commit()

    def get_user_wins(self, username):
        c = self.connection.cursor()
        c.execute("SELECT wins FROM ranking WHERE name = ?", (username,))
        result = c.fetchone()
        return result[0] if result else 0