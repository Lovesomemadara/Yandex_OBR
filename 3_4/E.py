products: list[str] = []
for _ in range(3):
    products.extend(item for item in input().split(', '))

all_products: list[str] = sorted(products)

for index, product in enumerate(all_products, 1):
    print(f'{index}. {product}')
