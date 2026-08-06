import numpy as np
"""
def cosine_similarity(a, b):
    a = np.array(a)                    # 转成数组
    b = np.array(b)                    # 转成数组
    dot = a @ b                        # 点积
    norm_a = np.linalg.norm(a)         # a 的长度
    norm_b = np.linalg.norm(b)         # b 的长度
    return dot / (norm_a * norm_b)     # 返回结果

  # 测试
print(cosine_similarity([1, 0, 0], [1, 1, 0]))
print(cosine_similarity([1, 2, 3], [2, 4, 6]))
print(cosine_similarity([1, 0], [1, 0]))
"""
a=np.array([1, 0, 0])
b=np.array([1, 1, 0])
print("a=",a)
print("b=",b)

dot=np.dot(a,b)
print("dot=",dot)

norm_a=np.linalg.norm(a)
print("norm_a=",norm_a)
norm_b=np.linalg.norm(b)    
print("norm_b=",norm_b)

result=dot/(norm_a*norm_b)
print("result=",result) 