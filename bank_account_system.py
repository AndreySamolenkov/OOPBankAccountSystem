# Bank Account System: Develop a Python class for a bank account that has methods for deposit, withdrawal, and display of the balance.


class BankAccount:

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def __str__(self):
    return f"Account Holder Name: {self.name}.\n"

  def withdraw(self, amount):
    if amount > self.balance:
      return "Insufficient balance\n"
    self.balance -= amount
    return f'You withdrew ${amount}. The remaining balance is ${self.balance}.\n'

  def transfer(self, amount, recipient):
    if amount > self.balance:
      return "Insufficient balance\n"
    self.balance -= amount
    recipient.balance += amount
    return f'${amount} has been transferred to {recipient.name}. Your new balance is ${self.balance}.\n'

  def display_balance(self):
    return f'The balance in your account is ${self.balance}.\n'


account_holder1 = BankAccount('Bob', 1200)
print(account_holder1)
print(account_holder1.display_balance())
withdraw_message = account_holder1.withdraw(300)
print(withdraw_message)
print(account_holder1.display_balance())

account_holder2 = BankAccount('Jack', 2400)
print(account_holder2)
print(account_holder2.display_balance())
withdraw_message = account_holder2.withdraw(500)
print(withdraw_message)
print(account_holder2.display_balance())

print(account_holder1.transfer(400, account_holder2))