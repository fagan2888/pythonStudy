import re


# 校验电话号码
def checkPhoneNumber(phoneNumber):
    reg = r'\d{3}-\d{8}|\d{4}-\d{7}'
    if re.match(reg, phoneNumber):
        print('regx successed')
        return True
    else:
        print('regx failed')
        return False

checkPhoneNumber('029-83526469')
checkPhoneNumber('0916-83556565')

# 切分字符串
print(re.split(r'\s+', 'a b  c      d'))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


# 分组

# 根据电话号码获取区号
def getAreaCodeByPhoneNumber(phoneNumber):
    if checkPhoneNumber(phoneNumber):
        m = re.match(r'(\d{3})-(\d{8})', phoneNumber)
        if m:
            return m.group(1)

print(getAreaCodeByPhoneNumber('029-85656596'))


print(re.match(r'^(\d+?)(0*)$', '155500').groups())

# 邮箱校验
def matchEmail(email):
    if re.match(r'^(\w+[\w+.]?\w+)@{1}(\w+)\.{1}(\w+)$', email):
        print(email, 'is email')
    else:
        print(email, 'is not email')

matchEmail('someone@gmail.com')
matchEmail('bill.gates@microsoft.com')

Email = '<Tom Paris> tom@voyager.org'
re_Email = re.compile(r'^(<[a-zA-Z\.\s]{1,19}>)\s+(([0-9a-zA-Z\.]{1,19})\@[0-9a-z]{2,9}\.(com|org))$')
name = re_Email.match(Email).group(1)
email = re_Email.match(Email).group(2)
print("%s Email: %s" % (name, email))