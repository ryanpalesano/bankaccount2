class Bankaccount:
    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        print(self.balance)
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= (self.balance - amount)
            return self
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

life_savings = Bankaccount(10, 2000)
checking = Bankaccount(3, 100000)
life_savings.deposit(500).deposit(250).deposit(350).withdraw(250).yield_interest().display_account_info()

life_savings.deposit(500)
checking.deposit(500)

checking.deposit(1000).deposit(5000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

