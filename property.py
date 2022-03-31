#Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should int or float')
        else:
            self.__balance = value

    def delete_balance(self):
        del self.__balance

    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=delete_balance)


a = BankAccount('Alex', 100000000)
print(a.balance)
a.balance = 777
print(a.balance)
