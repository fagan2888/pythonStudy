import sqlite3


def init_table():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建
    conn = sqlite3.connect('test.db')
    # 创建cursor
    cursor = conn.cursor()
    # 执行一条sql语句，创建表
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR (20) PRIMARY KEY, name VARCHAR (20))')
    # 继续执行SQL语句，插入一条记录
    cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')
    # 通过rowcount获取插入行数
    cursor.rowcount
    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭connection
    conn.close()


def show_all():
    conn = sqlite3.connect('test.db')
    # 创建cursor
    cursor = conn.cursor()
    # 继续执行SQL语句，插入一条记录
    cursor.execute('SELECT * FROM user')
    # 获取查询结果集
    values = cursor.fetchall()

    print(values)
    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭connection
    conn.close()


show_all()
