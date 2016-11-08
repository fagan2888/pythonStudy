# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
#
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
# 但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性。

import json

# 将dict序列化为json字符串
d = dict(name='Andrew', age=29, score=99)
jsonStr = json.dumps(d)
print('json字符串:', jsonStr)

# 将json字符串反序列化为python对象
d1 = json.loads(jsonStr)
print('python对象:', d1)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(student):
    return{
        'name':student.name,
        'age':student.age,
        'score':student.score
    }

s = Student('Andrew', 29, 99)
print('student2dit序列化获得json字符串:', json.dumps(s, default=student2dict, sort_keys=True))

jsonstr = json.dumps(s, default=lambda s: s.__dict__)
print('lambda根据对象__dict__序列化获得json字符串:', jsonstr)

def dict2student(dict):
    return Student(dict['name'], dict['age'], dict['score'])

print('反序列化：', json.loads(jsonstr, object_hook=dict2student))