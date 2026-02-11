from typing import Union, List, Optional
from abc import ABC, abstractmethod


class Glass:
    def __init__(self, capaci: Union[int, float], occupi: Union[int, float]):
        if not isinstance(capaci, (int, float)):
            raise TypeError
        if not capaci > 0:
            raise ValueError
        self.capaci = capaci

        if not isinstance(occupi, (int, float)):
            raise TypeError
        if occupi < 0:
            raise ValueError
        if occupi > capaci:
            raise ValueError
        self.occupi = occupi

    def add_water(self, volume: Union[int, float]) -> None:
        if not isinstance(volume, (int, float)):
            raise TypeError
        if volume < 0:
            raise ValueError
        if self.occupi + volume > self.capaci:
            raise ValueError(f"Максимум добавить {self.capaci - self.occupi}")
        self.occupi += volume

    def get_free_space(self) -> Union[int, float]:
        return self.capaci - self.occupi


class Book:
    """Класс книги"""

    def __init__(self, ti: str, au: str, pa: int):
        """
        >>> book = Book("2005", "Иванов Иван", 230)
        >>> book.ti
        '2005'
        """
        if not isinstance(ti, str):
            raise TypeError
        if not isinstance(au, str):
            raise TypeError
        if not isinstance(pa, int) or pa <= 0:
            raise ValueError

        self.ti = ti
        self.au = au
        self.pa = pa
        self.current_page = 1
        self.bookmarks = []

    def open_page(self, page: int) -> str:
        """
        Открыть страницу

        :param page: Страницы
        :return: Информация о странице

        >>> book = Book("2005", "Иванов Иван", 230)
        >>> book.open_page(10)
        'Открыта страница 10'
        """
        if page < 1 or page > self.pa:
            raise ValueError(f"Страница от 1 до {self.pa}")
        self.current_page = page
        return f"Открыта страница {page}"

    def add_bookmark(self, page: int, note: str = "") -> None:
        """Закладку"""
        if page < 1 or page > self.pa:
            raise ValueError(f"Страница от 1 до {self.pa}")
        self.bookmarks.append({"page": page, "note": note})


class Smartphone:
    """Класс для телефона"""

    def __init__(self, br: str, mo: str, bat: int):
        """
        >>> phone = Smartphone("Samsung", "Galaks 11", 3000)
        >>> phone.br
        'Samsung'
        """
        if not isinstance(br, str):
            raise TypeError
        if not isinstance(mo, str):
            raise TypeError
        if not isinstance(bat, int) or bat <= 0:
            raise ValueError

        self.br = br
        self.mo = mo
        self.battery_capacity = bat
        self.battery_level = 100
        self.apps = []

    def charge(self, minutes: int) -> int:
        """
        Зарядка телефона

        :param minutes: Время зарядки
        :return: Заряд

        >>> phone = Smartphone("Samsung", "Galaks 11", 3000)
        >>> phone.charge(30)
        100
        """
        if minutes < 0:
            raise ValueError
        self.battery_level = min(100, self.battery_level + minutes // 2)
        return self.battery_level

    def install_app(self, app_name: str) -> List[str]:
        """
        Установить приложение

        :param app_name: Приложения
        :return: Список приложений
        """
        if not isinstance(app_name, str):
            raise TypeError
        self.apps.append(app_name)
        return self.apps


class Tree:
    """Класс для дерева"""

    def __init__(self, sp: str, age: int, he: float):
        """
        >>> tree = Tree("Берёза", 10, 5.5)
        >>> tree.sp
        'Берёза'
        """
        if not isinstance(sp, str):
            raise TypeError
        if not isinstance(age, int) or age <= 0:
            raise ValueError
        if not isinstance(he, (int, float)) or he <= 0:
            raise ValueError

        self.sp = sp
        self.age = age
        self.he = he
        self.season = "лето"

    def grow(self, years: int) -> float:
        """
        Взрастить дерево

        :param years: Сколько лет
        :return: Высота

        >>> tree = Tree("Берёза", 10, 5.5)
        >>> tree.grow(5)
        6.5
        """
        if years < 0:
            raise ValueError
        self.age += years
        self.he += years * 0.2
        return self.he

    def change_season(self, season: str) -> str:
        """
        Сезон

        :param season: Имя сезона
        :return: Сейчас сезон

        >>> tree = Tree("Берёза", 10, 5.5)
        >>> tree.change_season("осень")
        'осень'
        """
        valid_seasons = ["весна", "лето", "осень", "зима"]
        if season not in valid_seasons:
            raise ValueError(f"Сезон должен быть одним из: {valid_seasons}")
        self.season = season
        return self.season