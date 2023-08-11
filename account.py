class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.__account_balance
    
    def get_name(self):
        return self.__account_name

# Example usage
account_one = Account('John')
print(f"Account name: {account_one.get_name()}")
print(f"Initial balance: {account_one.get_balance()}")

if account_one.deposit(100):
    print("Deposit successful")
else:
    print("Deposit failed")

if account_one.withdraw(50):
    print("Withdrawal successful")
else:
    print("Withdrawal failed")

print(f"Current balance: {account_one.get_balance()}")
