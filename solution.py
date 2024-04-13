from random import choice, randint
from copy import deepcopy


class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def __repr__(self):
        return str(self.radius)

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        return sum([Circle.area(circ) for circ in Circle.all_circles])


class NavalBattle:
    playing_field = []
    playing_field_show = [['⁓' for j in range(10)] for i in range(10)]

    def __init__(self, marker: str):
        self.marker = marker

    def shot(self, x, y):
        if NavalBattle.playing_field:
            if NavalBattle.playing_field_show[y - 1][x - 1] == '⁓':
                if NavalBattle.playing_field[y - 1][x - 1]:
                    NavalBattle.playing_field_show[y - 1][x - 1] = self.marker
                    print('попал')
                else:
                    NavalBattle.playing_field_show[y - 1][x - 1] = 'o'
                    print('мимо')
            else:
                print('ошибка')
        else:
            print('поле не заполнено')

    @staticmethod
    def show():
        for i in range(10):
            print(*NavalBattle.playing_field_show[i], sep='')

    @classmethod
    def new_game(cls):
        cls.playing_field = [[0 for j in range(10)] for i in range(10)]
        cls.playing_field_show = [['⁓' for j in range(10)] for i in range(10)]

        for ship_count in range(1, 5):
            ship_len = 5 - ship_count

            for ship in range(ship_count):
                while True:
                    playing_field_try = deepcopy(cls.playing_field)
                    x, y = randint(0, 9), randint(0, 9)
                    orientation = choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
                    for sector in range(ship_len):
                        if 0 <= x <= 9 and 0 <= y <= 9:
                            acceptable = True
                            for i in range(x - 1 + (x == 0), x + 2 - (x == 9)):
                                for j in range(y - 1 + (y == 0), y + 2 - (y == 9)):
                                    if cls.playing_field[i][j] != 0:
                                        acceptable = False

                            if acceptable:
                                playing_field_try[x][y] = 1
                                x += orientation[0]
                                y += orientation[1]

                            else:
                                break

                        else:
                            break
                    else:
                        cls.playing_field = deepcopy(playing_field_try)
                        break


class RomanNumber:
    dec_to_rom = {}  # creates roman to decimal translator
    rom_to_dec = {}  # creates decimal to roman translator
    for i in range(1, 4000):
        roman_helper = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'M', 'MM', 'MMM']
        ]
        rom = ''
        dec = i
        while dec:
            rom = roman_helper[len(str(i)) - len(str(dec))][dec % 10] + rom
            dec //= 10
        dec_to_rom[i] = rom
        rom_to_dec[rom] = i

    @staticmethod
    def is_roman(value):
        if value in RomanNumber.rom_to_dec:
            return True
        return False

    @staticmethod
    def is_int(value):
        if value in RomanNumber.dec_to_rom:
            return True
        return False

    def __init__(self, value=None):
        if isinstance(value, int):
            if RomanNumber.is_int(value):
                self.rom_value = RomanNumber.dec_to_rom[value]
                self.int_value = value
            else:
                print('ошибка')
                self.rom_value = None
                self.int_value = None
        elif RomanNumber.is_roman(value):
            self.rom_value = value
            self.int_value = RomanNumber.rom_to_dec[value]
        else:
            print('ошибка')
            self.rom_value = None
            self.int_value = None

    def __repr__(self):
        return str(self.rom_value)

    def __add__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value + other.int_value)

    def __sub__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value - other.int_value)

    def __mul__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value * other.int_value)

    def __pow__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value ** other.int_value)

    def __truediv__(self, other):
        if self.int_value is None or other.int_value is None \
                or self.int_value // other.int_value != self.int_value / other.int_value:
            return RomanNumber(None)
        return RomanNumber(self.int_value // other.int_value)

    def __floordiv__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value // other.int_value)

    def __mod__(self, other):
        if self.int_value is None or other.int_value is None:
            return RomanNumber(None)
        return RomanNumber(self.int_value % other.int_value)

    def decimal_number(self):
        return self.int_value

    def roman_number(self):
        return self.rom_value

