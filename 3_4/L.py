products: list[str] = []
for _ in range(int(input())):
    products.extend(input().split(', '))

products.sort()

for i, product in enumerate(products, start=1):
    print(f'{i}. {product}')
