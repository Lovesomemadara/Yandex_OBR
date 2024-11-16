class User:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.password = "12345"

        print(id(obj))

        return obj

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.__is_blocked = False

    def __str__(self) -> str:
        return f"ID: {id(self)}"


aleks = User("Алекс", "alex@site.com")

# print(id(aleks))
print(aleks.__dict__)
print(aleks)


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            obj = super().__new__(cls)

            cls.__obyekt = obj

        return cls.__instance


db_1 = DataBase()
db_2 = DataBase()
db_3 = DataBase()
db_4 = DataBase()

print(
    f"\nID-1: {id(db_1)}",
    f"\nID-2: {id(db_2)}",
    f"\nID-3: {id(db_3)}",
    f"\nID-4: {id(db_4)}",
)
