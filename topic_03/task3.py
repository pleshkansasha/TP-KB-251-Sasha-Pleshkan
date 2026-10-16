animals = {"dog": 4, "cat": 4, "duck": 2}
animals.update({"cow": 4})
print(animals)
del animals["cat"]
print(animals)
print(animals.keys())
print(animals.values())
print(animals.items())
animals.clear()
print(animals)