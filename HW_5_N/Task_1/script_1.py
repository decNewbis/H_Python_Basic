import uuid

from datetime import datetime as dt

from HW_5_N.Task_1.hw_data import *


class CustomUserMixin:
    def __init__(self, name: str, surname: str, age: int):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(age, int):
            raise TypeError("Expected types: name: str, surname: str, age: int")
        self.name = name
        self.surname = surname
        self.age = age
        self._user_id = uuid.uuid4()
        self._join_date = dt.now().strftime("%d.%m.%Y")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id_):
        raise AttributeError(f"can\'t set attribute")

    @property
    def join_date(self):
        return self._join_date

    @join_date.setter
    def join_date(self, join_date_):
        raise AttributeError(f"can\'t set attribute")

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'Користувач id: {self.user_id}'


class Member(CustomUserMixin):
    def change_name(self, new_name: str):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise TypeError("Expected type 'str'")

    def change_surname(self, new_surname: str):
        if isinstance(new_surname, str):
            self.surname = new_surname
        else:
            raise TypeError("Expected type 'str'")

    def change_age(self, new_age: int):
        if isinstance(new_age, int):
            self.age = new_age
        else:
            raise TypeError("Expected type 'int'")


class Moderator(Member):
    def __init__(self, name, surname, age):
        super(Moderator, self).__init__(name, surname, age)
        self.badge = 'Moderator'

    def change_badge(self, new_badge: str):
        if self.__dict__.get('badge') is not None:
            if isinstance(new_badge, str):
                self.badge = new_badge
            else:
                raise TypeError("Expected type 'str'")
        else:
            raise NoAccess(f"{self.full_name}")


class Admin(Moderator):
    def __init__(self, name, surname, age, level=1):
        super(Admin, self).__init__(name, surname, age)
        if not isinstance(level, int):
            raise TypeError("Expected types: name: str, surname: str, age: int, level: int")
        self.badge = 'Admin'
        self.level = level

    def change_level(self, new_level: int):
        if self.__dict__.get('badge') == 'Admin':
            if isinstance(new_level, int):
                self.level = new_level
            else:
                raise TypeError("Expected type 'int'")
        else:
            raise NoAccess(f"{self.full_name}")
