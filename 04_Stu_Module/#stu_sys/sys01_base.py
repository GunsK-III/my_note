"""
    sys 模块主要用于与 Python 解释器（运行时环境）进行交互
"""

import sys

""" # -01-
    sys.argv 是一个列表，包含了传递给Python脚本的命令行参数
    列表的第一个元素是脚本本身的文件名
    后续元素依次是传递给脚本的各个参数
"""
def exs01():
    print("sys.argv: ", sys.argv)


""" # -02-
    返回 Python 解释器的版本字符串
"""
def exs02():
    print(sys.version)
    print(sys.version_info)


""" # -03-
    返回当前操作系统标识符
"""
def exs03():
    print(sys.platform)     # >> win32


""" # -04-
    打印出来的是Python模块搜索路径的列表。
    这个列表决定了Python解释器在执行import语句时按什么顺序在哪些目录中查找模块文件。
    每个系统的具体路径会因为Python安装位置、操作系统和环境配置的不同而有所差异。
    包含当前目录、PYTHONPATH 环境变量内容、标准库路径等。
    可以动态修改，用于临时添加模块搜索路径。
"""
def exs04():
    print(sys.path)


""" # -05-
    立即终止程序执行，之后的代码不可到达。
    传入的字符串可以打印出来。
     下面会发生一个现象：控制台中“退出程序！”在“sys.argv:”的上面，
     这是因为print() 函数默认会将输出内容先放入缓冲区，
     缓冲区的内容不会立即显示到控制台，而 sys.exit() 会立即终止程序，
     程序退出时缓冲区被强制刷新，之前缓存的 print 内容才得以显示。
"""
def exs05():
    sys.exit("退出程序！")

