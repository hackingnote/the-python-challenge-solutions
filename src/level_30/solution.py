from PIL import Image
import math

with open('yankeedoodle.csv') as f:
    data = [x.strip() for x in f.read().split(",")]
    length = len(data)
    print(length)
    # 7367

    factors = [x for x in range(2, length) if length % x == 0]
    print(factors)
    # [53, 139]

    img = Image.new("F", (53, 139))
    img.putdata([float(x) for x in data], 256)

    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.ROTATE_90)
    #img.show()
    
    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])])

    print(res)
