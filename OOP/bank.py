import datetime


class Bank:

    @staticmethod
    def _Current_time(self):
        time = datetime.datetime.now()
        return time

    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__balance = 0
        self.amount = 0
        self.transaction_list = []

    def creation(self, name ,age):
        self.__name = name
        self.__age = age
        if age >= 18:
           print(f"account has been created {self.__name}")
        else:
            print(f"you are not legal you are {self.__age}")

    def show(self):
        print(f" your __name is {self.__name} and you are {self.__age} your __balance is {self.__balance}")

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            self.transaction_list.append((self.__name , amount , Bank._Current_time(self) , "Deposit"))
            self.show()
        else:
            print("enter valid amount")

    def withdraw(self , amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((self.__name , amount , Bank._Current_time(self)  , "Withdrawal"))
            self.show()
        else:
            print("Withdrawal amount exceeds account __balance")

    def showrecipt(self):
        for name,amount,date,transaction_type in self.transaction_list:
            if transaction_type == "Withdrawal":
                amount *= -1
            print(f"Recipt:\n  Name: {name}\n  Amount: {amount} \n  Date: {date}\n  transaction type: {transaction_type}")



account = Bank()
account.creation("hayyan", 18)
account.deposit(20)
account.withdraw(19)
account.showrecipt()