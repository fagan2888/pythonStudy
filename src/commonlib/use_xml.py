from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_elment: %s, attrs: %s' % (name, attrs))

    def end_element(self, name):
        print('sax: end_elment: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


def sax_paraser(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)


# 生成简单xml
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some  data')
L.append(r'</root>')
s = ''.join(L)

sax_paraser(xml)
sax_paraser(s)
