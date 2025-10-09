# decorator 本身就是一个 callable
# decorator 可以认为是一个输入和输出全是 函数 的 函数。

def deco(f):
    pass

@deco
def double(x):
    return x * 2

# 完全等价于
double = deco(double)

