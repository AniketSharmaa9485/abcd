'''aniket = [ "Bca", "IITM", "Cyberhorizon", "Ace"]
print(aniket)
# constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# indexing
ap = ["robin", "jack" ,"rohan"]
print(ap[1])
if "rohan" in ap:
    print("Yes i understand list")
#changle able item
ap[2] = "moniho"
print(ap)
ap[2:4] = ["aniket"]
print(ap)

#extent
ap.extend(aniket)
print(ap)
ap.insert(3,"namskar")
print(ap)
ap.append("OMnamshivaya")
print(ap)
ap.remove("IITM")
print(ap)
ap.pop(3)
print(ap)
del ap[0]
print(ap)
ap.clear()
print(ap)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)
'''

