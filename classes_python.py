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
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
