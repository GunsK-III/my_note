# 斐波那契数
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
def fib1():
    """推荐算法"""
    a1 = a2 = 1
    n = int(input("输入序号："))
    for i in range(n - 2):
        a1, a2 = a2, a1 + a2  # 这一行代码不能分成两行
    print(f"斐波那契数列第{n}个数是：", a2)


def fib2(n):
    """递归算法（性能较差，一般不推荐）"""
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


n = int(input("序号："))
res = fib2(n)
print(f"斐波那契数列第{n}个数是：{res}", )
