import random as rd

# 随机生成的一个实数，它在[0,1)范围内
num_01 = rd.random()
print("#1. ", num_01)

# 随机生成一个实数，它在指定闭区间内[1,10]
num_02 = rd.uniform(1, 10)
num_03 = rd.uniform(10, 1)
print("#2. ", num_02, num_03)

# 随机生成一个整数，它在指定闭区间内
num_04 = rd.randint(1, 10)
print("#3. ", num_04)

# 随机选择
num_list1 = ['1', '2', '3', '4', '5']
print("#4. ", rd.choice(num_list1))

# 随机抽样，从列表中不重复地抽取k个元素，返回列表
num_list2 = [1, 2, 3, 4, 5]
print("#5. ", rd.sample(num_list2, 3))

# 随机排序
num_list3 = ['1', '2', '3', '4', '5']
rd.shuffle(num_list3)
print("#6. ", num_list3)

# 随机种子
# rd.seed(12345)  # 之后每次允许结果一样
print("#7. ", rd.randint(1, 100))

# 权重选择，参数 k 是抽取次数
num_list4 = ['No.1', 'No.2', 'No.3']
print("#8. ", rd.choices(num_list4, weights=[0.1, 0.3, 0.6], k=3))

# 正态分布
# 参数：均值(mu)和标准差(sigma)
heights = [int(rd.gauss(175, 5)) for _ in range(10)]
print("#9. ", heights)  # 大部分在170-180之间
