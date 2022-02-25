import zipfile, re

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))

num = '90052'

comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)    
    match = re.search("Next nothing is (\d+)", content)    
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
