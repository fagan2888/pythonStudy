import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists student (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# cursor.execute('insert into user (id, name) VALUES (%s, %s)', ['1', 'Michael'])
# print('cursor.rowcount:', cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user WHERE id=%s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

