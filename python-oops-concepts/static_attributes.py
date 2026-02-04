# static attributes in python

class User:
    user_count=0
    
    
    def __init__(self,user_name,email):
        self.username=user_name
        self.email=email
        User.user_count+=1
        
        
    def display_user(self):
        print(f"welcome {self.usernam} and with yourr email {self.email}")
        
        
user1=User("xinchoa","xian@gmail.com")
user2=User("zon","zon@gmail.com")
print(User.user_count)
print(user1.user_count)
print(user2.user_count)


# static vs instances method  example

class BankAccount:
    MIN_BALANCE=100
    
    def __init__(self,ownr,balance=0):
        self.owner=ownr
        self._balance=balance
        
    def deposit(self,amount):
        if amount >0:
            self._balance+=amount
            print(f"{self.owner} your new balance is {self._balance}")
        else:
            print("deposit amount mut be greater than 10 rs ")
            
    @staticmethod
    def is_valid_interest_rata(rate):
        return 0 <= rate <=5 
    
    
acount=BankAccount("rabia",100)
acount.deposit(500)

print(BankAccount.is_valid_interest_rata(2))
print(BankAccount.is_valid_interest_rata(7))