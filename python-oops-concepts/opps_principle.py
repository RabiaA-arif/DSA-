#  encapsulation 

# class BadBankAcount:
#     def __init__(self,balance):
#         self.balance=balance
        
        
        
# account=BadBankAcount(0)
# account.balance=-1
# print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance=0.0
        
    @property
    def balance(self):
        return self._balance
    
    
    def deposit(self,amount):
        if amount <=0:
            raise ValueError("Deposit amount must be more than 0")
        else:
            self._balance+=amount
            
            
    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("withdraw amoutn must be positive")
        if amount >= self._balance:
            raise ValueError(" Amount is insufficient ")
        self._balance-=amount
        
        
acount=BankAccount()
print(acount.balance)
acount.deposit(1000.99)
print(acount.balance)
print(acount.withdraw(200))
print(acount.balance)
