# 生成1到10的平方数列表

"""
squares = [x**2 for x in range(1,11)]   
print(squares)

#生成1到20里所有的偶数列表
evens = [x for x in range(1,21) if x%2==0]
print(evens)

n=7
result =all(n % i !=0 for i in range(2,int(n**0.5)+1)  )

print(result)   

"""
"""
result=[x for x in range(1,101) if (x % 3==0 and x % 5!=0)]
print(result)

"""
"""
fouth=input("Year：")
print(fouth)
print(fouth[-1])"""


# words = ["hello", "World", "python", "AI", "code", "GPU", "learn"]
# result=[x for x in words if all(ch.islower() for ch in x)]
# print(result)

