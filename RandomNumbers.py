import numpy as np

rng=np.random.default_rng(seed=1) #seed reproduces same random numbers

print("-----random-----")
print(rng.integers(low=1,high=101,size=(3,2)))
print('---------random floats--------')
np.random.seed(1) #seed reproduces same random numbers
print(np.random.uniform(low=-1,high=1,size=(3,2)))

print('-----shuffle-----')
rng=np.random.default_rng()
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

rng=np.random.default_rng()
fruits=np.array(['apple','banana','cherry','date','elderberry'])
fruits=rng.choice(fruits,size=(3,3))
print(fruits)