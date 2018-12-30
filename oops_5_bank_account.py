class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}  \nAccount balance: {self.balance}"

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return "Funds Unavailable"
        else:
            self.balance = self.balance - withdraw
            return self.balance


acct1 = Account("Jose", 100)
print(acct1)

print(acct1.owner)
print(acct1.balance)

print(acct1.deposit(20))
print(acct1.deposit(60))
print(acct1.deposit(100))

print(acct1.withdraw(50))
print(acct1.withdraw(240))






