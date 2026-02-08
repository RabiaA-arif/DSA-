# Inharence 
class Vechile:
    def __init__(self,brand,model,name):
        self.brand=brand
        self.name=name
        self.model=model
        
    def start(self):
        print("vechile starting")
        
    def stop(self):
        print("vechile is stop")
        
class Car(Vechile):
    def __init__(self,brand,model,name,price,number_of_wheels):
        super().__init__(brand,model,name)
        self.price=price
        self.wheels=number_of_wheels
        
class Bike(Vechile):
    def __init__(self,brand,model,name,engine_pp,color):
        super().__init__(brand,model,name)
        self.engine=engine_pp
        self.colr=color
        


car=Car("X","2022","ulto",200000000,"white")
print(car.__dict__)
bike=Bike("CD","2019","honda","1000cc","black")
print(bike.__dict__)
