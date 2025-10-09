# 通过下面这里例子，先来了解什么是“一切皆对象”

def git_multiple_func(n):

    def multiple(x):
        return x * n

    return multiple


double = git_multiple_func(2)
triple = git_multiple_func(3)

print(double(3))
print(triple(3))
