from io import StringIO

# 不带参数的StringIO构造函数
f = StringIO()
f.write('hello')
f.write(' wrold!')
print(f.getvalue())

# 带参数的StringIO构造函数
f1 = StringIO('Hello! \n Hi! \n Goodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

