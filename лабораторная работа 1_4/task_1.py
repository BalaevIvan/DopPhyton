class Vehicle:
    """Базовый класс автомобиля"""

    def __init__(self, br: str, m: str, ye: int):
        self.br = br
        self.m = m
        self.ye = ye
        self.mi = 0
    def drive(self, dis: float) -> str:
        self.mi += dis
        return f"{dis} км"
    def __str__(self) -> str:
        return f"{self.br} {self.m}, {self.ye} года"
    def __repr__(self) -> str:
        return f"Vehicle('{self.br}', '{self.m}', {self.ye})"
class Car(Vehicle):
    """Класс автомобиля"""

    def __init__(self, br: str, m: str, ye: int, f_t: str):
        super().__init__(br, m, ye)
        self.f_t = f_t
        self.fl = 50
    def drive(self, dis: float) -> str:
        """Перегружен: с расходом"""
        need = dis * 0.1
        if need > self.fl:
            return "Нет топлива"
        self.fl -= need
        return super().drive(dis) + f", осталось: {self.fl} л"
    def __str__(self) -> str:
        return f"Авто {self.br} {self.m}, {self.f_t}"
    def __repr__(self) -> str:
        return f"Car('{self.br}', '{self.m}', {self.ye}, '{self.f_t}')"
    
if __name__ == "__main__":
    v = Vehicle("Generic", "Model", 2020)
    print(v)
    print(v.drive(100))

    c = Car("Toyota", "Camry", 2021, "бензин")
    print(c)
    print(c.drive(200))
    print(c.drive(300))

