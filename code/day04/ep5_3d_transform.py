"""EP5 — 三维空间中的线性变换

看完视频后在这里验证：
- 造一个 3×3 矩阵 M，M 的三列分别是 i-hat, j-hat, k-hat 变换后的位置
- 验证 M @ v 等于 v[0]*M[:,0] + v[1]*M[:,1] + v[2]*M[:,2]（3D 版的 EP3 公式）
- 试两个 3D 变换（如绕 z 轴 90° 旋转、绕 x 轴 90° 旋转）的**复合**，
  看 A @ B 和 B @ A 结果不同（3D 里旋转顺序更不能颠倒——想象魔方转法）

参考矩阵：
  绕 z 轴 90° 逆时针：[[0,-1,0],[1,0,0],[0,0,1]]
  绕 x 轴 90° 逆时针：[[1,0,0],[0,0,-1],[0,1,0]]
"""
import numpy as np


# ---------- 1. 用三列构造 3×3 矩阵 ----------
# 自己定 i-hat, j-hat, k-hat 变换后落在哪里
i_hat = np.array([1, 0, -1])
j_hat = np.array([2, 1, 0])
k_hat = np.array([0, 3, 1])

# column_stack：把三个向量当作“列”拼起来（注意不是 np.array([...]) ，那样是按行拼）
M = np.column_stack([i_hat, j_hat, k_hat])
print("M =\n", M)
print("M 的第 0 列（i-hat 落点）:", M[:, 0])

# ---------- 2. 验证 M @ v == 三列的线性组合 ----------
v = np.array([3, -2, 5])

by_matmul = M @ v
by_columns = v[0] * M[:, 0] + v[1] * M[:, 1] + v[2] * M[:, 2]

print("\nv =", v)
print("M @ v           =", by_matmul)
print("列的线性组合     =", by_columns)
print("两者相等？", np.allclose(by_matmul, by_columns))

# ---------- 3. 3D 旋转复合：顺序很重要 ----------
Rz = np.array([[0, -1, 0],
               [1,  0, 0],
               [0,  0, 1]])   # 绕 z 轴 90° 逆时针
Rx = np.array([[1, 0,  0],
               [0, 0, -1],
               [0, 1,  0]])   # 绕 x 轴 90° 逆时针

# 矩阵乘法从右往左读：Rz @ Rx 表示“先 Rx，再 Rz”
first_x_then_z = Rz @ Rx
first_z_then_x = Rx @ Rz

print("\n先绕 x 再绕 z（Rz @ Rx）=\n", first_x_then_z)
print("先绕 z 再绕 x（Rx @ Rz）=\n", first_z_then_x)
print("两者相等？", np.array_equal(first_x_then_z, first_z_then_x))

# 用 i, j, k 各自追踪一下，更直观
basis = {"i": np.array([1, 0, 0]), "j": np.array([0, 1, 0]), "k": np.array([0, 0, 1])}
print("\n基向量落点对比：")
for name, e in basis.items():
    print(f"  {name}: 先x后z → {first_x_then_z @ e},  先z后x → {first_z_then_x @ e}")

# 额外验证：复合矩阵 == 依次施加两个变换
w = np.array([1, 2, 3])
print("\n(Rz @ Rx) @ w =", first_x_then_z @ w, "  Rz @ (Rx @ w) =", Rz @ (Rx @ w))
