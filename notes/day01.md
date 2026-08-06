# Day 1 - 2026-08-03 起步（实际收尾 2026-08-06）

> 计划中的第一天，但实际拉长到多个自然日才做完。原因：Vector 类和 matplotlib 是首次接触，节奏放慢是对的，不用为进度焦虑。

## 今日目标（原计划）

- [x] 环境搭建（Python / PyTorch / CUDA 验证）
- [x] Python / NumPy 基础自测（4 题）
- [x] 建立 GitHub 学习仓库 `llm-learning-journey`

## 完成的 4 道题

| 题号 | 主题 | 文件 |
|---|---|---|
| 1 | NumPy 余弦相似度 | `code/day01/practice.py` |
| 2 | 列表推导式（素数 / 偶数 / 纯小写词） | `code/day01/primeNum.py` |
| 3 | Vector 类，重载 `+` `-` `*`（点积） | `code/day01/vector.py` |
| 4 | Matplotlib 画 sin/cos 双曲线 | `code/day01/plot_sincos.py` |

## 学到的关键点

### NumPy
- `np.dot(a, b)` 或 `a @ b` 都能算点积
- `np.linalg.norm(v)` 求向量模长
- `np.linspace(start, stop, n)` 第三个参数是**点的个数**（含端点），别和 `np.arange(start, stop, step)`（第三个是步长，不含终点）搞混
- **向量化**：`np.sin(x)` 直接作用在整个数组上，底层是 C 循环，比 Python 的 `for v in x: math.sin(v)` 快一到两个数量级

### Python OOP
- 运算符重载靠"魔法方法"（dunder methods）：
  - `+` → `__add__(self, other)`
  - `-` → `__sub__(self, other)`
  - `*` → `__mul__(self, other)`
  - `print(obj)` 输出格式 → `__repr__(self)`
- `sum(a * b for ...)` 用**生成器表达式**比 `sum([a * b for ...])` 更省内存，因为不构建中间列表

### Matplotlib
- `plt.plot` 连续调用两次会画在**同一张图**上（有"当前图"的概念）
- `label=` 只是登记名字，必须调 `plt.legend()` 才会显示图例
- `plt.savefig()` 必须在 `plt.show()` **之前**，否则 show() 关闭窗口后当前图被清空，存出来是空白

## 遇到的坑

1. **缩进 bug**：把 `__add__`、`__sub__`、`__mul__` 错误地写在了 `__init__` 内部（缩进比 `__init__` 更深），导致这些方法根本没注册到类上。教训：Python 靠缩进划分作用域，class 里所有方法的 `def` 必须**平级对齐**。
2. **点积的语义**：一开始 `__mul__` 只写了逐元素相乘 `[a*b for ...]` 就返回了，忘了点积还需要**求和**这一步。
3. **f-string 少引号**：`return f"Vector({self.data})` 少了收尾 `"`，Python 报 `SyntaxError: unterminated string literal`。

## 明日计划（Day 2）

- 主学习：NumPy Quickstart 官方教程 https://numpy.org/doc/stable/user/quickstart.html
- 动手：numpy-100 前 15 题 https://github.com/rougier/numpy-100
- 重点掌握：广播（broadcasting）、切片、`reshape` / `axis` 参数
