""" note
    1. 装饰器（Decorator）允许在不修改原函数代码的情况下，为函数添加额外的功能。
    2. 装饰器本质上是一个Python函数（或其他可调用对象），它接受一个函数作为参数，并返回一个新的函数。装饰器使用@符号作为语法糖。
       （python一切皆对象，函数也是，函数可以作为一个参数被传入到函数中，也可以作为函数的返回值）
    通过一个简单的计算时间的例子，看一下装饰器的功能。"""

import time

# 不适用装饰器的写法
def not_decorator():
    def func01():
        time_start = time.time()
        time.sleep(0.5)
        print("这是第一个函数", end="。")
        time_end = time.time()
        cost = time_end - time_start
        print('函数1执行时间：', cost)

    def func02():
        time_start = time.time()
        time.sleep(1.5)
        print("这是第二个函数", end="。")
        time_end = time.time()
        cost = time_end - time_start
        print('函数2执行时间：', cost)

    def func03():
        time_start = time.time()
        time.sleep(1)
        print("这是第三个函数", end="。")
        time_end = time.time()
        cost = time_end - time_start
        print('函数3执行时间：', cost)

    if __name__ == '__main__':
        func01()
        func02()
        func03()


# 上面的实现方式看起来非常得臃肿，下面来试试装饰器的写法
def timer(function):
    def wrapper():
        time_start = time.time()
        resout = function()
        time_end = time.time()
        cost = time_end - time_start
        print('函数执行时间：', cost)
        return resout
    return wrapper

@timer
def func1():
    print("这是第一个函数", end="。")
    time.sleep(0.5)

@ timer
def func2():
    print("这是第二个函数", end="。")
    time.sleep(1.5)

def func3():
    print("这是第三个函数，不计算时间", end="。")


func1()
func2()
func3()

# 这样看起来，十分简洁啊
