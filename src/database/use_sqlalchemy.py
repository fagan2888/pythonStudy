from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据连接,create_engine()用来初始化数据库连接
# SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
# 创建DBsession类型
DBsession = sessionmaker(bind=engine)

# 创建session对象
session = DBsession()
# 创建User对象
new_user = User(id='10', name='Tracy')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()


# 查询数据
session = DBsession()
# 创建query查询，filter是where条件，one()返回唯一行，all()返回所有行
user = session.query(User).filter(User.id == '5').one()
# 打印查询结果类型和name属性
print('type:', type(user))
print('name:', user.name)
session.close()
