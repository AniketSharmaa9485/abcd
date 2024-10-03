'''
x = lambda a,b : a*b
print(x(5,6))
x = lambda a,b,c : a+b+c
print(x(5,6,8))
x= lambda a,o,r :a-o+r
print(x(3,3,9))

def myfunc(n):
    return lambda a: a*n
x = myfunc(4)
print(x(20))
'''
def myhon(n):
    return lambda a : a*n
ob = myhon(4)
rj = myhon(6)

print(ob(10))
print(rj(10))