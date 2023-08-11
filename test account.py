import pytest
from account import Account

# Test initialization of Account
def test_account_init():
    account = Account('John')
    assert account.get_name() == 'John'
    assert account.get_balance() == 0.0

# Test deposit method
def test_account_deposit():
    account = Account('Alice')
    
    assert account.deposit(100.0) == True
    assert account.get_balance() == 100.0
    
    assert account.deposit(-50.0) == False  # Negative deposit should fail
    assert account.get_balance() == 100.0  # Balance should remain unchanged
    
    assert account.deposit(0.0) == False  # Zero deposit should fail
    assert account.get_balance() == 100.0  # Balance should remain unchanged

# Test withdraw method
def test_account_withdraw():
    account = Account('Bob')
    account.deposit(200.0)
    
    assert account.withdraw(50.0) == True
    assert account.get_balance() == 150.0
    
    assert account.withdraw(-30.0) == False  # Negative withdrawal should fail
    assert account.get_balance() == 150.0  # Balance should remain unchanged
    
    assert account.withdraw(200.0) == False  # Withdrawal exceeding balance should fail
    assert account.get_balance() == 150.0  # Balance should remain unchanged

if __name__ == '__main__':
    pytest.main()
