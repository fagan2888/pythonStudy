from io import BytesIO

b = BytesIO()
b.write('你好吗？'.encode('utf-8'))
print(b.getvalue())