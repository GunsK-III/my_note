# decorator 本身就是一个 callable
# decorator 可以认为是一个输入和输出全是 函数 的 函数。

def deco(f):
    return f


# 下面两种写法，效果完全等价
@deco
def double(x):
    return x * 2


double = deco(double(2))
print("res:", double)
