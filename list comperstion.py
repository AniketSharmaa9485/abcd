#comprehention
ap = ["rahul", "chamun", "ramun" ,"nawab"]
rp = []
for x in ap:
    if "u" in x:
        rp.append(x)
print(rp)

op = ["soo", "loo", "moo"]
sp = [x for x in op if "l" in x]
print(sp)

sp = [ x for x in op if x!= "soo"]
print(sp)


sp = [ x for x in op]
print(sp)


sp = [ x for x in range(3) if x>0]
print(sp)


sp = [ x.upper() for x in op]
print(sp)