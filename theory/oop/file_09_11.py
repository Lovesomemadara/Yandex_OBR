# класс, сущность
class Cat:
    # атрибут, поле, свойство | класса
    LEGS: int = 4

    # конструктор, инициализатор, магический метод
    def __init__(self, name: str) -> None:
        # атрибут, поле, свойство | экземпляра
        self.name = name

    # Методы
    def voice(self) -> None:
        print("Meow")

    def jump(self) -> None:
        print("Jump")

    # classmethod
    # staticmethod
    # magic methods

    # Переопределение методов
    def __repr__(self) -> str:
        return f"{id(self)}"

    def __str__(self) -> str:
        return f"Кличка: {self.name}"


# экземпляр, объект

vasya = Cat("Вася")
vasya.voice()
print(vasya.__dict__)

murka = Cat("Мурка")
murka.voice()
print(murka.__dict__)

print(vasya)
