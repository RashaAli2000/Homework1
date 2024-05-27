class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.balance
    def prent(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.rate = rate
    def apply_interest(self):
        if self.rate > 0:
            self.balance += self.balance * self.rate
        else:
            print("Interest rate must be positive")
    def prent(self):
        print(f"Interest Rate: {self.rate}")
    def get_balance(self):
        return self.balance

# Create instances and perform operations
account = BankAccount("88888", "rasha")
account.deposit(1000)
account.withdraw(500)
print(account.get_balance())
account.prent()

savings = SavingsAccount("9999", "rasha", 0.0,0.2)
savings.deposit(1000)
savings.apply_interest()
print(savings.get_balance())
savings.prent()
