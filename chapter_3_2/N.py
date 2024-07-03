n: int = int(input())
available_ingredients: set[str] = {input() for _ in range(n)}

m: int = int(input())
recipes: list[tuple[str, set[str]]] = []
for _ in range(m):
    dish_name = input()
    num_ingredients = int(input())
    recipe_ingredients = {input() for _ in range(num_ingredients)}
    recipes.append((dish_name, recipe_ingredients))

available_dishes: list[str] = []
for dish_name, recipe_ingredients in recipes:
    if recipe_ingredients.issubset(available_ingredients):
        available_dishes.append(dish_name)

if available_dishes:
    print('\n'.join(sorted(available_dishes)))
else:
    print('Готовить нечего')

# -------------------------------------------

PRODUCTS = {input() for _ in range(int(input()))}

RECEPTES = {}
for _ in range(int(input())):
    dish_name = input()
    for _ in range(int(input())):
        RECEPTES[dish_name] = RECEPTES.get(dish_name, []) + [input()]

result = []
for dish_name, recept in RECEPTES.items():
    if set(recept) <= PRODUCTS:
        result.append(dish_name)

if result:
    print(*sorted(result), sep="\n")
else:
    print("Готовить нечего")
