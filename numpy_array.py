import numpy as np

integerArray = np.array([1,2,3,4], int)

print(integerArray[0])

print(integerArray[:2])

print(2 in integerArray)

integerArray2 = np.array([5, 8], int)

print(np.concatenate((integerArray, integerArray2)))

print(np.zeros(10))

print(np.ones(10, dtype=int))

rangeArray = np.array(range(10), int)

print(rangeArray)