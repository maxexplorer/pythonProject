#Геттеры и сеттеры, property атрибуты

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
