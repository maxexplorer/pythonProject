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

    my_balance = property(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)


a = BankAccount('Alex', 100000000)
print(a.my_balance)
a.my_balance = 777
print(a.my_balance)
