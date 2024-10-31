from casinoGame import CasinoGame
import random

class Roulette(CasinoGame):
    def play(self):
        while True:
            try:
                rate = float(input("Podaj kwotę stawki: "))
                self.check_balance(rate)
                break
            except ValueError as e:
                print(f"Błąd: {e}")

        number = random.randint(1, 36)
        color = 'czerwony' if number % 2 == 0 else 'czarny' if number != 0 else 'zielony'

        print(f"Wylosowana liczba: {number} ({color})")

        choice = input("Na jaką liczbę lub kolor stawiasz? (np. 1, czerwony): ")

        if choice.isdigit() and int(choice) == number:
            wins = rate * 36
            self.player.add_wins(wins)
            print(f"Wygrałeś {wins} PLN!")
        elif choice.lower() == color:
            wins = rate * 36
            self.player.add_wins(wins)
            print(f"Wygrałeś {wins} PLN!")
        else:
            self.player.substract_rate(rate)
            print("Przegrałeś")
