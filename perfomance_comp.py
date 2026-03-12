import numpy as np
import time

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
py_list = [x * 2 for x in py_list]
print("Python list time:", time.time() - start)

# NumPy array
np_array = np.arange(size)
start = time.time()
np_array = np_array * 2
print("NumPy array time:", time.time() - start)