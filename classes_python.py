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


# classes Track and TrackLine

class Track:
    def __init__(self, start_x, start_y):
        self._start_x = start_x
        self._start_y = start_y
        self._tracks = []

    def add_track(self, tr):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)

    def __len__(self):
        len1 = ((self._start_x - self._tracks[0].x) ** 2 + (self._start_y - self._tracks[0].y) ** 2) ** 0.5
        return int(len1 + sum(self.__get_length(i) for i in range(1, len(self._tracks))))

    def __get_length(self, i):
        return ((self._tracks[i - 1].x - self._tracks[i].x) ** 2 + (
                self._tracks[i - 1].y - self._tracks[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_speed(self):
        return self._max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2

# classes Cell and GamePole

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()


# classes Router, Server and Data

class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()


class Server:
    server_ip = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, msg, ip):
        self.data = msg
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()


# classes ObjList and LinkedList

class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def set_data(self, obj):
        self.__data = obj

    def get_next(self):
        return self.__next

    def set_next(self, obj):
        self.__next = obj

    def get_prev(self):
        return self.__prev

    def set_prev(self, obj):
        self.__prev = obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return

        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev

        if self.tail is None:
            self.head = None

    def get_data(self):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']

# class EmailVaidator

from string import ascii_uppercase, ascii_lowercase, digits


class EmailValidator:
    EMAIL_CHARS = ascii_uppercase + ascii_lowercase + digits + '_.@'
    EMAIL_RANDOM_CHARS = ascii_uppercase + ascii_lowercase + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join(sample(cls.EMAIL_RANDOM_CHARS, randint(4, 20))) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if '.' not in s[1]:
            return False
        if email.count('..') > 0:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


res = EmailValidator.check_email("sc_lib@list.ru")  # True
res = EmailValidator.check_email("sc_lib@list_ru")  # False


# class Circle

class Circle:
    attrs = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}

    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) not in self.attrs[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


circle = Circle(1, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует

# classes GeyserClassic, Mechanical, Aragon, Aragon

import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filter_class = ('Mechanical', 'Aragon', 'Calcium')
        self.filters = {
            (1, self.filter_class[0]): None,
            (2, self.filter_class[1]): None,
            (3, self.filter_class[2]): None
        }

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        if type(slot_num) == int and 1 <= slot_num <= 3:
            key = (slot_num, self.filter_class[slot_num - 1])
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for f in self.filters.values():
            if f is None:
                return False
            start = f.date
            if end - start > self.MAX_DATE_FILTER:
                return False
        return True


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


# classes ObjList and LinkedList

class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        if isinstance(obj, str):
            self.__data = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if isinstance(obj, (ObjList, type(None))):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, (ObjList, type(None))):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if self.head is None:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        p = obj.prev
        n = obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev

# class Complex

from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        return sqrt(self.real ** 2 + self.img ** 2)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)


# class RadiusVector

class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def get_coords(self):
        return self.__coords

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(i ** 2 for i in self.__coords) ** 0.5


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)


# classes TreeObj and DecisionTree

class TreeObj:
    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            else:
                obj = obj_next
        return obj.value

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        return obj.right


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)


# clases Clock and DeltaClock

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        if self.clock1.get_time() - self.clock2.get_time() < 0:
            return f'00: 00: 00'
        return f'{str(self.clock1.hours - self.clock2.hours).zfill(2)}: ' \
               f'{str(self.clock1.minutes - self.clock2.minutes).zfill(2)}: ' \
               f'{str(self.clock1.seconds - self.clock2.seconds).zfill(2)}'

    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return diff if diff > 0 else 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400


# classes Ingredient and Recipe

