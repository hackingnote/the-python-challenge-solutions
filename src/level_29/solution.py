from urllib.request import Request, urlopen
import bz2, base64

req = Request('http://www.pythonchallenge.com/pc/ring/guido.html')
req.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
raw = urlopen(req).read().splitlines()[12:]
data = bytes([len(i) for i in raw])
print(bz2.decompress(data))

