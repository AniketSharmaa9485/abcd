cars = ["mercdies", "ford", "alto", "maruti"]
x = len(cars)
for i in cars:
    print(i)
print(x)
cars.append("honda")
cars.pop(1)
print(cars)
cars.remove("honda")
print(cars)