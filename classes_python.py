# class_log_methods

def class_log(log_lst):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_method_decorator(v))
        return cls

    def log_method_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return log_methods


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


# Vector = class_log(vector_log)(Vector)

v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)


# classes Stack and StackObj

class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj

        self.__last = obj

    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __len__(self):
        return sum(1 for _ in self)

    def _get_obj(self, indx):
        if type(indx) != int or not (0 <= indx <= len(self)):
            raise IndexError('неверный индекс')
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self._get_obj(item).data

    def __setitem__(self, key, value):
        self._get_obj(key).data = value


# classes Stack and StackObj

class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.__last:
            self.__last.next = obj
        self.__last = obj
        if self.top is None:
            self.top = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return

        while h.next and h.next != self.__last:
            h = h.next

        if self.top == self.__last:
            self.top = self.__last = None
        else:
            h.next = None
            self.__last = h

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
        return self

    def __imul__(self, other):
        return self.__mul__(other)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


# classes StackInterface, Stack and StackObj

from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """adding an object to the end of the stack"""

    @abstractmethod
    def pop_back(self):
        """removing the last object from the stack"""


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._last = None

    def push_back(self, obj):
        if self._last:
            self._last.next = obj
        self._last = obj
        if self._top is None:
            self._top = obj

    def pop_back(self):
        h = self._top
        if h is None:
            return

        while h.next and h.next != self._last:
            h = h.next

        if self._top == self._last:
            del_obj = self._top
            self._top = self._last = None
        else:
            del_obj = h.next
            h.next = None
            self._last = h
        return del_obj

    def __iter__(self):
        h = self._top
        while h:
            yield h
            h = h.next


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, obj):
        self._next = obj


# classes CountryInterface and Country
class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """abstract object-property"""

    @property
    @abstractmethod
    def population(self):
        """abstract object-property"""

    @property
    @abstractmethod
    def square(self):
        """abstract object-property"""

    @abstractmethod
    def get_info(self):
        """method for getting information about the country"""


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name
        self.__population = population
        self.__square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


# class RandomPassword

from random import randint, sample  # функция для генерации целых случайных значений в диапазоне [a; b]


# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(sample(self.psw_chars, randint(self.min_length, self.max_length)))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass = [rnd() for i in range(3)]
