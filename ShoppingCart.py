products = []
prices = []

while True:
    product = input('Enter product name or Q to quit: ')
    if product.lower() == 'q':   # check user input, not the list
        break
    else:
        price = float(input('Enter product price: '))
        prices.append(price)
        products.append(product)

print("\n----- Your Cart -----")
for i in range(len(products)):
    print(f"{products[i]} --- {prices[i]}")

total = sum(prices)
print(f"\nTotal Price: {total}")
