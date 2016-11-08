import time, threading

# 假设这是你的银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

# 不加锁可能会出现balance结果不为0
def run_thread(n):
    for i in range(1000000):
        change_it(n)

# 加锁线程保证balance永远为0
def run_thread_lock(n):
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()

def test(fuc):
    t1 = threading.Thread(target=fuc, args=(5,), name='first')
    t2 = threading.Thread(target=fuc, args=(8,), name='second')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(fuc.__name__, ' result: ', balance)

# 测试不加锁
# test(run_thread)

# 测试加锁
test(run_thread_lock)