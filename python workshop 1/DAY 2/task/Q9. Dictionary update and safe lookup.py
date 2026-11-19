prices = {'pen': 10, 'pencil': 5, 'book': 60}
print("Pen:", prices.get('pen', 'Item not found'))
print("Eraser:", prices.get('eraser', 'Item not found'))
prices.update({'book': 65})
prices.setdefault('notebook', 40)
for item, price in prices.items():
    print(item, price)
