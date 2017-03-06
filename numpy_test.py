import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.int32)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("a dot b : \n", np.dot(a, b))
print("b dot a : \n", np.dot(b, a))

a = np.array([3, 4])
b = np.array([[1], [2], [3]])
print("a * b : \n", a * b)
print("b * a : \n", b * a)

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print("a * b : \n", a * b)
print("a dot b : \n", np.dot(a, b))
