from PIL import Image
import math

im = Image.open('beer2.png')

data = list(im.getdata())

out = None

for i in range(33):
    max_value = max(data)
    data = [x for x in data if x < max_value - 1]
    print(len(data))
    l = int(math.sqrt(len(data)))
    out = Image.new('L', (l, l))
    out.putdata(data)
    out.show()
