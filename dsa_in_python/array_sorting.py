import array
# You are given an array `nums` consisting of integers where 
# half of the numbers are even, and the other half are odd.
# Your objective is to rearrange the array such that each 
# even number appears at an even index, and each odd number appears at an odd index.
my_arr=array.array('i',[3,2,4,7])
sort_arr=array.array('i',[])
for i in range(len(my_arr)):
  if i%2==0:
    print(i)
    if my_arr[i]%2==0:
      print(my_arr)
    
    
   
      
        
# for j in sort_arr:
#     print(j,end=" ")