class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.__ingredients = list(args)

    def get_ingredients(self):
        return tuple(self.__ingredients)

    def add_ingredient(self, ing):
        self.__ingredients.append(ing)

    def remove_ingredient(self, ing):
        self.__ingredients.remove(ing)

    def __len__(self):
        return len(self.__ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3


# class ListMath

class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __verify_method(value):
        if type(value) not in (int, float):
            raise ArithmeticError('operand should has type int or float')

    def __add__(self, other):
        self.__verify_method(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.__verify_method(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __mul__(self, other):
        self.__verify_method(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        self.__verify_method(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math])

    def __iadd__(self, other):
        self.__verify_method(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __isub__(self, other):
        self.__verify_method(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __imul__(self, other):
        self.__verify_method(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.__verify_method(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])  # ListMath: [1, -5, 7.68]
lst = lst + 76  # сложение каждого числа списка с определенным числом
lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76  # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst  # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst  # деление числа на каждый элемент списка
lst /= 13.0


# classes Book and Lib

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self, book_list=None):
        book_list = book_list if book_list and isinstance(book_list, list) else []
        self.book_list = book_list

    @staticmethod
    def __verify_method(obj):
        if not isinstance(obj, (Book, int)):
            raise TypeError('object should class Lib')

    def __add__(self, other):
        self.__verify_method(other)
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self.__verify_method(other)
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        self.__verify_method(other)
        if type(other) == Book:
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        self.__verify_method(other)
        if type(other) == Book:
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


# classes Item and Budget

class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        elif isinstance(other, (int, float)):
            return self.money + other
        else:
            raise TypeError('operand should has type Item or int or float')

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)


# class Box3D

class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3  # Box3D: width=2, height=1, depth=0


# class MaxPooling

class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh:i * sh + h] for x in r[j * sw:j * sw + w])
                res[i][j] = max(s)
        return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
print(res)


# classes Dimensions and ShopItem

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = 0
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verify_method(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__verify_method(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__verify_method(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__verify_method(value):
            self.__c = value

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __ge__(self, other):
        return self.volume >= other.volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __lt__(self, other):
        return self.volume < other.volume


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

# class StringText

import re

stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

pattern = r'[–?!,.;]'
lst = []
for i in stich:
    lst.append(re.sub(pattern, '', i).split())


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)

    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)


lst_text = [StringText(lst_words) for lst_words in lst]
lst_text_sorted = [' '.join(i.lst_words) for i in sorted(lst_text, reverse=True)]


# class Morph

class Morph:
    def __init__(self, *args):
        self._words = list(map(lambda x: x.strip(' .,!?;:').lower(), args))

    def add_word(self, word):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other):
        if type(other) != str:
            raise ValueError('operand should has type str')
        return other.lower() in self._words


dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]
text = 'Мы будем устанавливать связь завтра днем.'
words = map(lambda x: x.lower().strip(' .,!?;:'), text.split())
res = sum(word == morph for word in words for morph in dict_words)


# class FileAcceptor

class FileAcceptor:
    def __init__(self, *args):
        self.extensions = args

    def __add__(self, other):
        return FileAcceptor(*self.extensions + other.extensions)

    def __call__(self, filename):
        return filename.split('.')[-1] in self.extensions


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))


# classes CentralBank, Money, MoneyR, MoneyD, MoneyE

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    EPS = 0.1
    type_money = None

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError('Неизвестен курс валют.')
        if self.type_money is None:
            raise ValueError('Неизвестен тип кошелька.')

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volumes(other)
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = 'rub'


class MoneyD(Money):
    type_money = 'dollar'


class MoneyE(Money):
    type_money = 'euro'


# class Body

class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def body_weight(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if type(other) == Body:
            return self.body_weight() == other.body_weight()
        return self.body_weight() == other

    def __gt__(self, other):
        if type(other) == Body:
            return self.body_weight() > other.body_weight()
        return self.body_weight() > other

    def __lt__(self, other):
        if type(other) == Body:
            return self.body_weight() < other.body_weight()
        return self.body_weight() < other


body1 = Body('square', 10, 15.0)
body2 = Body('sircle', 10, 15.0)

print(body1 > 15)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2)  # True, если масса тела body1 равна массе тела body2
print(body1 < 100)  # True, если масса тела body1 меньше 10
print(body2 == 5)  # True, если масса тела body2 равна 5


# classes Thing and Box

