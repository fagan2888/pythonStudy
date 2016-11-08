import os

def getOsName():
    s = os.name
    if s == 'nt':
        return 'Windows'
    elif s == 'posix':
        return 'Linux/Unix/Mac OS X'
        print('详细信息:', os.uname())

print('操作系统:', getOsName())
print('环境变量:', os.environ)
print('环境变量 PATH:', os.environ.get('PATH'))

# 查询当前目录
currentPath = os.path.abspath('.')
print('当前目录', currentPath)

# 在指定目录新建目录
testDir = os.path.join(currentPath, 'testCreateDir')
if os.path.exists(testDir) == False:
    print('新建目录', testDir)
    os.mkdir(testDir)
else: print(testDir, '目录已存在')

# 删除一个目录
os.rmdir(testDir)
print('删除目录', testDir)

# 拼接路径
joinPath = os.path.join(testDir, 'test.txt')
print(joinPath)

# 拆分路径获取最后一级文件名或目录
print(os.path.split(joinPath))

# 拆分路径获取文件扩展名
print(os.path.splitext(joinPath))

# 获取目录下所有子目录
print('当前目录：', os.getcwd())
print('当前目录父目录:', os.path.dirname(os.getcwd()))
listDir = os.listdir(os.path.dirname(os.getcwd()))
print('父目录下子目录及文件：', listDir)

# 当前目录所有子目录
s = [x for x in os.listdir('.') if os.path.isdir(x)]
print('当前目录所有子目录:', s)

# 当前目录下所有.py文件
s = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('当前目录下所有.py文件:', s)

def getAllDir(path):
    dirs = [x for x in os.listdir(path) if os.path.isdir(x)]
    print(dirs)
    if dirs != None:
        for dir in dirs:
            currentPath = os.path.join(path, dir)
            print(currentPath)
            getAllDir(currentPath)

# getAllDir(os.path.abspath('.'))

# 用os.walk方式获取所有目录
def getAllDirByOsWalk(directory):
    assert os.path.isdir(directory),'make sure directory argument should be a directory'
    result = []
    for root,dirs,files in os.walk(directory, topdown=True):
        for fl in dirs:
            fullpath = os.path.join(root, fl)
            result.append(fullpath)

    return result

abspath = os.path.abspath('.')
print(abspath, '所有子目录：\n', getAllDirByOsWalk(abspath))

# 递归获取所有子目录
def IterateDir_Recursion(directory):
    assert os.path.isdir(directory),'make sure directory argument should be a directory'

    def recuirfunc(dirs, result):
        if not dirs:
            return result

        temp = dirs.pop()
        for item in os.listdir(temp):
            path = os.path.join(temp, item)
            if os.path.isdir(path):
                dirs.append(path)
                result.append(path)
            else:
                pass

        recuirfunc(dirs, result)

    dirs = [directory]
    result = []
    recuirfunc(dirs, result)

    return result

abspath = os.path.abspath('.')
result = IterateDir_Recursion(abspath)
print(abspath, '所有子目录：\n', result)