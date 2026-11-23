"""EP7 — 逆矩阵、列空间与零空间

看完视频后在这里验证：

1. 逆矩阵：M 可逆时，M_inv = np.linalg.inv(M)，验证 M @ M_inv ≈ I（用 np.allclose）
2. 解方程 Ax=b：np.linalg.solve(A, b)，几何上就是"找一个 x，让 A 把它变到 b"
3. 不可逆情形：造一个 det=0 的矩阵（如 [[1,2],[2,4]]），
   - np.linalg.inv(M) 会报错 LinAlgError
   - np.linalg.matrix_rank(M) < n → 秩不足
   - 列空间被压到更低维度：这个矩阵的输出只落在一条直线上
4. 零空间（Null space）：满足 M @ v = 0 的所有 v 组成的空间
   - 用 scipy.linalg.null_space(M) 求（或手推）
   - 可逆矩阵的零空间只有零向量；不可逆矩阵有非零零空间

关键概念：
  秩（rank）= 列空间的维度 = 变换后空间被"压"到几维
  满秩 = 秩等于 n = 可逆 = det ≠ 0 = 零空间只有零向量
"""
import numpy as np

# TODO: 看完 EP7 再写
