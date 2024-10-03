'''ab  = {"apple", "banana", "cherry","apple"}
print(len(ab))# unordered ,unchangeable ,no duplicate
ed = {"apple", "banana", "cherry", True ,1,2,0}
print(len(ed))
md = (("apple", "banana", "cherry", True ,1,2))
print(md)
# access set item
ob = {"brokli", "ladyfinger", "ginger"}
for c in ob:
    print(c)
print("ginger" in ob)
print("ladyfinger" not in ob)

ar = {"I", "speak", "english", "well"}
ra = {"kill", "the", "enimey"}
ar.update(ra)
print(ar)

kl = {"apple", "banana", "cherry"}
my = ["awosom", "wow", "great"]
kl.update(my)
print(kl)
'''
th = {"apple", "banana", "cherry"}
th.pop()
print(th)
th.clear()
del th
