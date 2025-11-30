""" time.perf_counter() 和 time.process_time() 是两个用于高精度时间测量的函数 """
import time
import math

def spend_time():
    # 一段CPU密集型计算
    for _ in range(1_000_000):
        math.sqrt(25)

    # 休眠一段时间
    time.sleep(1)

    # 再一段CPU密集型计算
    for _ in range(500_000):
        math.pow(2, 10)

""" 使用 time.perf_counter()
    它忠实地记录了从函数开始到结束在现实世界中流逝的总时间，其中包括了那1秒钟的睡眠。
    这是你作为一个用户会感知到的“程序运行了多久”。"""
start_perf = time.perf_counter()
spend_time()
end_perf = time.perf_counter()
elapsed_perf = end_perf - start_perf

""" 使用 time.process_time()
    它完全忽略了 time.sleep(1) 的那一秒钟，因为程序在睡眠时没有占用CPU。
    这个时间反映了你的程序真正在“干活”（计算） 的时长。
"""
start_proc = time.process_time()
spend_time()
end_proc = time.process_time()
elapsed_proc = end_proc - start_proc


print(f"perf_counter() 测量结果: {elapsed_perf:.4f} 秒")
print(f"process_time() 测量结果: {elapsed_proc:.4f} 秒")
# >> perf_counter() 测量结果: 1.1147 秒
# >> process_time() 测量结果: 0.0781 秒
