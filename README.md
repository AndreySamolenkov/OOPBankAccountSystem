Bank Account Management System

This is a Python class that implements a basic bank account management system. The class BankAccount has the following methods:

    __init__(self, name, balance): Initializes a bank account with a name and a starting balance.

    withdraw(self, amount): Withdraws a specified amount from the account and returns a message indicating the new balance. If the amount to be withdrawn is greater than the current balance, returns an error message saying "Insufficient balance".

    display_balance(self): Returns a message indicating the current balance of the account.

    transfer(self, amount, recipient): Transfers a specified amount from the current account to another account. Returns a message indicating the transfer amount and the new balance of the current account. If the amount to be transferred is greater than the current balance, returns an error message saying "Insufficient balance".
