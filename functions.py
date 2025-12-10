import numpy as np
#array creation
a=np.array([1,2,3,4])
print(a)

#array of zeroes
np.zeros(5)
np.zeros((3,4))

#array of ones
np.ones(5)
np.ones((2,3))

#fixed value
np.full((2,3),7)

#empty
np.empty((2,3))

#arange:range with step
np.arange(1,10,2) #1,3,5,7,9

#linspace: eveny spaced numbers over a specified interval
np.linspace(0,1,5) #0. ,0.25,0.5,0.75,1

#identity matrix
np.eye(3)

#random values
np.random.random((2,3))
np.random.randint(1,10,size=5)
np.random.randn(5)
np.random.choice([1,2,3,4],size=3)

#imp attr.
a.ndim #number of dimensions
a.shape #shape of array (rows,cols)
a.size #total number of elements
a.dtype #data type of elements
a.itemsize #size in bytes of each element

#indexing and slicing
b=np.array([10,20,30])
b[0] #10
b[-1] #30

c=np.array([[1,2,3],
            [4,5,6]])
c[0,1] #2

c[1:4]
c[:3]
c[::2]
c[:2,:2]

#boolean indexing
d=np.array([10,15,20,25,30])
d[d>20] #array([25,30])
#fancy indexing
d[[0,2,4]] #array([10,20,30])
d[[0,1],[1,2]] #array([15,30])

#reshaping
e=np.arrange(6)
e.reshape((2,3)) #array([[0,1,2],[3,4,5]])

#ravel:flatten
e.ravel() #array([0,1,2,3,4,5])
#transpose
e.T #array([[0,3],[1,4],[2,5]])
#stacking
f=np.array([1,2,3])
g=np.array([4,5,6])
np.vstack((f,g)) #vertical stack
np.hstack((f,g)) #horizontal stack

#concatenation
np.concatenate((f,g)) #array([1,2,3,4,5,6])
np.concatenate((f,g),axis=0) #array([1,2,3,4,5,6])

#splitting
h=np.array([1,2,3,4,5,6])
np.split(h,3) # [array([1,2]), array([3,4]), array([5,6])]
np.array_split(h,4) # [array([1,2]), array([3,4]), array([5]), array([6])]

#aritmatic ufuncs
x=np.array([1,2,3])
y=np.array([4,5,6])
np.add(x,y) #array([5,7,9])
np.subtract(y,x) #array([3,3,3])
np.multiply(x,y) #array([4,10,18])
np.divide(y,x) #array([4.,2.5,2.])
np.power(x,2) #array([1,4,9])
np.mod(y,2) #array([0,1,0])

#trigonometric ufuncs
angles=np.array([0,np.pi/2,np.pi])
np.sin(angles) #array([0.,1.,0.])
np.cos(angles) #array([1.,0.,-1.])
np.tan(angles) #array([0.,inf,0.])
np.arcsin([0,1]) #array([0.,pi/2])

#exponential and logarithmic ufuncs
vals=np.array([1,2,3])
np.exp(vals) #array([2.718,7.389,20.085])
np.log(vals) #array([0.,0.693,1.098])
np.log10(vals) #array([0.,0.301,0.477])
np.log2(vals) #array([0.,1.,1.585])

#rounding ufuncs
vals2=np.array([1.2,2.5,3.7])
np.floor(vals2) #array([1.,2.,3.])
np.ceil(vals2) #array([2.,3.,4.])
np.round(vals2) #array([1.,3.,4.])

#absolute value
np.abs(vals2) #array([1.2,2.5,3.7])

#aggregate functions
data=np.array([[1,2,3],
                [4,5,6]])
np.sum(data) #21
np.mean(data) #3.5
np.std(data) #1.7078
np.var(data) #2.9166
np.min(data) #1
np.max(data) #6
np.argmin(data) #0
np.argmax(data) #5
np.median(data) #3.5

#sorting
np.sort(data)
np.argsort(data)
np.partition(data,2)
np.sort(data,axis=0)

#determinant
np.linalg.det(data)
#inverse
np.linalg.inv(data)
#matrix multiplication
np.dot(data,data.T)
#eigenvalues and eigenvectors
np.linalg.eig(data)
#solving systems of equations
np.linalg.solve(data,vals2)

#broadcasting
m=np.array([1,2,3])
n=2
m+n #array([3,4,5])
m+n[:,np.newaxis] #array([[3],[4],[5]])

#random functions
rng=np.random.default_rng()
rng.random(5) #5 random floats [0.0,1.0)
rng.integers(1,10,size=5) #5 random ints [1,10)
rng.choice([10,20,30,40],size=3) #3 random choices from array

#input/output funcs (read/write)
np.loadtxt('data.txt')
np.genfromtxt('data.csv',delimiter=',')
np.save('array.npy',data)
np.load('array.npy')
np.savetxt('array.txt',data)

