from urllib.request import urlopen
import pickle

h = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(h)

for line in data:
    print("".join([k * v for k, v in line]))
