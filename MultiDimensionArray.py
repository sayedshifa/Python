import numpy as np

array=np.array([[['a','b','c','d'],['e','f','g','h'],['i','j','k','l']],
                [['A','B','C','D'],['E','F','G','H'],['I','J','K','L']],
                [['1','2','3','4'],['5','6','7','8'],['9','10','11','12']]])
print(array.ndim)
print(array.shape)
print(array[0][0][0])
print(array[1,2,3])
print('-----')

word=array[0,0,0]+array[1,1,1]+array[2,2,2]

print(word)