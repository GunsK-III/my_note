# 参考 https://www.runoob.com/python/python-date-time.html
import time


def exs_tm01():
    """ 获取时间 """
    # Unix时间戳（UTC时间），表示从1970年1月1日00:00:00开始经过的秒数
    print("--- 当前时间戳 --- \n", time.time())

    # 将UTC时间戳转换为本地时间
    local_time_ = time.localtime(time.time())

    # 本地时间
    local_time = time.localtime()
    print("\n--- 本地时间信息元组 --- \n", local_time)

    # 时间格式化
    print("\n--- 时间格式化0 --- \n", time.asctime(local_time))
    # 格式化成 2016-03-20 11:45:39 形式
    print("\n--- 时间格式化1 ---\n", time.strftime("%Y-%m-%d %H:%M:%S", local_time))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print("\n--- 时间格式化2 ---\n", time.strftime("%a %b %d %H:%M:%S %Y", local_time))

    # 将格式字符串转换为时间戳
    time_ = "Sat Mar 28 22:24:24 2016"
    stamp = time.strptime(time_, "%a %b %d %H:%M:%S %Y")
    print("\n--- 时间信息元组 --- \n", stamp)
    mktime = time.mktime(stamp)
    print("\n--- 本地时间对应的时间戳 ---\n", mktime)

def exs_tm02():
    """ 设置延时 """
    print("开始计时...")
    for i in range(6):
        time.sleep(1)
        print(f"过了{i+1}秒...")
