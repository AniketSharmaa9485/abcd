ab = ("apple", "banana", "cherry")#allow duplicate ,ordered,unchangeable
print(ab)
print(len(ab))
thistuple = ("apple",)
print(type(thistuple))

#change tuple value
am  =  ("aman", "hanuman", "yoyo")
ji = list(am)
ji.append("honeysingh")
am = tuple(ji)
print(am)
ab+=am
print(ab)

# asterisk
aman = ("arun", "rahul", "Monika", "Shaurab")
(abaa , dabba ,*jabaa) = aman
print(abaa)
print(dabba)
print(jabaa)
arnav = aman*2
print(arnav)

AB = ("apple", "banana", "cherry")
mp = list(AB)
mp.append("orange")
mp.remove("cherry")
AB = tuple(mp)
print(AB)