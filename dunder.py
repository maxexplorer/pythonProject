# Магический методы

class Vector:

    def __init__(self, *args):
        self.values = sorted(filter(lambda x: isinstance(x, int), args))

    def __str__(self):
        if self.values:
            b = list(map(str, self.values))

            return f'Вектор({", ".join(b)})'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            b = list(map(lambda x: x + other, self.values))
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = list(map(lambda x, y: x + y, self.values, other.values))
                return Vector(*b)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            b = list(map(lambda x: x * other, self.values))
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = list(map(lambda x, y: x * y, self.values, other.values))
                return Vector(*b)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножить с {other}')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other

a = Rectangle(10, 20)
b = Rectangle(30, 40)
print(a.area)
print(b.area)
print(a < b)
print(a > b)

class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, int):
            return self.rating == other
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, int):
            return self.rating > other
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        elif isinstance(other, int):
            return self.rating < other
        else:
            return 'Невозможно выполнить сравнение'

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнение"