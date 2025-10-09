# 学习numpy库时的一些笔记.《对将要运算的数据，需要预先将它们表述成numpy数组的形式（向量化）》
"""这里有对numpy的较为详细的介绍https://www.labri.fr/perso/nrougier/from-python-to-numpy/"""
import numpy as np

"""基本信息"""
a = np.array([1, 2, 3, 4, 5, 6])  # 可以用array函数创建/初始化数组
print(a, type(a))    # >> [1 2 3 4 5 6]
# print(a.shape)     # 获取数组尺寸   >> (6,)
# print(a.ndim)       # 获取数组维度   >> 1
b = np.array([[1, 2, 3], [4, 5, 6]])  # 二维数组可以用来存放矩阵或表格数据
# print(b.shape)      # >> (2, 3)   第一个数字表示第一维的尺寸（行数），第二个同理（列数）
# print(b.T)      # 矩阵转置
# print(a.max, a.min, a.sum, a.mean)      # 最大值，最小值，求和，均值
# print(a.argmin, a.argmax)       # 返回值的索引
# print(np.median, np.mean, np.std)       # 中位数，均值，标准差


'''自动创建'''
c = np.zeros([2, 3])  # 2, 3表示数组尺寸，创建2行3列的全零数组
d = np.ones([2, 3])  # 创建全1数组
e = np.arange(1, 5)  # 创建(1, 5]的一维数组
# print(e)  # >> [1 2 3 4]
f = np.linspace(0, 10, 6)  # 于[0, 10]中取等间分布的6个数
# print(f)  # >> [ 0.   2.5  5.   7.5 10. ]

'''随机数'''
g = np.random.rand(2, 4)  # 创建2行4列随机数组，每个数值在[0, 1)之间
# print(g)
# print(np.random.rand())     # 返回一个 [0, 1) 区间内的随机浮点数
# print(np.random.rand(5))    # 返回一个形状为 (5,) 的一维数组，包含 5 个随机浮点数
# print(np.random.rand(2, 3, 4))  # 返回一个形状为 (2, 3, 4) 的三维数组，包含 24 个随机浮点数
# np.random.seed(2)           # 这个命令可以使下一次生成的随机数组保持固定，其中的参数为非负。

h = np.arange(10)
# print(h)       # >> [0 1 2 3 4 5 6 7 8 9]
i = h[h < 3]  # 可以筛选
# print(i)        # >> [0 1 2]
k = h[(h > 2) & (h % 2 == 0)]  # 另外，或运算符是“ | ”
# print(k)        # >> [4 6 8]

'''数据类型'''
# print(b.dtype)      # >> int32      在这个环境下，创建的整数数值的数组默认类型时32位整数
# print(c.dtype)      # >> float64    默认64位浮点数
l = np.array([1.0, 2.1, 3.2], dtype=np.int32)
# print(l)        # >> [1 2 3]
m = np.array([0, 1, 2, 3], dtype=np.str_)
# print(m)        # >> ['0' '1' '2' '3']
n = m.astype(bool)  # astype可以转换数据类型
# print(n)        # >> [False  True  True  True]

'''数组运算'''
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
a3 = np.array([1, 2, 3])
a4 = np.array([9, 8, 7, 6])
# 相同维度数组可以直接对同一位置的数值进行元素级别四则运算、幂运算、求余。如果维度不同，也有算的办法，这里不细究。
# print(a1 % a2)
b4 = np.sqrt(a1)  # 还可以开方
b5 = np.cos(a1)  # 以及进行三角函数运算
b6 = np.log(a4)  # 以及取对数，默认以自然数对数e为底数。需要自定义底数时，需要用换底公式
# print(b6)
b1 = np.dot(a1, a2)  # dot()对一维数组进行向量点积，对二维数组进行矩阵乘法(点乘)，这是线代中的概念。这个在机器学习中很关键
# print(b1)
b2 = a1 @ a2  # @可以对数组进行矩阵乘法(点成)运算
b3 = np.matmul(a1, a2)  # matmul()专门负责处理矩阵乘法，对数组格式有严格要求。在这里b1和b2和b3是等价的

'''切片用法'''
o = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(o[:, 1:])       # 运行一下看看就知道了，在这里的第一个冒号写与不写效果一样
# print(o[0:2, :])    # 0:2的意思是[0,2)

# print(h[0:9:2])     # 第三个数是跨度(Stride)   >> [0 2 4 6 8]
# print(h[9:0:-1])    # 跨度为负值时，可以倒序输出
# print(h[::-1])      # 这样写更简单
# print(a1[::-1])

