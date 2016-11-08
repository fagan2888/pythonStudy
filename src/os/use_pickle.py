import pickle

# 转成byte
d = dict(name='Andrew', age=29, score=99)
print('byte格式：', pickle.dumps(d))

# dump写入到文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# dumps从文件中读取
f = open('dump.txt', 'rb')
d1 = pickle.load(f)
print(d1)
f.close()