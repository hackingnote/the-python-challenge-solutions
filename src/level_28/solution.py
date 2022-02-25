from PIL import Image

im = Image.open('bell.png')

# split RGB and get Green
green = list(im.split()[1].getdata())

# calculate diff for every two bytes
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]

# remove the most frequent value 42
filtered = list(filter(lambda x: x != 42, diff))

# convert to string and print out
print(bytes(filtered).decode())

