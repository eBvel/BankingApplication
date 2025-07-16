class BankAccount:

    def __init__(self, value: float):
        self.__balance = value

    def deposit(self, value: float) -> str:
        if value > 0:
            self.__balance += value
            return "Deposit to the balance has been made."
        else:
            return "The deposit value is less then minimum value"

    def withdraw(self, value: float) -> str:
        if value > 0:
            self.__balance -= value
            return "Withdraw from the balance has been made."
        else:
            return "The withdraw amount is less then minimum value"

    @property
    def get_balance(self) -> float:
        return self.__balance

    def _set_balance(self, value: float):
        self.__balance = value

    def __del_balance(self):
        del self.__balance

    def __getattr__(self, item: object) -> str:
        return f"Attribute {item} not found."
