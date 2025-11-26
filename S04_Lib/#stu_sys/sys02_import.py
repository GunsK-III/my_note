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

# 可以去pkg1中看看发生了什么
def exs11():
    import pkg1
    pkg1.model_a.func_a()
    pkg1.model_b.func_b()


# exs11()


def exs12():
    from pkg1 import model_a
    model_a.func_c()

exs12()
