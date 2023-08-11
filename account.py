class Account:
    """
    A class representing a bank account.
    
    Attributes:
        name (str): The account holder's name.
        balance (float): The current account balance.
    """
    
    def __init__(self, name: str) -> None:
        """
        Initialize a new Account instance.

        Args:
            name (str): The account holder's name.
        """
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        """
        Get the current account balance.

        Returns:
            float: The account balance.
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Get the account holder's name.

        Returns:
            str: The account holder's name.
        """
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
