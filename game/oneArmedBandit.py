import random
from game.casinoGame import CasinoGame
import colors.colors as color

class OneArmedBandit(CasinoGame):
    def __init__(self, player):
        super().__init__(player)
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💰"]
        self.wins = {
            "🍒🍒🍒": 5,
            "🍋🍋🍋": 10,
            "🍊🍊🍊": 15,
            "🍉🍉🍉": 20,
            "⭐⭐⭐": 50,
            "💰💰💰": 100,
        }

    def play(self):
        while True:
            try:
                rate = float(input(color.yellow("Podaj kwotę stawki: ")))
                self.check_balance(rate)
                break
            except ValueError as e:
                print(color.red(f"Błąd: {e}"))
        results = self.check_result()
        self.calculate_win(results, rate)

    def check_result(self):
        results = [random.choice(self.symbols) for _ in range(3)]
        print(color.yellow(f"Wynik gry: {' '.join(results)}"))
        return ''.join(results)

    def calculate_win(self, results, rate):
        if results in self.wins:
            win = self.wins[results] * rate
            self.player.add_wins(results)
            print(color.green(f"Gratulacje! Wygrałeś {win} PLN!"))
        else:
            self.player.substract_rate(rate)
            print(color.red("Przegrałeś! Spróbuj ponownie."))

