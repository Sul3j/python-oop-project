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
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_player(self, name, wins):
        c = self.connection.cursor()
        try:
            c.execute('INSERT INTO players (name, wins) VALUES (?, ?)', (name, wins))
        except sqlite3.IntegrityError:
            c.execute('UPDATE players SET wins = wins + ? WHERE name = ?', (wins, name))
        self.connection.commit()

    def show_top(self):
        c = self.connection.cursor()
        self.connection.commit('SELECT name, wins FROM players ORDER BY wins DESC LIMIT 100')
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