class Thing:
    def __init__(self, name: str, mass: (int, float)):
        self.name = name.lower()
        self.mass = mass
        self.lst = [self.name, self.mass]

    def __eq__(self, other):
        if not isinstance(other, Thing):
            raise ValueError('operand should type class Thing')
        return self.name == other.name and self.mass == other.mass


class Box:
    def __init__(self):
        self.__things = []

    def add_thing(self, obj: Thing):
        self.__things.append(obj)

    def get_things(self):
        return self.__things

    def __eq__(self, other):
        if not isinstance(other, Box):
            raise ValueError('operand should type class Box')
        return sum(i.lst == j.lst for i in self.__things for j in other.__things) == len(self.__things)


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 != b2  # True


# classes DataBase and Record

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


class Record:
    count = 1

    def __init__(self, fio, descr, old):
        self.pk = self.count
        Record.count += 1
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase('database.db')

for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))


# class BookStudy

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = [BookStudy(*i.split(';')) for i in lst_in]
unique_books = len(set(lst_bs))


# class Dimensions

class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
lst_dims = sorted([Dimensions(*map(float, elem.split())) for elem in s_inp.split(';')], key=hash)


# class Triangle

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.verify_triangle()

    def __setattr__(self, key, value):
        if type(value) not in (int, float) and value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        object.__setattr__(self, key, value)

    def verify_triangle(self):
        if not (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        return True

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s


# classes PositiveValue and Triangle

class PositiveValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = PositiveValue()
    b = PositiveValue()
    c = PositiveValue()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle(value, self.b, self.c)) or \
                (key == 'b' and not self.__is_triangle(self.a, value, self.c)) or \
                (key == 'c' and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    def __len__(self):
        return self.a + self.b + self.c if self.a and self.b and self.c else None

    def __call__(self):
        a, b, c = self.a, self.b, self.c
        if not (a and b and c):
            return None

        p = 0.5 * (a + b + c)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# classes Cell and GamePole

from random import randint


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) != int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        GamePole.__instance = None

    def __init__(self, N, M, total_mines):
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for row in self.__pole_cells:
            for x in row:
                x.is_open = False
                x.is_mine = False

        n = 0
        while n < self._total_mines:
            i = randint(0, self._n - 1)
            j = randint(0, self._m - 1)
            if self.__pole_cells[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            n += 1

        index = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine:
                    mines = sum((self.pole[x + i][y + j].is_mine for i, j in index if
                                 0 <= x + i < self._n and 0 <= y + j < self._m))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self._n or not 0 <= j < self._m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))


# class Vector

class Vector:
    def __init__(self, *args):
        self.coords = args

    @staticmethod
    def verify_length(obj1, obj2):
        if len(obj1) != len(obj2):
            raise ArithmeticError('размерности векторов не совпадают')

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        self.verify_length(self, other)
        return Vector(*(x + y for x, y in zip(self.coords, other.coords)))

    def __sub__(self, other):
        self.verify_length(self, other)
        return Vector(*(x - y for x, y in zip(self.coords, other.coords)))

    def __mul__(self, other):
        self.verify_length(self, other)
        return Vector(*(x * y for x, y in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        self.coords = tuple(x + y for x, y in zip(self.coords, other.coords)) if type(other) == Vector else tuple(
            x + other for x in self.coords)
        return self

    def __isub__(self, other):
        self.coords = tuple(x - y for x, y in zip(self.coords, other.coords)) if type(other) == Vector else tuple(
            x - other for x in self.coords)
        return self

    def __eq__(self, other):
        return self.coords == other.coords


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]
v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]
print(v1 == v2)  # False
print(v1 != v2)  # True


# class Track

class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.coords = []

    def add_point(self, x, y, speed):
        self.coords.append([(x, y), speed])

    def __chek_index(self, index):
        if type(index) != int or index not in range(len(self.coords)):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.__chek_index(item)
        return self.coords[item]

    def __setitem__(self, key, value):
        self.__chek_index(key)
        self.coords[key][-1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)


# classes Star, WhiteDwarf, YellowDwarf, RedGiant, Pulsar

class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


stars = [
    RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
    WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
    WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
    YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)
]

white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
