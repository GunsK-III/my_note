r"""
先看一下 sys.path，重点在第二行 D:\\NewFolder\\pythonProject\\study_note
['D:\\NewFolder\\pythonProject\\study_note\\src\\S04_Lib\\#stu_sys\\pkg1\\sub_pkg1',
'D:\\NewFolder\\pythonProject\\study_note',
'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip',
'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\DLLs',
'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311\\Lib',
'C:\\Users\\BMF\\AppData\\Local\\Programs\\Python\\Python311',
'D:\\NewFolder\\pythonProject\\study_note\\.venv',
'D:\\NewFolder\\pythonProject\\study_note\\.venv\\Lib\\site-packages']
"""

def func_a():
    print("func_a is called.")


def exs_sys01():    # 可以直接导入
    from model_b import func_b
    func_b()

def exs_sys02():    # 可以同级相对导入
    from .model_b import func_b
    func_b()

def exs_sys03():    # 可以从上一级相对导入
    from ..sub_pkg2.model_c import func_c
    func_c()


def exs_sys04():    # 这个方法是失败的
    from ...pkg2.model_d import func_d
    func_d()

# 在 #stu_sys/ 目录下运行 python sys02_import.py
# Python 的 sys.path[0] 是 #stu_sys/（当前目录）
# 所以 from pkg1.sub_pkg1 import model_a 能成功（因为 pkg1 在当前目录下）
# 但是！此时 #stu_sys 本身不被视为一个包，只是一个包含模块的文件夹
# 因此，当 model_a.py 尝试 from ...pkg2... 时，
# 它认为自己的包是 pkg1.sub_pkg1（因为 #stu_sys 没被当作包）
# 那么 ... 就试图跳出 pkg1 → 到“项目根目录的父目录”，这就 超出了顶层包！
# 这就是报错的真正原因。

