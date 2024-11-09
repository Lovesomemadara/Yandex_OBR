from abc import ABC, abstractmethod

# Абстракция
class BaseHouse(ABC):
    foundament: bool = True

    @abstractmethod
    def door(self):
        raise NotImplementedError


# Наследование
class House(BaseHouse):
    pass

class SmallHouse(House):
    pass


h1 = House()

print(h1)
