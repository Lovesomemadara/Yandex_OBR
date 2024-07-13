products: list[str] = []
for _ in range(3):
    products.extend(input().split(', '))

products.sort()

for index, product in enumerate(products, start=1):
    print(f'{index}. {product}')
