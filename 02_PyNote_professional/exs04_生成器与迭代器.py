""" 生成器（generator）与迭代器。"""

""" 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器："""

def exs01():
    list1 = [1, 2, 3, 4]
    it = iter(list1)                  # 使用iter()创建迭代器对象。
    print("第一次迭代：", next(it))     # 使用next()输出迭代器下一个元素。>> 1
    print("第二次迭代：", next(it))     # >> 2

def exs02():
    """迭代器对象可以使用 for 语句进行遍历"""
    list1 = [1, 2, 3, 4]
    it = iter(list1)  # 创建迭代器对象
    for x in it:
        print(x, end=" ")       # >> 1 2 3 4

def exs03():
    import sys  # 引入 sys 模块
    list1 = [1, 2, 3, 4]
    it = iter(list1)  # 创建迭代器对象

    while True:
        try:
            print(next(it))
        except StopIteration:       # 一旦迭代器中没有更多元素可返回，就会抛出 StopIteration 异常
            sys.exit()              # 终止整个程序。下方代码不再执行。和break不同，break只能跳出循环。

def exs04():
    """迭代器在类中的使用。"""
    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            return x

    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))


""" 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    yield 用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
    然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，
    直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
    调用一个生成器函数，返回的是一个迭代器对象。"""

def exs05():
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    generator = countdown(5)    # 创建生成器对象

    print(next(generator))  # 通过迭代生成器获取值。>> 5
    print(next(generator))  # >> 4
    print(next(generator))  # >> 3

    for value in generator:    # 使用 for 循环迭代生成器
        print(value)        # >> 2 1


# def Iterator():
#     a = 1
#     while a < 4:
#         yield a
#         a += 1
#
#
# b = 1
# for value in Iterator():
#     print(f"第{b}次迭代", value)
#     b += 1
