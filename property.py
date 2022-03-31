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
