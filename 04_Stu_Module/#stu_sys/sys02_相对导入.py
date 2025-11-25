import sys


# 先来看一下当前默认的导包路径（模块搜索路径），这就是直接导入模块时，解释器搜索的路径
def exs10():
    print(sys.path)
r"""
    在我的计算机中，输出的是
    ['D:\\NewFolder\\pythonProject\\study_note\\src\\04_Stu_Module\\#stu_sys',
    'D:\\NewFolder\\pythonProject\\study_note',
    'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip',
    'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\DLLs',
    'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\Lib',
    'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311',
    'D:\\NewFolder\\pythonProject\\study_note\\.venv',
    'D:\\NewFolder\\pythonProject\\study_note\\.venv\\Lib\\site-packages']
    Python解释器依照上面的顺序去这些路径下寻找模块。
    上个文件中讲到可以使用sys动态修改导包路径，下面来看一下
"""


# 首先可以直接导入 sys.path 路径下的 包（packages）和模块（module）
def exs11():
    from sys01_base import exs01
    exs01()


def exs12():
    from dir1.my_packages import my_package
    my_package()

# def exs13():
#     from . import sys01_base
#     sys01_base.exs01()
# exs13()


# def exs13():
#     sys.path.append(r'D:\NewFolder\pythonProject\study_note\src')
# exs13()

# model not found 问题还没解决，明天再来看看
