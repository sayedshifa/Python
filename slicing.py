import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
#access array elements using slicing
#array[start:end:step]

print(array[0:4:2])
print('-----')
print(array[::2])
print('-----')
print(array[::-2])
print('-----')
print(array[:,0])
print('-----')
print(array[:,-2])
print('-----')
print(array[:,0:3])
print('-----')
print(array[:,1:4])
print('-----')
print(array[:,::5])
print('-----')
print(array[:,::-2])
print('-----')
print(array[0:2,1:3])
print('-----')
print(array[0:2,2:4])
print('-----')
print(array[2:,2:])

