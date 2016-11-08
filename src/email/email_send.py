from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def build_msg(text, email_type):
    return MIMEText(text, email_type, 'utf-8')


def attach_image(msg):
    with open(r'C:\Users\YuanLiangFeng\Desktop\mvp.png', 'rb') as f:
        # 设置附件的MIME和文件名
        mime = MIMEBase('image', 'png', filename='mvp.png')
        # 添加头文件
        mime.add_header('Content-Disposition', 'attachment', filename='mvp.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件内容读进来
        mime.set_payload(f.read())
        # 用base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart中
        msg.attach(mime)


def build_multi_msg(text, email_type):
    msg = MIMEMultipart()
    msg.attach(MIMEText(text, email_type, 'utf-8'))
    attach_image(msg)
    return msg


def send_mail(msg):
    # 输入email和口令
    # from_addr = input('From: ')
    from_addr = '422258549@qq.com'
    # password = input('Password: ')
    # password = 'lufeng19430413'  # 126邮箱授权码
    password = 'xiqpxqlzvxflcbdf'  # QQ邮箱授权码
    # 输入收件人地址
    # to_addr = input('To: ')
    to_addr = 'lufengdie@126.com'
    # 输入SMTP服务器地址
    # smtp_server = input('SMTP server: ')
    smtp_server = 'smtp.qq.com'

    # 构造MIMEText对象时，第一个参数就是邮件正文，
    # 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
    # 最后一定要用utf-8编码保证多语言兼容性
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

    try:
        # SMTP协议默认端口是25
        server = smtplib.SMTP_SSL(smtp_server, 465)
        # 打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        # 登录SMTP服务器
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('发送失败：\n', e)

# 发送html正文邮件
# content = '<html><body><h1>Hello, lufeng</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
# email_type = 'html'
# email_msg = build_msg(content, email_type)

# 发送普通文本邮件
# content = 'Hello, send by python...'
# email_type = 'plain'
# email_msg = build_msg(content, email_type)

# 发送带附件(图片)邮件
# email_msg = build_multi_msg('send with file...', 'plain')

# 发送图片在正文显示邮件
content = '<html><body><h1>Hello, 良锋袁</h1><p><img scr="cid:0"></p></body></html>'
email_msg = build_multi_msg(content, 'html')

send_mail(email_msg)
