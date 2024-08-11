from pprint import pprint
from sys import stdin, stdout, stderr


def custom_print(*args, sep=' ', end='\n'):
    output: str = sep.join(map(str, args)) + end
    stdout.write(output)


data: list[str] = stdin.readlines()
custom_print(*data)

data: dict = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "title2": "delectus aut autem",
    "title3": "delectus aut autem",
    "title4": "delectus aut autem",
    "title5": "delectus aut autem",
    "title6": "delectus aut autem",
    "title7": "delectus aut autem",
    "title8": "delectus aut autem",
    "completed": False
}

pprint(data)
