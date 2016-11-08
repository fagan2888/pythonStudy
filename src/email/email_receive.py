import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。
# 下面的代码我们偷了个懒，只取了第一个元素
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos > 0:
            charset = content_type[pos + 8:].strip()
    return charset


# indent用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(header)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if(msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % (' ' * indent, content_type))





# 输入邮件地址，口令和POP3服务器地址
# email = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server: ')

email = 'lufengdie@126.com'
password = 'lufeng19430413'
pop3_server = 'pop.126.com'

# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 可选，打印POP3服务器欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat 邮件数量和占用空间
print('Message: %s Size: %s' % server.stat())

# 返回所有邮件编号
resp, emails, octets = server.list()
# 可以查看列表，类似[b'18235', b'18236']
print(emails)

# 获取最新一封邮件，index从1开始
index = len(emails)
resp, lines, octets = server.retr(index)

# lines存储了邮件原始文件的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 稍候解析出邮件
msg = Parser().parsestr(msg_content)

print_info(msg, indent=1)

# 可以根据索引从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()
