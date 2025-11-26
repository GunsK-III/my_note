"""with()除了能够用于文件，还有很多应用场景"""

def exs01():
    """可以连接数据库等中间件，结束抽自动关闭"""
    import sqlite3

    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()


def exs02():
    """可以线程锁"""
    import threading

    lock = threading.Lock()

    with lock:
        # 临界区代码
        print("这段代码是线程安全的")


def exs03():
    """可以临时修改系统状态"""
    import decimal

    with decimal.localcontext() as ctx:
        ctx.prec = 42  # 临时设置高精度
        # 执行高精度计算
    # 精度恢复原设置
