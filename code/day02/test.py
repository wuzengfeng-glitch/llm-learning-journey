import numpy as np

print(0*np.nan)

# # print(np.nan == np.nan)
# print(np.inf > np.nan)

# print(np.nan - np.nan)

# print(np.nan in set([np.nan]))

# print(0.3 == 3 * 0.1)

print(np.__version__)

# help(np.add)

# np.info(np.add)


# np.eye(3)

# arr=np.arange(9).reshape(3,3)
# print("arr:\n", arr)
# print(np.eye(3))
# print(np.identity(3))

# print(help(np.random.random))

# arr = np.array([1, 2, 0, 0, 4, 0])
# print(np.nonzero(arr))

# arr11=np.random.rand(3,3,3)
# print("arr11:\n", arr11)


# arr12=np.random.rand(12,12)
# print(arr12)
# print(arr12.min())
# print(arr12.max())


# a13=np.random.random(30)
# print(a13.mean())

# a14 = np.ones((5,5))
# a14[1:-1,1:-1] = 0
# print("a14:\n", a14)


# print(np.eye(5))

a = np.arange(9)
b=a.reshape(3,3)
print(b)
print(b[[1,2]])
# print(b>3)
# print(b[b>3])
# print(a)  # [0 1 2 3 4 5 6 7 8]
# print(a[2:5])  # [2 3 4]
# print(a[::-1])  # [8 7 6 5 4 3 2 1 0]
# a[[0,3]]


