# I/O操作


# 一次性读取文件
def read(path):
    with open(path, 'r') as f:
        print(f.read())

# readline()循环读取文件
def loop_read(path):
    f = None
    try:
        f = open(path, 'r') # 打开文件
        for line in f.readlines(): # 循环读取每行文本
            print(line.strip())     # 打印删除过末尾的'\n'的文本
    except Exception as e:
        print('Something is wrong:', e.args)
    finally:
        if f != None:
            f.close()

# 读取二进制文件
def read_binary_file(path):
    f = None
    try:
        f = open(path, 'rb')
        print(f.read())
    except Exception as e:
        print('Something is wrong:', e.args)
    finally:
        if f != None:
            f.close()

# 以指定编码格式读取文件
def read_encoding(path, encoding):
    f = None
    try:
        f = open(path, 'r', encoding=encoding, errors='ignore')
        print(f.read())
    except Exception as e:
        print('Something is wrong:', e.args)
    finally:
        if f != None:
            f.close()

# 写入文件
def write_to_file(path):
    f = None
    try:
        # 'w'表示可写
        f = open(path, 'w', encoding='gb2312', errors='ignore')
        f.write('备注：write something by \'write_to_file\' method...')

        # 读取文件内容
        f = open(path, 'r', encoding='gb2312', errors='ignore')
        print(f.read())
    except Exception as e:
        print('Something is wrong:', e.args)
    finally:
        if f != None:
            f.close()

# with as 方式写入文件
def write_to_file_with_as(path):
    with open(path, 'w') as f:
        f.write('备注：write something by \'write_to_file_with_as\' method...')

# read('test.py')
#
# loop_read('tes.py')
#
# read_binary_file('../res/mvp.png')
#
# read_encoding('../res/gb2312.txt', 'gb2312')
#
# write_to_file('../res/gb2312.txt')

write_to_file_with_as('../res/gb2312.txt')
