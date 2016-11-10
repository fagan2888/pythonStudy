from sqlalchemy import Column, String, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 一对多关系


import mysql.connector

# 创建表
conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists classroom (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
cursor.execute('create table if not exists teacher (id VARCHAR(20) PRIMARY KEY, name VARCHAR(10), subject VARCHAR(10), class_id VARCHAR(20))')


# 创建对象基类
Base = declarative_base()


# 班级
class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    teacher = relationship('Teacher')

    def __repr__(self):
        return '<User: (id: %s, name: %s, teacher: %s)>' % (self.id, self.name, self.teacher)


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(String(20), primary_key=True)
    name = Column(String(10))
    subject = Column(String(10))

    # "多"的一方teacher表是通过外键关联到class表
    class_id = Column(String(20), ForeignKey('classroom.id'))

    def __repr__(self):
        return '<Teacher: (id: %s, name: %s, subject: %s, class_id: %s)>' % (self.id, self.name, self.subject, self.class_id)


# 多次插入方式
def insert_multiple():
    new_class = Classroom(id='1', name='三年二班')
    session.add(new_class)
    session.commit()

    math_teacher = Teacher(id='1', name='李志', class_id='1', subject='数学')
    chiese_teacher = Teacher(id='2', name='赵雷', class_id='1', subject='语文')
    session.add_all([math_teacher, chiese_teacher])
    session.commit()


# 一次插入方式
def insert_once():
    math_teacher = Teacher(id='1', name='李志', class_id='1', subject='数学')
    chiese_teacher = Teacher(id='2', name='赵雷', class_id='1', subject='语文')
    new_class = Classroom(id='1', name='三年二班', teacher=[math_teacher, chiese_teacher])
    session.add(new_class)
    session.commit()


# 初始化数据连接,create_engine()用来初始化数据库连接
# SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
DBsession = sessionmaker(bind=engine)
session = DBsession()

insert_once()

result = session.query(Classroom).filter(Classroom.id == '1').all()
print(result)
