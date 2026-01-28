class Dog:
    def __init__(self,name,breed,owner):# init class run only once when we create instance of class
        self.name=name
        self.breed=breed
        self.owner=owner
    def bark(self):  # self is used for accessing variable inside the class 
        print("today dog sit aside of me")
        
        
        
        
class owner():
    def __initi__(self,name,address,contact):
        self.name_person=name
        self.address=address
        self.contact=contact
      
        
owner1=owner("rabia","uk","463")
dog1=Dog("pokkis","noting",owner1)
print(dog1.owner1.name_person)
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

# owner2=owner("tayyaba","uk","923")

# dog2=Dog("roger","nippi",owner2)
# print(dog2.name)
# print(dog2.breed)
# dog2.bark()