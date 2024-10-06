import numpy as np

a = np.array([5,6,9])
print(a)
print("Dimension of a:", a.ndim)
print("Itemsize of a: ", a.itemsize)
print("Data type of a: ", a.dtype)


b = np.array([[1,2], [3,4], [5,6]])
print("b:\n",b)
print("Dimension of b:", b.ndim)


c = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
print("c:\n",c)
print("Itemsize of c: ", a.itemsize)
print("Data type of c:", c.dtype)
print("Array size of c:", c.size)
print("Shape of c:", c.shape)

d = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print("d:\n", d)

e = np.zeros((3, 4))
print("Array initialised with zeros:\n", e)

f = np.ones((3, 4))
print("Array initialsed with ones:\n", f)

g = np.arange(1, 5)
print("Array in the range of 1 - 5:\n", g)

h = np.arange(1, 5, 2)
print("Array in the range of 1-5 with stepsize as 2:\n", h)

i = np.linspace(1, 5, 10)
print("Generate 10 numbers in the range between 1-5 that are linearly spaced:\n", i)

j = np.array([[1,2], [3,4], [5,6]])
print("j:\n", j)
print("Shape of J:\n",j.shape)

j = j.reshape(2,3)
print("j:\n", j)
print("Shape of J:\n",j.shape)

j = j.ravel()
print("Flattened j:\n", j)
print("Shape of J:\n",j.shape)

j = np.array([[1,2], [3,4], [5,6]])
print("Min value in j:\n", j.min())

print("Max value in j:\n", j.max())

print("Sum of all values in j:\n", j.sum())

print("Sum of all values row-wise in j:\n", j.sum(axis=0))

print("Sum of all values column-wise in j:\n", j.sum(axis=1))

print("Square root of j:\n", np.sqrt(j))

print("Standard Deviation of j:\n", np.std(j))

print("Addition of two arrays:\n")

k = np.array([[1,2], [3,4]])
print("k:\n", k)

l = np.array([[5,6], [7,8]])
print("l:\n", l)

print("\nk+l:\n", k+l)


print("\nMatrix product of k and l:\n", k.dot(l))