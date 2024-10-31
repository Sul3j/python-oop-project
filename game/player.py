import colors.colors as color

class Player:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # chronione saldo

    @property
    def balance(self):
        return self._balance

    # dodwanie środków
    def add_wins(self, amount):
        self._balance += amount

    # odejmowanie określonej stawki
    def substract_rate(self, rate):
        if rate > self._balance:
            raise ValueError(color.red("Niewystarczające środki na koncie."))
        self._balance -= rate