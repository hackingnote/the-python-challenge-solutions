import urllib.request, base64, re

request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
cred = base64.b64encode(b"butter:fly")
request.add_header("Authorization", "Basic %s" % cred.decode())
#print(request.headers)
response = urllib.request.urlopen(request)

pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
content_range = response.headers['content-range']
(start, end, length) = pattern.search(content_range).groups()

while True:
    try:
        request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)
#        print(request.headers)
        response = urllib.request.urlopen(request)
#        print(response.read().decode())
#        print(response.headers)
        (start, end, length) = pattern.search(response.headers['content-range']).groups()
    except: 
        break 

request.headers['Range'] = 'bytes=%i-' % (int(length) + 1)
print(request.headers)
response = urllib.request.urlopen(request)
print(response.headers)
print(response.read().decode())



request.headers['Range'] = 'bytes=2123456743-'
response = urllib.request.urlopen(request)
print(response.headers)
print(response.read().decode())

request.headers['Range'] = 'bytes=1152983631-'
response = urllib.request.urlopen(request)

with open("level21.zip", "wb") as f:
    f.write(response.read())
