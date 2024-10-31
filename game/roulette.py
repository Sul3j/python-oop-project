from game.casinoGame import CasinoGame
import random
import colors.colors as text_color

class Roulette(CasinoGame):
    def play(self):
        while True:
            try:
                rate = float(input(text_color.yellow("Podaj kwotę stawki: ")))
                self.check_balance(rate)
                break
            except ValueError as e:
                print(text_color.red(f"Błąd: {e}"))

        number = random.randint(1, 36)
        color = 'czerwony' if number % 2 == 0 else 'czarny' if number != 0 else 'zielony'

        choice = input(text_color.yellow("Na jaką liczbę lub kolor stawiasz? (np. 1, czerwony): "))
        print(text_color.red(f"Wylosowało: {number} ({color})"))

        if choice.isdigit() and int(choice) == number:
            wins = rate * 36
            self.player.add_wins(wins)
            print(text_color.green(f"Wygrałeś {wins} PLN!"))
        elif choice.lower() == color:
            wins = rate * 2
            self.player.add_wins(wins)
            print(text_color.green(f"Wygrałeś {wins} PLN!"))
        else:
            self.player.substract_rate(rate)
            print(text_color.red("Przegrałeś"))
