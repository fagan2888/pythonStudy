import hashlib

s = 'Andrew'
md5 = hashlib.md5()
md5.update(s.encode('utf-8'))
print('%s md5加密：%s' % (s, md5.hexdigest()))

b = b'Andrew'
md5_1 = hashlib.md5()
md5_1.update(b)
print('%s md5加密：%s' % (b, md5.hexdigest()))
print('md5加密后长度：%s' % len(md5.hexdigest()))

sha1 = hashlib.sha1()
sha1.update(b)
print('%s sha1加密：%s' % (b, sha1.hexdigest()))
print('sha1加密后长度：%s' % len(sha1.hexdigest()))


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


# 校验用户名密码
def check(user, password):
    if user == '':
        print('用户名不能为空')
        return False
    elif password == '':
        print('密码不能为空')
        return False
    return True


def login(user, password):
    if check(user, password) is False:
        return
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_password = md5.hexdigest()
    if user in db:
        if db[user] == md5_password:
            return True
        else:
            print('密码错误')
    else:
        print('用户不存在')
    return False

if login('', '123456'):
    print('登录成功')
