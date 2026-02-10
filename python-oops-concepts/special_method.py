class Person:
    def __new__(self ,name,age):
        self.name=name
        self.age=age
        instance=super().__new__(self)
        return instance
    
        
    def display(self):
        return type(f"user name is:{self.name} and user age is:{self.age}")
    
    def __str__(self):
        return type(f"name:{self.name} age :{self.age}")
    
    
    def __repr__(self):
        return type(f"name:{self.name} age :{self.age}")
        
        
user=Person("john",22)
print(user.display())
print(user.__str__())
print(user.__repr__())



# class Person:
#     def __init__(self ,name,age):
#         self.name=name
#         self.age=age
#         # return self.name,self.age
        
#     def display(self,name,age):
#         self.name=name
#         self.age=age
#         return (f"user name is:{self.name} and user age is:{self.age}")
    
    
        
# user=Person("rabia",22)
# # print(user)
# # user.display()
# # Person.display()
# print(user.display("tayyaba",22))


#  banking transaction 

class Transaction:
    def __new__(self,amount,type,transaction_id):
        self.amount=amount
        self.type=type
        self.transaction_id=transaction_id
        instance=super().__new__(self)
        return instance
    
    def __str__(self):
        print("Your Transaction is succefully done")
        return f"{self.type} :{self.amount}$"
    
    def __repr__(self):
        print("Developer side logs of transactions")
        return f"transaction (id={self.transaction_id} , type ={self.type},amount ={self.amount})"
    
    
transfer1=Transaction(2000,"Credited","23ai01")
# print(transfer1.__str__())
print(transfer1.__repr__())



#  product inventry -Ecommerce 

class Products:
    def __new__(self,name,sku,price):
        self.name=name
        self.sku=sku
        self.price=price
        instance=super().__new__(self)
        return instance
    
    def __repr__(self):
        # print("log of inventry management")
        return f"Product(name={self.name},sku = {self.sku},price ={self.price})"
    
products=[
    Products("keyboard","M11",2000),
    Products("mouse","M20",1000),
    Products("book","b123",2000)
]
print(products)

#  2D points
class Points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        print("points of co-ordinates")
        return (self.x,self.y)
    
    def __repr__(self):
        # print("dev logs")
        return f"Points({self.x},{self.y})"
    
    
p1=Points(2,4)
print(p1.__str__())
print(p1.__repr__())

print(repr(p1))

p2=eval(repr(p1))
