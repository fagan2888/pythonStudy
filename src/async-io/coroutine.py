
def consumer():
    r = ''
    while True:
        n = yield r
        print(n)
        if not n:
            return
        print('[CONSUMER] Cunsuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None) # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return %s' % r)
    c.close()

c = consumer()
produce(c)

