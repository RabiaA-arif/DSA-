# import array
# # we dont need to write array every where jus rught below line
# # from array import *  
# # alias name of array
# # import array as arr
# value=array.array('i',[1,2,3,4,5,6,7,8,9,10])
# # value=array.array('d',[1,2,3,4,5.0])
# # value=array('u',['w','ed','yes'])
# # print(value)
# for i in range(0,5):
#     print(value[i],end=" ")
# print('\n')
# for i in range(len(value)):
#     print(value[i],end=" ")
# print('\n')
# for j in value:
#     print(j,end=" ")
    
# print('\n')
# print(value.typecode)

# value.reverse()
# for i in value:
#     print(i,end=" ")
# print('\n')
# value.insert(2,22)
# value.append(200)
# value[4]=90
# for i in value:
#     print(i,end=" ")
# print('\n')

# copy_array=array.array(value.typecode ,(x for x in value))
# for h in copy_array:
#     print(h,end=" ")
# print('\n')
# # copy_array.pop(4)
# copy_array.pop()
# for i in range(len(copy_array)):
#     print(copy_array[i],end=" ")
# print('\n')    
# copy_array.remove(3)
# for i in range(len(copy_array)):
#     print(copy_array[i],end=" ")
    
# arr=array.array('i',[1,2,3,4,5,6,7,8])
# slc=arr[2:5]
# slc=arr[2:-2]
# slc=arr[::]
# for i in slc:
#     print(i,end=' ')
    
# arr=array.array('i',[])

# n=int(input("Enter the number"))
# for i in range(0,n):
#     arr.append(int(input("input next number")))
    
# for j in arr:
#     print(j,end=" ")
    
# arr=array.array('i',[12,1,3,4,55,33,445,55])
# ind=arr.index(445)
# print(ind)
# for i in arr:
#     print(i,end=" ")
# print('\n')
# print(ind)

from numpy import *
# val=array([1,2,3,4,5])
# arranf number with mathematical progression work of linspace first number for starting point number and second one is for ending point and last is partion of number
# val=linspace(10,30,6)
# in arange last number is add to previous one
# val=arange(5,50,3) 
#  logspace number point in the form of 10 raised to power or e raised to power e means 10
# val=logspace(20,40,3)
# val=zeros(8)
# val=ones(3)
# val=full(8,3)
# for x in val:
#     print(x,end=" ")
    
zero=array(10)
print(zero)
one_D=array([1,2,3,4,5])
print(one_D)
#  two dimensional array is collection of one Dimensional array
two_D=array([[1,2,3],[1,2,3]])
print(two_D)
three_D=array([[[1,2,3],[1,2,3]],[[4,5,6],[4,5,6]]])

print(three_D)