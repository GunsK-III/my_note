# 全局变量（global），就是为了在函数中使用函数外的变量
def exs01():
    x = 100

    def foo():
        x = 5           # 这里新建了一个局部变量 x，完全不会碰外面的 100，但是不建议这么写。
        print('函数内部 x =', x)

    foo()                    # → 函数内部 x = 5
    print('全局 x =', x)      # → 全局 x = 100


def exs02():
    count = 0                # 全局计数器

    def add_one():
        global count        # 声明“下面的 count 就是全局那个”
        count += 1
        print('内部 count =', count)

    add_one()               # → 内部 count = 1
    add_one()               # → 内部 count = 2
    print('外部 count =', count)  # → 外部 count = 2


