import math
# вывод комплексного числа
class ComplexNumber:    # объявляем класс
    def __init__(self, real, imaginary):    # объявляем метод с параметрами реального и мнимого числа
        self.x = real                       # определяем переменую с реальным числом
        self.y = imaginary                  # определяем переменную с мнимым числом
    def __str__(self):                      # определяем функцию для возврата строки
        return str(self.x) + (self.y >= 0 and " +" or " ") + str(self.y) + "i"      # возвращаем строку

# сложение
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumber(x, y)

# сопряжённое число
    def getConjugate(self):
        return ComplexNumber(self.x, -self.y)

# модуль числа
    def __abs__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

Number1 = ComplexNumber(3, -8)  # создаём объект класса
print(Number1)                  # печатаем число
Number2 = ComplexNumber(13, 17)
print(Number1 + Number2)
print(Number1.getConjugate())
print(abs(ComplexNumber(4, -29)))