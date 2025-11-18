""" 函数的一些特性"""

""" 01 函数参数的默认值在函数定义时就会被计算，而不是在调用时
       所以下面这段程序中即便没有调用func1()，但是运行后还是会等待输入。"""
def func0():
    def func1(a=input("func1()被调用了。")):
        print("func1", a)

    def func2():
        print("func2")

    func2()  # >> 函数func1()被调用了。


""" 02 函数类型注解（type hints），指定输入输出的格式
       如果指定的类型和实际的类型不一致，不会报错，只是在编辑器中提醒"""
def func3(user_input: str, other_input: str) -> tuple[int, str]:
    return len(user_input), other_input


""" 03 函数的传参格式。先解释一下一些名词。
       positional arguments：位置参数。调用函数时使用。传入数值时顺序至关重要，解释器根据位置来确定哪个值赋给哪个参数。
       keyword arguments：关键字参数。调用函数时使用。传入数值的顺序可以随意。
       default arguments：默认参数。定义函数时使用。可赋予入参默认值。
       parameters：形式参数。定义函数时使用。默认参数之后不能有形式参数。
       *args：可变位置参数。定义函数时使用。可接受任意数量的位置参数。
       **kwargs：可变关键字参数。定义函数时使用。可接受任意数量的关键字参数。"""
def func4(par1: str, par2: str, def_arg1: str = 'def1', def_arg2: str = 'def2'):
    print(par1, par2, def_arg1, def_arg2)


# def func5(par1, def_arg1='def1', par2):         # 不合法，默认形参后面不能跟没有默认值的必需参数


# func4('arg1', 'arg2')                      # 位置参数，依赖顺序。 >> arg1 arg2 def1 def2
# func4('arg1', 'arg2', 'def1', 'def2')      # 默认参数，可以缺省。 >> arg1 arg2 def1 def2
# func4('arg1', 'arg2', def_arg2='def2', def_arg1='arg1')       # 关键字参数，不依赖顺序。 >> arg1 arg2 def1 def2
# func4('arg1', 'arg2', def_arg1='def1', 'def2')                # 不合法，位置参数必须在关键字参数之前，一旦开始使用关键字参数，后面的所有参数都必须是关键字参数


def comprehensive_example(a, b, /, c, d=10, *, e, f=20, **kwargs):
    """
    a, b: 仅位置参数
    c, d: 位置或关键字参数（d有默认值）
    e, f: 仅关键字参数（f有默认值）
    **kwargs: 接收其他关键字参数
    """
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
    if kwargs:
        print(f"其他参数: {kwargs}")

# comprehensive_example(1, 2, 3, e=30)                           # 使用d和f的默认值
# comprehensive_example(1, 2, c=3, d=40, e=30, f=50)             # 指定所有参数
# comprehensive_example(1, 2, 3, e=30, extra1="x", extra2="y")   # 带额外参数


""" 04 内置函数。
    当这个模块被调用时，只有公共函数被调用，内部函数不被调用"""
def _internal_function():
    print("内部函数")
