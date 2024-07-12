n: int = int(input())
products: list[str] = []
for _ in range(n):
    products.extend(item for item in input().split(', '))

sort_products: list[str] = sorted(products)

for i, product in enumerate(sort_products, 1):
    print(f'{i}. {product}')
