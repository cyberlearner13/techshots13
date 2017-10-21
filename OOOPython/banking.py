from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount = {}
    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name,initialDeposit]
        print("Account was created successfully. Your account number is ",self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication successful")
                self.accountNumber = accountNumber # to refer to this number for further calculation such as dep,with,check in account
                return True
            else:
                print("Authentication Failed")
                return False

    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawlAmount
            print("Withdrawl was successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()

    def displayBalance(self):
        print("Available balance: ",self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = float(input())
        savingsAccount.createAccount(name,deposit)
    elif userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter the account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter a withdrawl amount")
                    withdrawlAmount = float(input())
                    savingsAccount.withdraw(withdrawlAmount)
                elif userChoice is 2:
                    print("Enter an amount to be deposited")
                    depositAmount = float(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
        else:
             pass
    elif userChoice is 3:
         quit()
