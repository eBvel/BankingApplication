from BankAccount import BankAccount


bank_account = BankAccount(100000.00)
print(bank_account.get_balance)
print(bank_account.deposit(3000.00))
print(bank_account.get_balance)
print(bank_account.withdraw(1500.00))
print(bank_account.get_balance)