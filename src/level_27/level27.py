from PIL import Image
import bz2

im = Image.open('zigzag.gif')


palette = im.getpalette()[::3]

table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))

raw = im.tobytes()

trans = raw.translate(table)

zipped = list(zip(raw[1:], trans[:-1]))

diff = list(filter(lambda p: p[0] != p[1], zipped))

indices = [i for i,p in enumerate(zipped) if p[0] != p[1]]

im2 = Image.new("RGB", im.size)
colors = [(255, 255, 255)] * len(raw)
for i in indices:
    colors[i] = (0, 0, 0)
im2.putdata(colors)
#im2.show()


s = [t[0] for t in diff] 
text = bz2.decompress(bytes(s))

import keyword
print(set([w for w in text.split() if not keyword.iskeyword(w.decode())]))
