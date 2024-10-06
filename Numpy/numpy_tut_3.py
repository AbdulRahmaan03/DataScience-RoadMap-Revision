import numpy as np
print("Slicing Techniques")
print("For lists:")

a = [1,2,3]
print("a: \n", a)
print("Siced: \n", a[0:2])


print("\nFor Arrays:")

a = np.array([1,2,3])
print("a: \n", a)
print("Siced: \n", a[0:2])

print("Multi-dimensional Array:\n")
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print("\nSlicing based on row and column")

print("3rd column 2nd element:\n", a[1,2])
print("2nd column elements in first two rows:\n", a[0:2, 2])

print("Last row:\n", a[-1])

print("Last two columns:\n", a[:, 1:3])

print("\nIterating through array:")
for row in a:
    print(row)

print("All elements printed out seperately:")
for cell in a.flat:
    print(cell)

print("\nStacking arrays:\n")

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)

print("a:\n",a)
print("b:\n",b)

print("\nVertically Stacked array:\n", np.vstack((a,b)))

print("\nHorizontally Stacked array:\n", np.hstack((a,b)))

a = np.arange(30).reshape(2,15)
print(a)
print("\nSplit horizontally into 3 arrays:")
result = np.hsplit(a,3)
print(result[0])
print(result[1])
print(result[2])

print("\nSplit vertically into 2 arrays:")
result = np.vsplit(a,2)
print(result[0])
print(result[1])

print("\nIndexing with boolean array\n")

a = np.arange(12).reshape(3,4)
print(a)

b = a > 4
print("\nBoolean indexed array, :\n", b)