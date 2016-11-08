import base64

b = base64.b64encode(b'binary\x00string')
print(b)

db = base64.b64decode(b)
print(db)

bs = base64.encodebytes(b'test')
print(bs)

print(base64.decodebytes(bs))