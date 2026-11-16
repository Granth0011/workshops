product=eval(input("Enter a list of products: "))
prices=eval(input("Enter a list of prices: "))
for i in range(len(product)):
    print(f"product: {product[i]}, price: {prices[i]:.2f}")
    