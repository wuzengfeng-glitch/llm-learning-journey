"""EP2 — 线性组合、张成、基

看完视频后在这里验证：
- 给定 v1, v2，计算若干 a*v1 + b*v2，观察它们"扫出"的空间
- 造一对共线的向量（如 v2 = 2*v1），验证它们张成的是一条线而不是平面
- 用 np.linalg.matrix_rank([v1, v2]) 检验线性相关：rank<2 就是线性相关
"""
import numpy as np

# TODO: 看完 EP2 再写
v1=np.array([1, 2])
v2=np.array([3, 4])     
v3=2*v1+3*v2
print("v1=", v1)
print("v2=", v2)
for a in [-1, 0, 1, 2]:
    for b in [-1, 0, 1]:
        print(a, b, a*v1 + b*v2)
print("v3=2*v1+3*v2=", v3)      

u1=np.array([4, 9])
u2=2*u1
print("u1=", u1)
print("u2=2*u1=", u2)
print("np.linalg.matrix_rank([u1, u2])=", np.linalg.matrix_rank([u1, u2]))  
print("np.linalg.matrix_rank([v1, v2])=", np.linalg.matrix_rank([v1, v2]))
rank_u = np.linalg.matrix_rank([u1, u2])
rank_v = np.linalg.matrix_rank([v1, v2])
print(f"rank={rank_u}, {'线性相关（共线）' if rank_u<2 else '线性无关（张成 R²）'}")
print(f"rank={rank_v}, {'线性相关（共线）' if rank_v<2 else '线性无关（张成 R²）'}")

