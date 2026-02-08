# polymorphisim

class Vechile:
    def __init__(self ,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def start(self):
        print("vechile is starting")
        
    def stop(self):
        print("vechile is stop")
        
class Car(Vechile):
    def __init__(self,brand,model,year,number_door):
        super().__init__(brand,model,year)
        self.number_door=number_door
        
    # def start_car(self):
    #     print("start the vechile ")
        
    # def stop_car(self):
    #     print("stop the vechile")
        
class Motorcycle(Vechile):
    def __init__(self,brand,model,year,color):
        super().__init__(brand,model,year)
        self.color=color
        
    def start(self):
        print("motorcycle is start")
        
    def stop(self):
        print("stop the motor bike")
        

vechiles=[
    Car("tesla","2020","2222","2"),
    Motorcycle("CD","black","2019","red")
]

for vechile in vechiles:
    if isinstance(vechile ,Vechile):
        print(f"inpecting {vechile.brand} {vechile.model} {vechile.year} ({type(vechile).__name__})")
        vechile.start()
        vechile.stop()
    else:
        raise Exception("object is not valid vechile")
# loop through the list of vechile and inspect them

# for vechl in vechile:
#     if isinstance(vechile,Car):
#         print(f"inspection {vechile.brand} {vechile.model} {vechile.year} ({type(vechile).__name__})")
#         vechile.start_car()
#         vechile.stop_car()
#     elif isinstance(vechile ,Motorcycle):
#         print(f" inspecting {vechile.brand} {vechile.model} {vechile.year} ({type(vechile).__name__})")
#         vechile.start_bike()
#         vechile.stop_bike()
#     else:
#         raise Exception(" object is not found")