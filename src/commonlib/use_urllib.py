import urllib
from urllib import request
from urllib import parse


# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
def open_url(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        print('Data:', data.decode('utf-8'))
        for key, value in f.getheaders():
            print('%s: %s' % (key, value))


# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页
def request_get(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# 以POST发送一个请求，只需要把参数data以bytes形式传入。
def request_post():
    print('Login to weibo.cn...')
    email = input('Email: ')
    pwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', pwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', 1),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'),
    ])
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status: ', f.status, f.reason)
        for key, value in f.getheaders():
            print('%s: %s' % (key, value))
        result = f.read().decode('utf-8')
        print('Data: ', result)
        response = eval(result)
        if response['retcode'] == 20000000:
            print('Login succseed.')
        else:
            print('Login failed, retcode:', response['retcode'])


# with proxy and proxy auth:
def proxy_handler():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


# open_url('https://api.douban.com/v2/book/2129650')

# request_get('http://www.douban.com/')

# request_post()

proxy_handler()
