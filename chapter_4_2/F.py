in_stock: dict[str, int] = {'coffee': 0, 'milk': 0, 'cream': 0}


def order(*preferences):
    recipes: dict[str, dict[str, int]] = {
        'Эспрессо': {
            'coffee': 1
        },
        'Капучино': {
            'coffee': 1, 'milk': 3
        },
        'Макиато': {
            'coffee': 2, 'milk': 1
        },
        'Кофе по-венски': {
            'coffee': 1, 'cream': 2
        },
        'Латте Макиато': {
            'coffee': 1, 'milk': 2, 'cream': 1
        },
        'Кон Панна': {
            'coffee': 1, 'cream': 1
        }
    }

    for drink in preferences:
        if drink in recipes:
            recipe: dict[str, int] = recipes[drink]
            if all(
                    in_stock.get(ing, 0) >= amt
                    for ing, amt in recipe.items()
            ):
                for ing, amt in recipe.items():
                    in_stock[ing] -= amt
                return drink
    return 'К сожалению, не можем предложить Вам напиток'


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
