"""os 模块是 Python 标准库中的一个重要模块，它提供了与操作系统交互的功能。
通过 os 模块，可以执行文件操作、目录操作、环境变量管理、进程管理等任务。"""
import os

def exs01():
    print("当前工作路径：", os.getcwd())       # 获取当前工作路径
    print("路径下的目录：", os.listdir())      # 获取当前os路径下的文件和目录，类型为列表

    os.chdir(r"D:\NewFolder\pythonProject\study_note\src\S04_Lib\#stu_os\new_dir2")     # 修改工作路径
    print("修改后的工作路径：", os.getcwd())
    print("路径下的目录：", os.listdir())

def exs02():
    os.mkdir("new_dir1")     # 创建目录，如果目录已存在，报 FileExistsError
    print(os.listdir())      # （创建文件的方法可以使用open()的w方法。）

def exs03():
    os.rmdir("new_dir")      # 删除目录。如果目录不为空,报 OSError。如果不存在，报 FileNotFoundError

def exs04():                 # 删除文件
    os.remove(r"D:\NewFolder\pythonProject\study_note\src\04_Stu_Module\stu_os\new_dir1\file01")

def exs05():
    os.rename("new_dir1", "new_dir2")                           # 重命名目录
    os.rename(r"new_dir2/file01", r"new_dir2/file02.txt")       # 重命名文件

def exs06():
    print(os.stat(r"new_dir2\file02.txt"))                      # 获取指定文件的状态信息

def exs07():
    print(os.path.exists(r"new_dir2/file02.txt"))               # 判断文件是否存在
    print(os.path.exists(r"new_dir2"))                          # 判断路径是否存在。 >> True
    print(os.path.isdir(r"new_dir2"))                           # 判断是否是目录
    print(os.path.isfile(r"new_dir2/file02.txt"))               # 判断是否是文件

def exs08():
    full_path = os.path.join(r'D:\NewFolder', r'pythonProject\study_note',
                             r'src\04_Stu_Module', r'#stu_os')  # 拼接路径
    print("路径：", full_path, "\n存在状态：", os.path.exists(full_path))

    dirname = os.path.dirname(full_path)        # 目录名
    basename = os.path.basename(full_path)      # 文件名
    split_result = os.path.split(full_path)     # 分割路径
    print(dirname, "\n", basename, "\n", split_result)

    file_name = str(input("输入文件名（01_os_操作文件目录.py、02_os_命令行输入.py）："))
    full_path2 = os.path.join(r'D:\NewFolder\pythonProject\study_note\src\04_Stu_Module\#stu_os',
                              file_name)
    print(f"{file_name}的信息是：", os.stat(full_path2))

def exs09():
    pid = os.getpid()           # 获取进程ID
    print(f"当前进程ID: {pid}")

    ppid = os.getppid()         # 获取父进程ID
    print(f"父进程ID: {ppid}")


exs09()

