class LowBalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance
        
    def __str__(self):
        return f"Balance too low: {self.balance}"
    
def withdraw(balance, amount):
    if amount > balance:
        raise LowBalanceError(balance)
    
    return int(balance) - int(amount)

try:
    print(withdraw("100" ,150))
    
except LowBalanceError as le:
    print(le)
    
except TypeError as te:
    print(te)
    
except Exception as e:
    print(e)
    
    
