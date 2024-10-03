'''a = "boolloo"
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
'''
class abc:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a+=1
            return x
        else:
            print("Not understand")

    obj = abc()
    myiter = iter(obj)

    for x in myiter:
        print(x)