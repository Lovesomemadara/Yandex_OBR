from datetime import datetime

__all__ = ["BankAccount"]


class BankAccount:
    def __init__(self,
                 name: str,
                 age: int,
                 card_number: str,
                 phone_number: str) -> None:
        self.name = name
        self._age = age
        self.__phone_number = phone_number
        self.__card_number = card_number

    def __validate_phone_number(self, value) -> None:
        phone_len: tuple[int, int] = (11, 12)
        if not isinstance(value, str):
            raise ValueError

        if len(value) not in phone_len:
            raise ValueError

    @property  # Getter
    def phone_number(self) -> str:
        print(f"Пользователь {self.name} "
              f"получил свой номер телефона в {datetime.now()}")
        return self.__phone_number

    @phone_number.setter  # Setter
    def phone_number(self, new_value: str) -> None:
        self.__validate_phone_number(new_value)
        self.__phone_number = new_value


bank_account_1 = BankAccount(
    "Petya", 25, "43625****", "+791231234567"
)
print(bank_account_1.__dict__)
bank_account_1.card_number = "643235***"
bank_account_1.phone_number = "+79001234567"
print(bank_account_1.__dict__)

print(bank_account_1.phone_number)
