from random import random

from game.casinoGame import CasinoGame

class BlackJack(CasinoGame):
    def __init__(self, player):
        super().__init__(player)
        self.waist = self.create_waist()
        self.dealer_hand = []

    @staticmethod
    def create_waist():
        colors = ['Kier', 'Karo', 'Trefl', 'Pik']
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [(number, color) for color in colors for number in numbers]

    def shuffle(self):
        random.shuffle(self.waist)

    def play(self):
        self.shuffle()
        while True:
            try:
                rate = float(input("Podaj kwotę stawki: "))
                self.check_balance(rate)
                break
            except ValueError as e:
                print(f"Błąd: {e}")

        self.player.hand = []
        self.dealer_hand = []

        # Rozdanie kart
        self.hand_out_cards(2)
        self.dealer_hand_out_cards(2)

        print(f"\nTwoja ręka: {self.player.hand}, suma: {self.calculate_hand_value(self.player.hand)}")
        print(f"Karta krupiera: {self.dealer_hand[0]} oraz jedna zakryta")

        # Tura gracza
        while True:
            action = input("Wybierz akcję (dobierz / passuj): ").lower()
            self.pick_card()
            print(f"Twoja ręka: {self.player.hand}, suma: {self.calculate_hand_value(self.player.hand)}")
            if self.calculate_hand_value(self.player.hand) > 21:
                print("Przegrałeś!")
                self.player.substract_rate(rate)
                return
            elif action == 'passuj':
                break
            else:
                print("Nieprawidłowa akcja!")

        # tura krupiera
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.pick_card_dealer()

        # sprawdzenie wyniku
        self.check_result(rate)

    # rozdanie kart
    def hand_out_cards(self, number_of_cards):
        for _ in range(number_of_cards):
            card = self.waist.pop()
            self.player.hand.append(card)

    # rozdanie kart krupierowi
    def dealer_hand_out_cards(self, number_of_cards):
        for _ in range(number_of_cards):
            card = self.waist.pop()
            self.dealer_hand.append(card)

    # dobieranie karty
    def pick_card(self):
        card = self.waist.pop()
        self.player.hand.append(card)

    # dobieranie ręki krupierowi
    def pick_card_dealer(self):
        card = self.waist.pop()
        self.dealer_hand.append(card)

    # obliczanie wartości ręki
    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card[0] in ['J', 'Q', 'K']:
                value += 10
            elif card[0] == 'A':
                aces += 1
                value += 11
            else:
                value -= 10
                aces -= 1
            return value

    # sprawdzanie wyniku gry
    def check_result(self, rate):
        player_value = self.calculate_hand_value(self.player.hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        print(f"\nTwoja suma: {player_value}, suma krupiera: {dealer_value}")

        if player_value > 21:
            print("Przegrałeś!")
            self.player.substract_rate(rate)
        elif dealer_value > 21 or player_value > dealer_value:
            wins = rate * 2
            self.player.add_wins(wins)
            print(f"Wygrałeś {wins} PLN!")
        elif player_value < dealer_value:
            print("Przegrałeś!")
            self.player.substract_rate(rate)
        else:
            print("Remis! Twoja stawka została zwrócona.")


