import itertools


# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算


# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
def use_count():
    natuals = itertools.count(1)
    for n in natuals:
        print(n)
        if n > 900:
            break


# cycle()会把传入的一个序列无限重复下去：
def use_cycle():
    cycle = itertools.cycle('ABC')
    for c in cycle:
        print(c)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
def use_repeat():
    repeat = itertools.repeat('ABC', 6)
    for r in repeat:
        print(r)


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
def use_takewhile():
    c = itertools.count(1)
    ns = itertools.takewhile(lambda x: x < 10, c)
    print(list(ns))


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
def use_chain():
    for i in itertools.chain('ABCDE', 'FGHIJ'):
        print(i)


def fliter_key(key):
    if isinstance(key, str):
        return '字母'
    elif isinstance(key, int):
        return '数字'
    else:
        return '未知'


# groupby()把迭代器中相邻的重复元素挑出来放在一起
def use_groupby():
    # 参数key用来重命名key的值
    for key, group in itertools.groupby(['A', 'A', 3, 3, 'B', 'B', 'C', 2, 2], key=fliter_key):
        print(key, list(group))


# 忽略大小写
def groupby():
    for key, group in itertools.groupby('AaaABBBBbCCCcCC', lambda x: x.upper()):
        print(key, list(group))


# use_takewhile()
# use_chain()
use_groupby()
groupby()