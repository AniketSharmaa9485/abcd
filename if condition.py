'''a = 20
v = 400
if a<v:
    print("you know condition")
elif a>v:
    print("you don't know ")
else:
    print("you are fool")
print("A") if a<v else print("=") if a==b else print("B")

# while loop
i = 1
while i > 0:
    break
    print(i)
    i+=1

x= 1
while x < 15:
    print(x)
    if x < 9:
        print("Namskar")
    x+=1

i = 1
while i < 6:
    print(i)
    i +=1
    continue
else:
    print("i is no longer less than 6")
'''

for x in range(2,303,100):
    print(x)
else:
    print("Finished")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally Finished")

adj = ["red", "bnanan", "tasty"]
ob =  ["ooo", "haa", "fff"]

for x in ob:
    for y in adj:
        print(x,y)