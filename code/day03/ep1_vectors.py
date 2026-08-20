"""EP1 — 向量究竟是什么？

看完视频后在这里验证：
- 用 np.array 分别造一个二维向量和三维向量
- 打印 shape，感受"向量 = 一维数组"（一列数）
- 尝试 v1 + v2、3 * v1，对应视频里"向量加法 / 数乘"的几何直觉
"""
import numpy as np

v1=np.array([1,2])

v2=np.array([1,2,3])

print("v1.shape=", v1.shape)
print("v2.shape=", v2.shape)

print("v1=",v1)
print("v2=",v2)


u1=np.array([1,2])
u2=np.array([3,4])  
print("u1+u2=", u1+u2)
print("3*u1=", 3*u1)        





# TODO: 看完 EP1 再写
