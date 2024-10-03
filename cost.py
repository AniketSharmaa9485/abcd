def spaceremover(a):
    r = ""
    for x in a:
        if x!=" ":
            r += x
    return r


a = " hello how are you "
x=spaceremover(a)
print(x)