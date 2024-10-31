import colors.colors as color

class CasinoGame:
    def __init__(self, player):
        self.player = player

    def play(self):
        raise NotImplementedError(color.red("Metoda graj musi być zaimplementowana w podklasie"))

    def check_balance(self, balance):
        if not isinstance(balance, (int, float)) or balance <= 0:
            raise ValueError(color.red("Stawka musi byś liczbą dodatnią."))
        if balance > self.player.balance:
            raise ValueError(color.red("Niewystarczające środki na koncie."))
        return True
