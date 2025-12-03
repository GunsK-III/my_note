# 参考 https://www.cainiaojc.com/python/python-datetime.html
# datetime 模块用来处理日期和时间""
import datetime

def exs_dt01():
    cur = datetime.datetime.now()
    print("--- 当前的日期时间 ---\n", cur)

    cur_date = datetime.date.today()
    print("\n--- 当前日期 ---\n", cur_date)

    cur_time = datetime.time(11, 34, 56)
    print("\n--- 当前时间 ---\n", cur_time)
    # print(type(time_obj))     # >> <class 'datetime.time'>
    # 上面输出的三个值都是时间类型，下面把它转换为字符串

    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S") # 自定义格式
    cur_str2 = cur.strftime("%x")               # 日期格式
    cur_str3 = cur.strftime("%X")               # 时间格式

    print("\n--- 时间转换为字符串 ---",
          cur_str, cur_str2, cur_str3, sep="\n")
    # print(type(cur_str))      # >> <class 'str'>

