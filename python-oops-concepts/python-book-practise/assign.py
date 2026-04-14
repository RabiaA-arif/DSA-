# assignments statement 
message="welcome to my world"  # herewe create variable and assign string value
# question : is while creating veriable of different types it store different variable value in different format
num=1223
flot=2.33
# use lowercase value for veriable naming
# it allow to use upercase,number but convention is to use lowercase name
# !important  :variable name cant be start with number

##################      wrong naming convention #####################
# 1num = 44 error 
# print(1num)

# invalid decimal literal : accur error when veriable name does  not follow the rule while defining the name of veriable 

# @age= =20  
# print(@age)
# invalid syntax error :Syntax error occurs when the Python interpreter wants to understand a
# written variable name, but it can't match the views which they have written
# in their interpreter and which we write our code. If they both can't match,
# it gives us a syntax error. 

# class="hello"
# Class is equal to hello also shows the syntax error
# because Python uses some built-in keywords that
# we can't use in creating variable names like class, 
# false, ye, is, if, and elf. These all are keywords in Python,
# so we can't use them directly in variable names. 

import keyword
print(keyword.kwlist) #list the keyword of python

# EXPRESSION : is the combination of value + veriable + assignment operator
name="rohial"
# STATEMENT : is the unit of code which have some effect

miles=2.43
print(miles*1.3)

4
x=1
print(x+1)
# print(x=1) type error :when operation is applied on inaproprite of function

# ODER OF OPERATION  : python follow oder for mathematics operation PEMDAS(paranthesis,exponents,multiply,divide,add,subtract)
# STRING OPERATION : we cant perform operation on string except +(concatenation) and * (it perform repition on string)
str1="hello"
str2="world"
strr=str1 +str2
print(strr)
print(strr *5)


# 42=n error
x=y=2
print(x)
print(y)

greet="Hello welcome !";
# greet="Hello welcome !". syntax error 
# print(xy) NameError
# TASK 1
r=5
pie=3.14
volume_radius=4/3*(pie*(r**3))
print(volume_radius)
print(r ** 3)
  
  
# TASK 2
cover_price=24.95
discount=40/100
first_shiping_cost=3
each_shiping_cost=75/100
total_copy_sell=60
total_shipping_cost=first_shiping_cost +((total_copy_sell-1)*each_shiping_cost)
wholesale_price_per=cover_price *(1-discount) + total_shipping_cost 

total_wholsale_price=wholesale_price_per *total_copy_sell
print(f"price of per book : {wholesale_price_per}")
print(f"Total wholesale price is : {total_wholsale_price}")


# TASK 3
initial_time=6.52
run_time=8.15
tempo_time=3 *7.12
total_time=run_time + tempo_time
return_time=initial_time + total_time
print(f"you return back : {return_time} minutes")


