class Vector:
    def __init__(self, data):
      self.data = list(data)
    

    def __add__(self, other):
      # __add__ 是「魔术方法」(magic/dunder method)：写 v1 + v2 时，
      # Python 在背后调用 v1.__add__(v2)。self = 加号左边，other = 右边。
      #
      # zip 把两个列表按位置「拉链式」配对：
      #   [1,2,3] 与 [4,5,6] -> (1,4), (2,5), (3,6)
      # 注意坑：zip 在较短的列表用完时就停止，不报错。
      #   Vector([1,2,3]) + Vector([4,5]) -> Vector([5,7])，静默丢掉第三个元素。
      #   若想严格，可先判断 len(self.data) != len(other.data) 再 raise ValueError。
      new_data = [a + b for a, b in zip(self.data, other.data)]
      # 返回「新的 Vector」而不是裸 list，也不修改 self（不可变风格）。
      # 这样结果才能继续参与运算，如 (v1 + v2) * v3。
      return Vector(new_data)
    

    def __sub__(self, other):
      # [a - b for ...] 是「列表推导式」(list comprehension)，不是列表字面量。
      # 方括号里写的是「生成数据的规则」，不是写死的数据，但结果类型同样是 list。
      #
      # 读法：先读右边(怎么循环)，再读左边(每轮存什么)
      #   [  a - b   for a, b in zip(...)  ]
      #      ↑存什么      ↑怎么循环
      #
      # 等价于下面 3 行 for 循环：
      #   new_data = []
      #   for a, b in zip(self.data, other.data):
      #       new_data.append(a - b)
      #
      # 换个括号就是别的类型：
      #   [x for x in ...]      -> list
      #   (x for x in ...)      -> 生成器，惰性求值不占内存(见 __mul__)
      #   {x for x in ...}      -> set，自动去重
      #   {k: v for k, v in ...} -> dict
      new_data = [a - b for a, b in zip(self.data, other.data)]
      return Vector(new_data)

    def __mul__(self, other):
      # 和 __add__ / __sub__ 不同：这里是圆括号的「生成器表达式」，
      # 不会真的建出列表，而是「算一个吐一个」交给 sum() 累加，更省内存。
      # 返回的是标量 int（点积 dot product），不是 Vector。
      return sum(a * b for a, b in zip(self.data, other.data))

    def __repr__(self):
      # 决定 print(v1) 显示成 Vector([5, 7, 9])，
      # 而不是默认的 <__main__.Vector object at 0x...>
      return f"Vector({self.data})"


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)   # Vector([5, 7, 9])
print(v1 - v2)   # Vector([-3, -3, -3])
print(v1 * v2)   # 32