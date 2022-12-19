import pymysql
# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT * from login")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print(data)
# 关闭数据库连接
cursor.close()


