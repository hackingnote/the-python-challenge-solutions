from urllib.request import urlopen
import png, re

response = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

(w, h, rgba, dummy) = png.Reader(response).read()

it = list(rgba)
mid = int(h / 2)
l = len(it[mid]) 
res = [chr(it[mid][i]) for i in range(0, l, 4*7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]
print("".join(map(chr, map(int, re.findall("\d+", "".join(res))))))
#print(l[0][int(h/2 * w)])
