

Capitals = { "Usa": "Washington D.C",
             "Germany": "Berlin",
             "Pakistan": "Islamabad",
             "Russia": "Moscow",
             "Japan": "Tokyo"}

print(Capitals)
print(Capitals.get("Usa"))
print(Capitals.get("Germany"))
print(Capitals.get("Pakistan"))
print(Capitals.get("Russia"))
print(Capitals.get("Japan"))
Capitals.update({"Usa" : "New York"})
Capitals.update({"China" : "Bejing"})
print(Capitals)
Capitals.pop("Russia")
print(Capitals)
Capitals.popitem()
# Capitals.clear()
print(Capitals)

keys = Capitals.keys()
values = Capitals.values()
print(keys)
print(values)

for key in Capitals.keys:
    print(key)
