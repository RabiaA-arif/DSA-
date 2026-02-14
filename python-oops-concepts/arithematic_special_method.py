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
        if not isinstance(other,Duration):
            return NotImplemented
        mint=self.minutes + other.minutes
        # print(mint)
        if mint >60:
            hour=mint/60
            # print(hour)
            # print("remaining mint :" ,rem_mint)
            total_hour=self.hours + other.hours + hour
            tot_minute=mint%60
            print("Time Duration is hour : minutes ")
            return f"{int(total_hour)} : {tot_minute}"
        else :
            mnt=self.minutes + other.minutes
            hur=self.hours + other.hours
            print("Time Duration is hour : minutes ")
            return f"{hur} , {mnt}"
    
time2=Duration(2,10)
time1=Duration(0,10)

time=time1 + time2
print(time)
    
    
 ################# specil method forr subtraction #####################
 
class Warehouse:
    def __init__(self,stock):
        self.stock_count=stock
    
    
    def __sub__(self,other):
        if not isinstance(other,Warehouse):
            return NotImplemented
        
        differece=self.stock_count - other.stock_count
        if differece <0:
            raise ValueError("stock value is in minus")
        
        return Warehouse(differece)
    
    def __repr__(self):
        return f"warehouse stock {self.stock_count} "
   
        
    
obj1=Warehouse(10)
obj2=Warehouse(6)
res=obj1 - obj2
print(res)
print(res.stock_count,"stock count")
print(res)



####################### specila method __mul__ practice ###############
