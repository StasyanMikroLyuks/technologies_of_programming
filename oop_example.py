class Car:
    """КОНСТРУКТОР"""
    def __init__(self):
        """если __ то приватный private"""
        """если без ничего - публичный public"""
        """если _ то защищенный protected"""
        """ПОЛЕ КЛАССА"""
        self._a = 20
        print("STAS PRIVET!!!")


    """Метод класса"""
    def move(self):
        print(0)
        return 0


class Motorcycle(Car):
    def __init__(self):
        super().__init__()
        print("PAVEL TOZHE")

    """
        Виды полиморфизма: переопределение (override)
        сокрытие (hide)
    """
    def move(self):
        print("param: ")
        return 200


# создание объекта
# объект - это переменная класса, копия класса, экземпляр класса
car = Car()
car.move()

motor = Motorcycle()
motor.move(20)
