#  Addition magic method
#  E-commerce cart system
class Cart:
    def __init__(self,items,total_price):
        self.items=items
        self.total_price=total_price
        
    def __add__(self,other):
        if not isinstance(other,Cart):
            return NotImplemented
        
        total_items=self.items + other.items
        total_price=self.total_price + other.total_price
        
        return Cart(total_items ,total_price)
    
    def __str__(self):
        return f"Products{self.items} total Price :{self.total_price}"
    
cart1=Cart(["pen"],200)
cart2=Cart(["pencils"],100)

        
cart=cart1 + cart2 
print(cart)    

# time management 

class Duration:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
        
    def __add__(self,other):
        if isinstance(other,Cart):
            return NotImplemented
        
        total_hour=self.minutes/60
        
        