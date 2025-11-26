import pandas as pd
import numpy as np

file_path = r"D:\NewFolder\Py_Folder\files2\Odds_456654.xlsx"

df = pd.read_excel(file_path)

# print(df.head(2))         # 前两行
# print(df.shape)           # 形状
# print(df.info)            # 数据类型
# print(df.describe())      # 描述性统计信息
# print(df['获胜选手'])       # 列

# col_1 = df.columns.values     # 调出所有列名，并转换为数组
# print(col_1)
# df.columns = [x.strip() for x in col_1]      # strip()可以去空格，用这个列表推导式可以去前、后空格


'''重复值'''
# print(df.duplicated())      # 检查是否有重复值 后面的条目在重复值判断中显示为True
# 从前向后，若第二行数据和第一行一样，将第二行数据判断为重复
# 从后向前，则将第一行数据判断为重复。
# print(df[df.duplicated()])     # 可以在df[]中输入Bool值，来确定到行
# df.drop_duplicates(inplace=False)    # 删除重复值, inplace=True表示直接修改df原文件。

'''异常值'''

