a = ["orange", "banana", "cherry"]
for x in range(len(a)):
    print(x)
ide = 0
while ide < len(a):
    print(a[ide])
    ide = ide + 1
[print(x) for x in a]
r = ("ammar", "antham", "anthani")
for i in range(len(r)):
    print(i)
for i in r:
    print(i)
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)
for x,y in thisdict.items():
    print(x,y)