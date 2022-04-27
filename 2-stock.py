data = input().split(' ')
stock = {}
products = input().split(' ')

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i+1])
    stock[food] = quantity

for product in products:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
