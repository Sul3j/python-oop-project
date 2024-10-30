class CasinoGame:
    def __init__(self, player):
        self.player = player

    def play(self):
        raise NotImplementedError("Metoda graj musi być zaimplementowana w podklasie")

    def check_balance(self, balance):
        if not isinstance(balance, (int, float)) or balance <= 0:
            raise ValueError("Stawka musi byś liczbą dodatnią.")
        if balance > self.player.balance:
            raise ValueError("Niewystarczające środki na koncie.")
        return True
