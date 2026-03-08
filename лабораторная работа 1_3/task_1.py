class Book:
    def __init__(self, n: str, a: str):
        self.n = n
        self.a = a
    def __str__(self):
        return f"Книга {self.n}. Автор {self.a}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.n!r}, author={self.a!r})"


class PaperBook(Book):
    def __init__(self, n: str, a: str, pag: int):
        super().__init__(n, a)
        self.pag = pag

class AudioBook(Book):
    def __init__(self, n: str, a: str, dur: float):
        super().__init__(n, a)
        self.dur = dur

if __name__ == "__main__":
    b = Book("Гете", "Фауст")
    pap = PaperBook("Человек_недостойный", "Дадзай", 300)
    aud = AudioBook("Капитанская_дочка", "Пушкин", 9.5)

    print(b)
    print(pap)
    print(aud)
    print(repr(pap))
    print(repr(aud))




