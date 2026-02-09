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