cost = int(input("Enter bike cost:"))
if cost<=50000:
    x = cost * 5 /100
    print(x)
if cost>50000 and cost<=100000:
    r = cost * 10 /100
    print(r)
if cost >100000:
    m = cost * 15/100
    print(m)