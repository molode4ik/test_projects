import datetime


class Transaction:
    def __init__(self, transaction_type, amount):
        self._timestamp = datetime.datetime.now()
        self._transaction_type = transaction_type
        self._amount = amount

    def get_details(self):
        return {
            "timestamp": self._timestamp,
            "transaction_type": self._transaction_type,
            "amount": self._amount
        }


class AccountStrategy:
    def create_account(self, account, name_account):
        pass

    def take_off(self, account, name_account, monetary_quantity):
        pass

    def contribute(self, account, name_account, monetary_quantity):
        pass

    def add_transaction(self, account, transaction_type, amount):
        transaction = Transaction(transaction_type, amount)
        account._transactions.append(transaction)


class DefaultStrategy(AccountStrategy):
    def create_account(self, account, name_account):
        if name_account not in account._list_account:
            account._list_account[name_account] = 0
            return "создание прошло успешно"
        else:
            return "такой аккаунт уже есть"

    def take_off(self, account, name_account, monetary_quantity):
        account._list_account[name_account] = account._list_account[name_account] - monetary_quantity
        self.add_transaction(account, name_account, "take_off", monetary_quantity)

    def contribute(self, account, name_account, monetary_quantity):
        account._list_account[name_account] = account._list_account[name_account] + monetary_quantity
        self.add_transaction(account, name_account, "contribute", monetary_quantity)


class SavingsAccountStrategy(AccountStrategy):
    def take_off(self, account, name_account, monetary_quantity):
        account._list_account[name_account] = account._list_account[name_account] - monetary_quantity
        self.add_transaction(account, name_account, "take_off", monetary_quantity)

    def contribute(self, account, name_account, monetary_quantity):
        account._list_account[name_account] = account._list_account[name_account] + monetary_quantity
        self.add_transaction(account, name_account, "contribute", monetary_quantity)

    def calculate_interest(self, account, name_account):
        interest = account._list_account[name_account] * account._interest_rate
        account.contribute(name_account, interest)
        self.add_transaction(account, name_account, "interest", interest)


class CreditAccountStrategy(AccountStrategy):
    def take_off(self, account, name_account, monetary_quantity):
        if monetary_quantity <= (account._credit_limit + account._list_account[name_account]):
            account._list_account[name_account] = account._list_account[name_account] - monetary_quantity
            self.add_transaction(account, name_account, "take_off", monetary_quantity)
        else:
            print("Превышен кредитный лимит")

    def contribute(self, account, name_account, monetary_quantity):
        account._list_account[name_account] = account._list_account[name_account] + monetary_quantity
        self.add_transaction(account, name_account, "contribute", monetary_quantity)

    def calculate_interest(self, account, name_account):
        if account._list_account[name_account] < 0:
            interest = abs(account._list_account[name_account]) * account._interest_rate
            account.contribute(name_account, interest)
            self.add_transaction(account, name_account, "interest", interest)


class Client:
    def __init__(self, id_user, strategy=None):
        self._id_user = id_user
        self._accounts = {}
        self._strategy = strategy or DefaultStrategy()
        print(self._strategy)

    def create_account(self, account_type, name_account):
        account = self._accounts.get(account_type)
        if account:
            self._strategy.create_account(account, name_account)

    def take_off(self, account_type, name_account, monetary_quantity):
        account = self._accounts.get(account_type)
        if account:
            self._strategy.take_off(account, name_account, monetary_quantity)

    def contribute(self, account_type, name_account, monetary_quantity):
        account = self._accounts.get(account_type)
        if account:
            self._strategy.contribute(account, name_account, monetary_quantity)

    def calculate_interest(self, account_type, name_account):
        account = self._accounts.get(account_type)
        if account and isinstance(self._strategy, SavingsAccountStrategy):
            self._strategy.calculate_interest(account, name_account)

    def get_account_balance(self, account_type, name_account):
        account = self._accounts.get(account_type)
        if account:
            return account.get_account(name_account)
        else:
            return "Указан неверный тип"

    def set_strategy(self, strategy):
        self._strategy = strategy


if __name__ == '__main__':
    client = Client(id_user=1,)
    client.create_account("savings", "SavingsAccount")
    client.take_off("savings", "SavingsAccount", 100)
    client.calculate_interest("savings", "SavingsAccount")
    client.set_strategy(CreditAccountStrategy())
    client.create_account("credit", "CreditAccount")
    client.take_off("credit", "CreditAccount", 50)
    client.calculate_interest("credit", "CreditAccount")
