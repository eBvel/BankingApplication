from BankAccount import BankAccount


def request_menu_item(menu_operations: dict, account: BankAccount):
    try:
        menu_item = int(input("\nВведите пункт меню: "))
        menu_operations[menu_item](account)
    except ValueError:
        print("Ошибка: введено некорректное значение!")
    except KeyError:
        print("Ошибка: указанный пункт меню отсутствует!")


def request_value(text: str) -> float:
    while True:
        try:
            value = float(input(text))
            if value > 0:
                return value
            print("Ошибка: введено значение менше или равное нулю!")
        except ValueError:
            print("Ошибка: введено не числовое значение!")


def check_balance(account: BankAccount):
    print(f"\nТЕКУЩИЙ БАЛАНС: {account.get_balance}")


def deposit_value(account: BankAccount):
    print("\nПОПОЛНЕНИЕ:")
    value = request_value("Укажите сумму депозита: ")
    print(account.deposit(value))


def withdraw_value(account: BankAccount):
    print("\nСНЯТИЕ:")
    value = request_value("Укажите сумму для снятия: ")
    print(account.withdraw(value))


def complete_program(account: BankAccount = None):
    global at_work
    at_work = False
    print("Программа завершена!")


def menu():
    print("""
    МЕНЮ:
    1) Проверить баланс;
    2) Внести средства;
    3) Снять средства;
    4) Выход.""")


def main():
    menu_operations = {
        1: check_balance,
        2: deposit_value,
        3: withdraw_value,
        4: complete_program
    }
    current_account = BankAccount(0)

    while at_work:
        request_menu_item(menu_operations, current_account)


at_work = True
menu()
main()
