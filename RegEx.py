import re
eg = "Hello Aniket sharma nice to meet you"
x = re.search("^hello.*you$",eg)

if x:
    print("Perfect")
else:
    print("you are done")

e = re.findall("ni",eg)
print(e)
if e:
    print("ok you got it")
else:
    print("Dumb")
m = re.sub("\s","9",eg)
print(m)