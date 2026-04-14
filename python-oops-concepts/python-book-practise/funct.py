a=int('77')
print(type(a))
# b=int('hello') error accur : valueError int cant convert alphabetical string into integer
# QUESTION : why int function convert number string into integer but not character ?
b=int(-2.33)
print(b)
c=int(3.444)
print(c)

e=str(45)
print(type(e))

import math
# print(math)

radian=0.7
height=math.sin(radian)
degree=45
radian=degree/180.0 * math.pi
print(math.sin(radian))

print(math.sqrt(2)/2.0)

def print_name():
    print("hello i am rabia here ")
    
    
def repeat_name():
   print_name()
   print_name()
   
   
repeat_name()
def print_twice(x):
    print(x)
    print(x)
# variable and parameter are local :when we create veriable inside the function it will only access inside the function 
# know as local veriable
def cat_name(cat1,cat2):
    total_cat=cat1 +cat2
    print_twice(total_cat)
    
ct="jerry"
ct1="blurry black"

obj=cat_name(ct,ct1)


# TASK 
def right_justify(s):
    print( " " * 70  + s)
    print(len(s))
    
right_justify('rabia')


    
def do_twice(f,f1):
    f()
    f()
    print(f1)
    
    
def print_spam():
    print('spam')
    
do_twice(print_spam,'Spam')