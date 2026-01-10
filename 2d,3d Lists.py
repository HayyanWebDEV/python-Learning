
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["celery", "onion", "cabagge"]
# meats = ["Chiken", "fish", "turkey"]
#
# groceries = [fruits, vegetables, meats]

groceries = [
    ["apple", "banana","mango"],
    ["cucumber", "Cabbage", "celery"],
    ["chicken", "turkey", "fish"]
]
print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])

for collection in groceries:
    print(collection)

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()