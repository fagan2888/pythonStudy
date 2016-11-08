
from urllib import request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    bool_title = False
    bool_time = False
    bool_place = False
    bool_miss = True

    def __init__(self):
        HTMLParser.__init__(self)
        self.message = []

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            if tag == "h3" and attrs[0][1] == "event-title":
                self.bool_title = True
            elif tag == "time" and attrs[0][0] == "datetime":
                self.bool_time = True
            elif tag == "span" and attrs[0][1] == "event-location":
                self.bool_place = True
            elif tag == "h3" and attrs[0][1] == "widget-title just-missed":
                self.bool_miss = False

    def handle_data(self, data):
        if self.bool_title and self.bool_miss:
            self.message.append([])
            self.message[-1].append(data)
            self.bool_title = False

        if self.bool_time and self.bool_miss:
            self.message[-1].append(data)
            self.bool_time = False

        if self.bool_place and self.bool_miss:
            self.message[-1].append(data)
            self.bool_place = False


def homework():
    parser = MyHTMLParser()
    with request.urlopen('http://www.python.org/events/python-events') as f:
        html = f.read().decode('utf-8')
    parser.feed(html)
    a = parser.message
    for x in a:
        print("=====================================")
        print("会议名：%s   会议时间：%s   会议地点：%s" % (x[0], x[1], x[2]))

if __name__ == "__main__":
    homework()
