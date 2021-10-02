class Pole:

    def __init__(self, row, col):
        self._pole = [[0 for a in range(row)] for b in range(col)]

    def show(self):
        print("\033[H\033[J")
        matrix = self._pole.copy()
        for line in map(lambda x: x.copy(), matrix):
            for i in range(len(line)):
                if line[i] == 0:
                    line[i] = ' '
                else:
                    line[i] = '*'
            print(''.join(line))

    def add_unit(self, unit, x, y):
        self._pole[x][y] = unit
        unit.set_pole(self)
        unit.set_x(x)
        unit.set_y(y)

    def seve_unit(self, x, y,):
        pass

    def move_unit(self, unit, x, y):
        self._pole[x][y] = unit
        self._pole[unit._x][unit._y] = 0
        unit.set_x(x)
        unit.set_y(y)


class Unit:

    def __init__(self, name):
        self.name = name
        self._pole = None
        self._x = None
        self._y = None

    def set_pole(self, m):
        self._pole = m

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def go_unit(self, napr):
        if napr == 'left':
            self._pole.move_unit(self, self._x, self._y - 1)
        elif napr == 'up':
            self._pole.move_unit(self, self._x - 1, self._y)
        elif napr == 'down':
            self._pole.move_unit(self, self._x + 1, self._y)
        elif napr == 'right':
            self._pole.move_unit(self, self._x, self._y + 1)
