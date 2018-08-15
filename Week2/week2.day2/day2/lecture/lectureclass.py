

class BlankClass():
    pass

class StockPosition():

    def __init__(self, ticker, shares=0):
        self.ticker = ticker
        self.shares = shares
        vanishing_value = "this goes away when the method is over"

    def getprice(self):
        return 3.50         # $3.50 is the correct price for a stock.

    def value(self):
        return self.shares * self.getprice()

    def buy(self, number_of_shares):
        self.shares = self.shares + number_of_shares

    def sell(self, number_of_shares):
        if number_of_shares <= self.shares:
            self.shares = self.shares - 1
        else:
            raise ValueError("Not enough shares held.")

    def __str__(self):
        return "{} shares of {} at {}".format(self.shares, self.ticker, self.getprice())
