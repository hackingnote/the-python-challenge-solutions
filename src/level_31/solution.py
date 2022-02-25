from PIL import Image

img = Image.open("mandelbrot.gif")

left = 0.34
bottom = 0.57
width = 0.036
height = 0.027
max = 128

w, h = img.size

xstep = width / w
ystep = height/ h

result = []

for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(left + x * xstep, bottom + y * ystep)
        z = 0 + 0j
        for i in range(max):
            z = z * z + c
            if abs(z) > 2: 
                break
        result.append(i)

img2 = img.copy()
img2.putdata(result)
img2.show()

diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
print(len(diff))

plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in diff])
plot.resize((230,730)).show()
