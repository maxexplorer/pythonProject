# Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should int or float')
        else:
            self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

a = BankAccount('Alex', 100000000)
print(a.my_balance)
a.my_balance = 777
print(a.my_balance)


from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def simple_password(value):
        with open('passwords.txt', 'r', encoding='utf-8') as file:
            passwords = file.read()
            if value in passwords:
                print(value)
                return True
            return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Password should be string')
        if len(value) < 4:
            raise ValueError('length should be minimum 4 chars')
        if len(value) > 12:
            raise ValueError('length should be maximum 12 chars')
        if not User.is_include_number(value):
            raise ValueError('Password should contain number')
        if User.simple_password(value):
            raise ValueError('Password is simple')
        self.__password = value


a = User('bob', '555555abs')
print(a.password)
a.password = 'cjkhkjl7'
print(a.password)


from string import ascii_letters

class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Логин должен содержать символ '@'")
        if '.' not in value:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = value

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_all_register(value):
        return any(map(lambda x: x.upper(), value)) + any(map(lambda y: y.lower(), value))

    @staticmethod
    def is_include_only_latin(value):
        for i in value:
            if i in ascii_letters:
                return True
        return False

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_password.txt', 'r', encoding='utf-8') as file:
            passwords = file.read()
            if value in passwords:
                print(value)
                return True
            return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) not in range(5, 12):
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not any(map(str.isdigit, value)):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if Registration.is_include_all_register(value) != 2:
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value


a = Registration('abc@mail.ru', 'qwerty123')
print(a.password)

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