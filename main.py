import database.db as database
import auth.auth as auth
import colors.colors as color

def main():
    db = database.Database()
    while True:
        print("\nWitaj w aplikacji")
        print("1. Zarejestruj się")
        print("2. Zaloguj się")
        print("3. Wyjdź")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            username = input(color.yellow("Wprowadź nazwę użytkownika: "))
            password = input(color.yellow("Wprowadź hasło: "))
            user = auth.User(username, password)
            user.register(db)

        elif choice == "2":
            username = input(color.yellow("Wprowadź nazwę użytkownika: "))
            password = input(color.yellow("Wprowadź hasło: "))
            auth.User.login(db, username, password)

        elif choice == "3":
            print(color.yellow("Zamykanie aplikacji."))
            db.close()
            break

        else:
            print(color.red("Nieprawidłowa opcja. Spróbuj ponownie."))

if __name__ == "__main__":
    main()


