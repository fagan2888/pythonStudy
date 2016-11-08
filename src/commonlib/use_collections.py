
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

from collections import namedtuple
Point = namedtuple('Point', field_names=['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

Test = namedtuple('Test', field_names=('test', 'name'))
test = Test('It\'s me', 'Andrew')
print('%s, My name is %s' % (test.test, test.name))


# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

from collections import deque

q = deque(['a', 'b', 'c', 'd', 'e', 'f'])
q.append('g')
q.appendleft('0')
print(q)


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict

d = defaultdict(lambda: 'N/A')
d['key1'] = 'abc'
print(d['key1'])  # key1存在
print(d['key2'])  # key2不存在返回默认值


# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print('无序dict: %s' % d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('有序OrderedDict: %s' % od)

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od1 = OrderedDict()
od1['x'] = 1
od1['y'] = 2
od1['z'] = 3
print(list(od1.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity): # capacity 容量
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        # key是否已存在，1表示已存在，0表示不存在
        containsKey = 1 if key in self else 0
        # 容量已满则移除最早添加的key
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        # key已存在则移除
        if containsKey:
            del self[key]
            print('set :', (key, value))
        else:
            print('add:', (key, value))
        # 设置键值对，上个if else都执行该行
        OrderedDict.__setitem__(self, key, value)

lastDict = LastUpdateOrderedDict(2)
lastDict['1'] = 'a'
lastDict['2'] = 'b'
print(lastDict)
lastDict['3'] = 'a'
print(lastDict)
lastDict['3'] = 'c'
print(lastDict)


# Counter是一个简单的计数器

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)