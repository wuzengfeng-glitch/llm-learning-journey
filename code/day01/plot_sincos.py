# np / plt 是社区约定俗成的别名，几乎所有教程和文档都这么写。
# pyplot 是 matplotlib 里模仿 MATLAB 的绘图接口。
import numpy as np
import matplotlib.pyplot as plt


# linspace = linearly spaced，「线性等距取点」：
# 在 [0, 2π] 闭区间上均匀取 200 个点，包含两个端点。
#   np.linspace(0, 10, 5) -> [0., 2.5, 5., 7.5, 10.]
#
# 注意第三个参数是「点的个数」，不是步长。
# 容易和 np.arange(0, 10, 0.5) 搞混 —— 那个第三参数是步长，且不含终点。
#
# 200 是采样密度：点越多曲线越平滑。改成 10 试试，会看到明显的折线。
x = np.linspace(0, 2 * np.pi, 200)  # 生成从0到2π的200个点

# NumPy 的核心特性：向量化(vectorization)。
# x 是含 200 个元素的数组，np.sin(x) 一次性对每个元素求正弦，
# 返回同样 200 个元素的新数组，不需要写循环。
#   NumPy 写法： y_sin = np.sin(x)
#   纯 Python ： y_sin = [math.sin(v) for v in x]   # 慢
# 底层是 C 循环，比 Python 循环快一到两个数量级。
y_sin = np.sin(x)
y_cos = np.cos(x)

# plot(x, y) 把 200 个 (x, y) 点用直线依次连起来。
# 所谓「曲线」其实是 200 段极短的折线，只是密到肉眼看不出来。
#
# 调用两次 plt.plot 会画在同一张图上（matplotlib 有「当前图」的概念，
# 后续命令都作用于它），颜色自动分配：第一条蓝、第二条橙。
#
# label= 本身不显示任何东西，只是给曲线登记名字，
# 要等下面的 plt.legend() 才会把这些名字收集起来画成图例框。
# 没有 legend() 的话 label 白写。
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

plt.xlabel('x')                          # x 轴标签
plt.ylabel('y')                          # y 轴标签
plt.title('Sine and Cosine Functions')   # 标题
plt.legend()                             # 图例（读取上面的 label）
plt.grid(True)                           # 显示网格线

# show() 必须放在最后。它会打开一个交互窗口，程序停在这里(阻塞)，
# 直到你手动关掉窗口才继续往下执行。
#
# 若想存成文件而不是弹窗，换成：
#   plt.savefig('sincos.png', dpi=150)
# 注意 savefig 要写在 show() 之前 —— show() 关闭窗口后会清空当前图，
# 之后再存就是空白图了。

plt.savefig('sincos.png', dpi=150)   # 放在 show() 之前
plt.show()

