from random import choice
from database.db import Database
from game.blackJack import BlackJack
from game.oneArmedBandit import OneArmedBandit
from game.player import Player
from game.roulette import Roulette

class Casino:
    def __init__(self):
        self.connection = Database()
        self.games = {
            '1': 'Ruletka',
            '2': 'Jednoręki Bandyta',
            '3': 'Blackjack',
        }

    def choose_game(self):
        print("Wybierz grę: ")
        for key, value in self.games.items():
            print(f"{key}: {value}")
        print('4: Wyświetl TOP 100 graczy')
        print('5: Wyjdź z gry')
        choice = input("Podaj numer gry: ")
        return choice

    def launch_game(self, name):
        balance = float(input("Podaj początkowe saldo: "))
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
                self.connection.show_top()
                continue
            elif choice == '5':
                print("Dziękujemy za grę!")
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
                continue

            game.play()
            print(f"Twoje saldo: {player.balance} PLN")
            self.connection.add_player(name, player.balance)

            continue_game = input("Czy chcesz zmienić grę? (tak/nie): ").lower()
            if continue_game != 'tak':
                print("Dziękujemy za grę!")
                break
