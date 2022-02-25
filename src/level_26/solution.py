import hashlib

def search_and_save():
    for i in range(len(data)):
        for j in range(256):
            newData = data[:i] + bytes([j]) + data[i + 1:]
            if hashlib.md5(newData).hexdigest() == md5code:
                open('repaired.zip', 'wb').write(newData)
                return   
 
md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open('maze/mybroken.zip', 'rb').read()
search_and_save()
