n: int = int(input())
available_ingredients: set[str] = set(input() for _ in range(n))

m: int = int(input())
recipes: list[tuple[str, set[str]]] = []
for _ in range(m):
    dish_name = input()
    num_ingredients = int(input())
    recipe_ingredients = set(input() for _ in range(num_ingredients))
    recipes.append((dish_name, recipe_ingredients))

available_dishes: list[str] = []
for dish_name, recipe_ingredients in recipes:
    if recipe_ingredients.issubset(available_ingredients):
        available_dishes.append(dish_name)

if available_dishes:
    print('\n'.join(sorted(available_dishes)))
else:
    print('Готовить нечего')
