import asyncio


@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用 asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again!')


# 获取Eventloop
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()



