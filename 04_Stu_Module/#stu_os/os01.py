"""os 模块是 Python 标准库中的一个重要模块，它提供了与操作系统交互的功能。
通过 os 模块，可以执行文件操作、目录操作、环境变量管理、进程管理等任务。"""
import os

def exs01():
    print("当前工作路径：", os.getcwd())       # 当前工作路径

    os.chdir(r"D:\NewFolder\pythonProject\study_note\src\04_Stu_Module\stu_os")     # 修改工作路径
    print("修改后的工作路径：", os.getcwd())

    print("当前路径下的目录：", os.listdir())    # 当前路径下的目录，类型为列表

def exs02():
    os.mkdir("new_dir1")     # 创建目录，如果目录已存在，报 FileExistsError
    print(os.listdir())

def exs03():
    os.rmdir("new_dir")    # 删除目录。如果目录不为空,报 OSError。如果不存在，报 FileNotFoundError

def exs04():            # 删除文件
    os.remove(r"D:\NewFolder\pythonProject\study_note\src\04_Stu_Module\stu_os\new_dir1\file01")

def exs05():
    os.rename("new_dir1", "new_dir2")   # 重命名目录
    os.rename(r"new_dir2/file01", r"new_dir2/file02")       # 重命名文件

def exs06():
    print(os.system("dir"))      # 执行shell命令

def exs07():
    print(os.stat(r"D:\NewFolder\pythonProject\study_note\src\04_Stu_Module\stu_os\new_dir2\file02"))       # 指定文件的状态信息

def exs08():
    print(os.path.exists(r"new_dir2\file02"))       # 判断文件或目录是否存在
    print(os.path.exists(r"new_dir2"))              # >> Ture


exs08()

