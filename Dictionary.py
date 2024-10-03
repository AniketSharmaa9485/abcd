'''cars = {
    "brand": "ford",
    "model": "Mustang",
     "year": 1964}
print(cars)
#dictionary item
cars = {
    "brand": "ford",
    "model": "Mustang",
     "year": 1964}
print(cars["brand"])
#duplicate not allowed
cars = {
    "brand": "ford",
    "model": "Mustang",
     "year": 1964,
     "year": 2020
    }
print(len(cars))
#Dictionary item - Data type
cars = {
    "brand": "ford",
    "model": "Mustang",
     "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(type(cars))
#The dict() Constructor
ob = dict(name = "hont", age = 36, country = "norway")
print(ob)
'''
ob = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964,

}
x = ob.items()
print(x) #befor
ob["color"] = "black"
print(x) #after
# condition
if "model" in ob:
    print("yes")
if "ford" in ob:
    print("yes")
ob["brand"] = "Nano"
print(ob)
ob.update({"year": 2024})
print(ob)
ob.pop("model")
print(ob)
del ob["color"]
print(ob)
