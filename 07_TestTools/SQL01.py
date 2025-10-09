import pymysql


def get_conn():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='your_database'
    )
    return connection


def query1():
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            # 执行SQL查询
            sql = "SELECT * FROM your_table"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()


query1()

# with pymysql.connect(
#     host='localhost',
#     user='root',
#     password='your_password',
#     database='your_database'
# ) as connection:
#
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM your_table"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
