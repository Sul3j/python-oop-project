from database.db import Database
from game.blackJack import BlackJack
from game.oneArmedBandit import OneArmedBandit
from game.player import Player
from game.roulette import Roulette
import colors.colors as color
import random

class Casino:
    def __init__(self):
        self.db_connection = Database()
        self.games = {
            '1': 'Ruletka',
            '2': 'Jednoręki Bandyta',
            '3': 'Blackjack',
        }

    def choose_game(self):
        print(color.red("Wybierz grę: "))
        for key, value in self.games.items():
            print(f"{key}: {value}")
        print('4: Wyświetl TOP 100 graczy')
        print('5: Wyjdź z gry')
        choice = input(color.yellow("Wybierz opcje: "))
        return choice

    def launch_game(self, name):
        balance = self.db_connection.get_user_balance(name)

        if balance is None or balance <= 0:
            # Losowe saldo od 0 do 5000
            balance = round(random.uniform(0, 5000), 0)
            self.db_connection.update_user_balance(name, balance)
            print(color.green(f"Przydzielono losowe saldo: {balance:.2f} PLN"))
        else:
            print(color.green(f"Twoje saldo wynosi: {balance:.2f} PLN"))

        player = Player(name, balance)

        while True:
            choice = self.choose_game()
            if choice == '1':
                game = Roulette(player)
            elif choice == '2':
                game = OneArmedBandit(player)
            elif choice == '3':
                game = BlackJack(player)
            elif choice == '4':
                self.db_connection.show_top()
                continue
            elif choice == '5':
                print(color.yellow("Dziękujemy za grę!"))
                break
            else:
                print(color.red("Nieprawidłowy wybór, spróbuj ponownie."))
                continue

            game.play()
            print(color.green(f"Twoje saldo: {player.balance} PLN"))
            self.db_connection.update_user_balance(name, player.balance)

            continue_game = input(color.yellow("Zostań w kasynie (k), wyjdź z aplikacji (x): ")).lower()
            if continue_game != 'k':
                print(color.yellow("Dziękujemy za grę!"))
                break
