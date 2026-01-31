class Dog:
    def __init__(self,name,breed,owner):# init class run only once when we create instance of class
        self.name=name
        self.breed=breed
        self.owner=owner
    def bark(self):  # self is used for accessing variable inside the class 
        print("today dog sit aside of me")
        
        
        
        
class owner():
    def __init__(self,name,address,contact):
        self.name_person=name
        self.address=address
        self.contact=contact
      
        
# owner1=owner("rabia","uk","463")
# dog1=Dog("pokkis","noting",owner1)
# print(owner1.name_person)
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

# owner2=owner("tayyaba","uk","923")

# dog2=Dog("roger","nippi",owner2)
# print(dog2.name)
# print(dog2.breed)
# # dog2.bark()



class Person:
    def __init__(self, name, age):
        self.age=age
        self.name=name
        
        
    def greet(self):
        print(f"Hi i am {self.name} and {self.age}  year old")
        
    
    
person1=Person("Rabia Arif ","20")
person1.greet()

person2=Person("Tayyaba",20)
person2.greet()

class User:
    def __init__(self,username,email,password):
        self.username=username
        self.__email=email
        self.password=password
        
        
    def welcom_user(self,user):
        print(f"dear {user.username} welcome in our code space and here is your  email {user.__email} and password {user.password}")
        
    def clean_email(self):
        return self.__email.lower().strip()
    
user1=User("rabia arif","rabiaarif@gmail.com","arif123")
user2=User("Tayyaba","   taYyaba@gmail.com","tayyaba11")
user1.welcom_user(user2)
print(user2.__email)
print(user2.clean_email())
