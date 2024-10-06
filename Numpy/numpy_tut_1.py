import numpy as np
import time
import sys

# Declare a list of 1000 elements and print its size
l = range(1000)
print(f"List size: {sys.getsizeof(5)*len(l)}")

# Declare an array of 1000 elements and print its size
array = np.arange(1000)
print(f"Array size: {array.size*array.itemsize}")

# Inference 1: List takes more space as compared to NumPy Array


# Define size
size = 1000000

# Define two lists with size defined above
l1 = range(size)
l2 = range(size)

# Define two arrays with size defined above
a1 = np.arange(size)
a2 = np.arange(size)

# Add the two lists and see time taken for it
start = time.time()
result = [x + y for x, y in zip(l1, l2)]
print("List addition time: ", (time.time() - start) * 1000)

# Add the two numpy arrays and see the time taken for it
start = time.time()
result = a1 + a2
print("Numpy array addtion time: ", (time.time() - start) * 1000)

# Inference 2: List takes more computation time as compared to numpy array

# Conclusion: Numpy arrays are efficient than lists.