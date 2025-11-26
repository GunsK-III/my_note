# 下面是绝对导入，使用完整的模块路径进行导入，最简单的调用方法
# from model_b import func_b
# func_b()
# 如果一个python文件在当前目录的父目录下，则需要先将目录添加到sys.path中，才能导入

# 下面是相对导入，相对于当前模块的位置来导入其他模块，使用点（.）表示层级关系：
from .model_b import func_b
func_b()
# from ..pkg2.model_c import func_c       # 这个方法不可用
# func_c()
# 相对导入，只能在包内使用，也就是说，包含相对导入的文件不能直接作为脚本运行

# 不用管这个
def func_a():
    print("func_a is called.")
