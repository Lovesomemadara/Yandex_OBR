class Employee:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Я сотрудник {self.name}"

    def info(self) -> None:
        print(f"{self.name}")


class Developer(Employee):
    # def __str__(self):
    #     return f"Я разработчик {self.name}"

    def __str__(self):
        return super().__str__() + " разработчик"


class PythonDeveloper(Developer):
    def __str__(self):
        return super().__str__() + " Python"


class JavaDeveloper(Developer):
    pass


employee = Employee("Макс")
py_dev = PythonDeveloper("Алекс")

employee.info()
print(employee)
print(py_dev)
