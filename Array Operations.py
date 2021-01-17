import numpy as np
import array

a=array.array('i',[1,2,3,4,5])

#traversing
print([i for i in a])

#slicing
print(a[2:5])

#indexing
print(a[3])                         

#updation
a[0]=9

#appending
a.append(10)
print(a)

#Insertion                  
a.insert(0,9)
print(a)

#Deletion
a.remove(3)
print(a)

#reversing
a.reverse()
print(a)
print("\n")




#np.insert(array1,2,9,axis=None)     #insertion in numpy

array1 = np.array([10,20,30,40,50])
array2=np.array([10, 20])

#1D concatenation
print(np.append(array1,array2))

arr1 = np.arange(1,10).reshape(3,3) 
arr2 = np.arange(10,19).reshape(3,3)

#2D concatenation
print(np.concatenate((arr1,arr2),axis=1))









