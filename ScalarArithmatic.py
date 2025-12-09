import numpy as np

array=np.array([1,2,3,4,5])

print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**2)
print(array%2)

print('------------------')
#Vectorized operations
array2=np.array([1.01,2.5,3.99])
print(np.sqrt(array2))
print(np.round(array2))
print(np.ceil(array2))
print(np.floor(array2))
print(np.pi)

#Exercise:
radii=np.array([1,2,3])
print(np.pi*radii**2)

#Element wise Arithmetic
array3=np.array([1,2,3])
array4=np.array([4,5,6])
print(array3+array4)
print(array4-array3)
print(array3*array4)
print(array3/array4)
print(array3**array4)

#Comparison Operators
scores=np.array([91,55,100,73,82,64])
print(scores==100)
print(scores>=60)
print(scores<80)
scores[scores<60]=0
print(scores)




