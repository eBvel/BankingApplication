class BankAccount:

    def __init__(self, value: float):
        self.__balance = value

    def deposit(self, value: float) -> str:
        if value > 0:
            self.__balance += value
            return "Пополнение средст выполнено успешно!"
        else:
            return "Ошибка: сумма депозита меньше или равна нуля!"

    def withdraw(self, value: float) -> str:
        if value < 0:
            return "Ошибка: сумма для снятия средств меньше или равна нулю!"

        if self.__balance - value >= 0:
            self.__balance -= value
            return "Снятие средств выполнено успешно!"
        else:
            return "Ошибка: на вашем балансе недостаточно средств для снятия!"

    @property
    def get_balance(self) -> float:
        return self.__balance

    def _set_balance(self, value: float):
        self.__balance = value

    def __del_balance(self):
        del self.__balance

    def __getattr__(self, item: object) -> str:
        return f"Attribute {item} not found."
