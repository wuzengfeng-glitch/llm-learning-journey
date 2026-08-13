"""
numpy-100 前 15 题 — Day 2 手写练习
原题库：https://github.com/rougier/numpy-100

规则：
1. 每题自己写，卡壳超 20 分钟才允许问我要 hint
2. 全部做完后统一让我检查，不要一题问一次
3. 遇到不会的函数：优先用 help(np.xxx) 或官方文档，锻炼查文档能力
"""

import numpy as np


# ===== Q1. Import numpy as np and print the numpy version =====
# (import 已在上面完成，这里只需 print 版本)

print(np.__version__)
# ===== Q2. Create a null vector of size 10 =====
# 提示：null vector = 全 0 的一维数组

c1=np.zeros(10)
# ===== Q3. How to find the memory size of any array? =====
# 提示：数组占内存 = 元素个数 × 每个元素占的字节数
# 用两个属性组合起来

print(c1.nbytes)

# ===== Q4. How to get the documentation of the numpy add function from the command line? =====
# 提示：Python 里怎么看一个函数的文档？（想想 help）
help(np.add)

# ===== Q5. Create a null vector of size 10 but the fifth value which is 1 =====
# 提示：先造全 0，然后把 index=4 的位置改成 1
# （题目说 "fifth value" 意思是第 5 个元素，index 从 0 开始所以 index=4）

c1=np.zeros(10)
c1[4]=1
# ===== Q6. Create a vector with values ranging from 10 to 49 =====
# 提示：想想 arange
# 结果应该是 [10, 11, 12, ..., 49]，共 40 个元素
c2=np.arange(10,50)  

# ===== Q7. Reverse a vector (first element becomes last) =====
# 提示：切片！Day 2 关卡 A 学过
# 造一个测试数组，然后反转
v = np.arange(10)
print(v[::-1])
# ===== Q8. Create a 3x3 matrix with values ranging from 0 to 8 =====
# 提示：arange + reshape 组合技
np.arange(9).reshape(3,-1)

# ===== Q9. Find indices of non-zero elements from [1,2,0,0,4,0] =====
# 提示：查一下 np.nonzero
arr = np.array([1, 2, 0, 0, 4, 0])
print(np.nonzero(arr))


# ===== Q10. Create a 3x3 identity matrix =====
# 提示：单位矩阵有专门的函数，查 np.eye 或 np.identity
np.eye(3)
np.identity(3)  
# ===== Q11. Create a 3x3x3 array with random values =====
# 提示：用 np.random.random 或 np.random.rand
# 注意两者传参方式不一样
arr11=np.random.rand(3,3,3)

# ===== Q12. Create a 10x10 array with random values and find the minimum and maximum values =====
# 提示：造完之后用 .min() 和 .max() 方法

arr12=np.random.rand(10,10)
print(arr12.min())
print(arr12.max())

# ===== Q13. Create a random vector of size 30 and find the mean value =====
# 提示：.mean() 方法

a13=np.random.random(30)
print(a13.mean())
# ===== Q14. Create a 2d array with 1 on the border and 0 inside =====
# 提示：这题稍难，两种思路都可以：
#   思路 A：先造全 1 矩阵，然后把"内部"切片赋值为 0
#   思路 B：先造全 0 矩阵，然后把"边界"赋值为 1
# 建议做一个 5x5 的测试，结果应该长这样：
# [[1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]]
a14 = np.ones((5,5))
a14[1:-1,1:-1] = 0

# ===== Q15. What is the result of the following expression? =====
# 不要跑代码，先猜每一行的结果，然后跑验证
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)
#
# 猜完了再取消注释运行，观察结果是否和你想的一样
# 这题考的是 IEEE 754 浮点数特殊值 (nan, inf) 和浮点精度的坑
# 答案
# nan
# false
# false
# nan
# true
# false