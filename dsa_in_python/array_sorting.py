import array
arr=array.array('i',[0,1,2,2,3,33,41,4,5,21,6,7,8])
even_array=array.array('i',[])
odd_array=array.array('i',[])
sort_arr=array.array('i',[])
for i in range(len(arr)):
  if arr[i]%2==0:
    even_array.append(arr[i])
    
  else:
    odd_array.append(arr[i])
  
for j in range(len(even_array)):
  
  sort_arr.append(even_array[j])
  
  sort_arr.append(odd_array[j])
  
  
print(even_array,"even array")
print(odd_array, "odd array")
print(sort_arr,"sorted array according to even odd index")

