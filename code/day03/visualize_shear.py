"""可视化 B = [[1, t], [0, 1]] 水平剪切变换（t: 0 → 1）

跑起来看到的效果：
- 淡灰色网格 = 原始坐标（t=0，永远不动，作为参考）
- 蓝色网格 = 当前变换后的坐标，每 1 秒跳一步
- i-hat（绿）始终在 (1,0) 不动；j-hat（红）从 (0,1) 移到 (1,1)
- 紫色向量 v=[2,3] 被推到 [2+3t, 3]（x 被 y 拉动，y 不变）
- 淡色箭头 = 原始位置，深色箭头 = 变换后位置，一眼看出"从哪来到哪去"
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def make_grid(n=5):
    """返回一堆网格线段，shape (线段数, 2 端点, 2 坐标)。"""
    lines = []
    for x in range(-n, n + 1):
        lines.append([(x, -n), (x, n)])   # 垂直线
    for y in range(-n, n + 1):
        lines.append([(-n, y), (n, y)])   # 水平线
    return np.array(lines, dtype=float)


def shear(t):
    return np.array([[1, t], [0, 1]], dtype=float)


fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)

grid = make_grid()

# —— 原始坐标层（半透明，永远不动，作参考） ——
for seg in grid:
    ax.plot(seg[:, 0], seg[:, 1], color='gray', lw=0.5, alpha=0.25)

v0 = np.array([2, 3])
# 原始箭头（幽灵位置，半透明）
ax.quiver(0, 0, 1, 0,     angles='xy', scale_units='xy', scale=1, color='green',  alpha=0.25)
ax.quiver(0, 0, 0, 1,     angles='xy', scale_units='xy', scale=1, color='red',    alpha=0.25)
ax.quiver(0, 0, v0[0], v0[1], angles='xy', scale_units='xy', scale=1, color='purple', alpha=0.25)

# —— 变换后层（每帧更新） ——
line_objs = [ax.plot([], [], 'b-', lw=0.7, alpha=0.85)[0] for _ in grid]

i_arrow = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1,
                    color='green', label='i-hat')
j_arrow = ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1,
                    color='red', label='j-hat')
v_arrow = ax.quiver(0, 0, v0[0], v0[1], angles='xy', scale_units='xy', scale=1,
                    color='purple', label='v=[2,3]')
ax.legend(loc='upper left')

# 实时坐标文字（跟着箭头末端跑）
i_label = ax.text(0, 0, '', color='green',  fontsize=9, weight='bold')
j_label = ax.text(0, 0, '', color='red',    fontsize=9, weight='bold')
v_label = ax.text(0, 0, '', color='purple', fontsize=9, weight='bold')


def update(t):
    M = shear(t)
    new_grid = grid @ M.T          # (N, 2, 2) @ (2, 2) 对每个端点做 M @ p
    for line, seg in zip(line_objs, new_grid):
        line.set_data(seg[:, 0], seg[:, 1])

    i_new = M @ np.array([1, 0])
    j_new = M @ np.array([0, 1])
    v_new = M @ v0
    i_arrow.set_UVC(i_new[0], i_new[1])
    j_arrow.set_UVC(j_new[0], j_new[1])
    v_arrow.set_UVC(v_new[0], v_new[1])

    # 坐标标签：定位到箭头末端稍微偏一点，避免覆盖
    off = 0.15
    i_label.set_position((i_new[0] + off, i_new[1] + off))
    i_label.set_text(f"i=({i_new[0]:.2f}, {i_new[1]:.2f})")
    j_label.set_position((j_new[0] + off, j_new[1] + off))
    j_label.set_text(f"j=({j_new[0]:.2f}, {j_new[1]:.2f})")
    v_label.set_position((v_new[0] + off, v_new[1] + off))
    v_label.set_text(f"v=({v_new[0]:.2f}, {v_new[1]:.2f})")

    ax.set_title(f"B(t) = [[1, {t:.2f}], [0, 1]]   水平剪切")
    return line_objs + [i_arrow, j_arrow, v_arrow, i_label, j_label, v_label]


# 5 个关键帧 + 来回：0 → 0.25 → 0.5 → 0.75 → 1 → 0.75 → 0.5 → 0.25 → 0
ts = [0, 0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25]
anim = animation.FuncAnimation(fig, update, frames=ts, interval=1000, blit=False)

# —— 鼠标点击画面：暂停 / 再次点击：继续 ——
paused = [False]
def toggle_pause(event):
    if paused[0]:
        anim.resume()
    else:
        anim.pause()
    paused[0] = not paused[0]

fig.canvas.mpl_connect('button_press_event', toggle_pause)

plt.show()
