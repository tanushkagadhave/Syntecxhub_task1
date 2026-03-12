import numpy as np

# Array creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(1, 13)
arr3 = np.random.randint(1, 100, size=(3, 4))

print("1D Array:", arr1)
print("2D Random Array:\n", arr3)

# Indexing & slicing
print("First element:", arr1[0])
print("Slice:", arr1[1:4])
print("2D Slice:\n", arr3[:, 1:3])

# Mathematical operations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))

# Axis-wise operations
print("Column-wise sum:", np.sum(arr3, axis=0))
print("Row-wise mean:", np.mean(arr3, axis=1))

# Reshaping
reshaped = arr2.reshape(3, 4)
print("Reshaped Array:\n", reshaped)

# Broadcasting
broadcasted = reshaped + 10
print("Broadcasted Array:\n", broadcasted)

# Save and load
np.save("sample_array.npy", reshaped)
loaded_array = np.load("sample_array.npy")
print("Loaded Array:\n", loaded_array)