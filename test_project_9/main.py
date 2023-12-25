from datetime import datetime


class Transaction:
    def __init__(self, amount, transaction_type):
        self._amount = amount
        self.date = datetime.now()
        self.type = transaction_type

    def get_amount(self):
        return self._amount


class Account:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self._balance = balance
        self._transactions = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction(amount, "DEPOSIT"))
            print(f"Deposit of {amount} successfully made.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(Transaction(amount, "WITHDRAW"))
            print(f"Withdrawal of {amount} successfully made.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self._balance}")

    def get_transaction_history(self):
        for transaction in self._transactions:
            print(
                f"Date: {transaction.date}, Type: {transaction.type}, Amount: {transaction.get_amount()}"
            )


class SavingsAccount(Account):
    def __init__(self, interest_rate, balance=0):
        super().__init__("Savings", balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self._balance * (self.interest_rate / 100)
        self.deposit(interest_amount)
        print(f"Interest of {interest_amount} added to the account.")


class CreditAccount(Account):
    def __init__(self, credit_limit, interest_rate, balance=0):
        super().__init__("Credit", balance)
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= -self.credit_limit:
            self._balance -= amount
            self._transactions.append(Transaction(amount, "WITHDRAW"))
            print(f"Withdrawal of {amount} successfully made.")
        else:
            print("Invalid withdrawal amount or exceeding credit limit.")


#Текущий счет
client1 = Account("Current")
client1.deposit(1000)
# client1.withdraw(500)
# client1.check_balance()
#
# # Создание сберегательного счета
# savings_account = SavingsAccount(interest_rate=5)
# savings_account.deposit(1000)
# savings_account.add_interest()
# savings_account.check_balance()

# Создание кредитного счета
credit_account = CreditAccount(credit_limit=10000, interest_rate=10)
credit_account.withdraw(800)

credit_account.withdraw(500)
credit_account.check_balance()
credit_account.get_transaction_history()
