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


# create two bank accounts
account1 = BankAccount("Bob", 1000)
account2 = BankAccount("Jack", 500)

# check the balance of account1
print(account1.display_balance())

# withdraw from account1
print(account1.withdraw(100))

# check the balance of account1 again
print(account1.display_balance())

# transfer from account1 to account2
print(account1.transfer(200, account2))

# check the balance of account1 and account2
print(account1.display_balance())
print(account2.display_balance())