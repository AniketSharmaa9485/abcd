
'''ap = ["orange", "mango", "banana", "leachi"]
ap.sort()
print(ap)
ap = [100,900,89,72,98]
print(ap)
ap.sort(reverse=True)
print(ap)

thislist = ["Banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)

def myfunc(n):
    return abs(n -50)

thislist = [100 , 50 ,65 ,82,23]
thislist.sort(key =myfunc)
print(thislist)

#case senstive
nm = ["Orange", "Aango", "banana", "Ceachi"]
nm.sort()
print(nm)

nm = ["Orange", "Aango", "banana", "Ceachi"]
nm.sort(key = str.upper)
print(nm)

nm = ["Orange", "Aango", "banana", "Ceachi"]
nm.reverse()
print(nm)
'''
# copy list
ap = ["apple","banana","cherry"]
op = ap.copy()
print(op)

am = list(ap)
print(am)
ol = am[1:]
print(ol)

# join method

rp = ["a","n","i"]
op = ["k","e","t"]
for x in op:
    rp.append(x)
print(rp)
sp = ["a","n","i"]
up = ["k","e","t"]
sp.extend(up)
print(sp)