from multiprocessing import Process, Queue

import os, time, random

#  写数据进程执行的代码
def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to quese...' % value)
        q.put(value)
        time.sleep(random.random() * 5)

# 读数据进程执行的代码
def read(q):
    print('Procee to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from quese.' % value)

if __name__ == '__main__':
    # 父进程创建Quese, 并传给子进程
    q = Queue()
    readProcess = Process(target=read, args=(q,))
    writeProcess = Process(target=write, args=(q,))
    # 启动readProcess
    readProcess.start()
    # 启动writeProcess
    writeProcess.start()
    # 等待writeProcess结束
    writeProcess.join()
    # readProcess进程中是死循环，无法等待自动结束，只能手动终止
    readProcess.terminate()
    print('All subprocess done.')

