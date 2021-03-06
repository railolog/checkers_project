class WhiteShashka():                  # Создаём класс белых и черных шашек
    def __init__(self, y, x):
        self.koords = [x, y]           # Координаты шашки на доске

    def hod(self, board, x, y):        # Аргументы: доска с шашками, координаты
        y0, x0 = self.koords           # Получаем нынешние координаты
        if x0 == x and y0 == y:
            return False
        if board[y][x] != 0:           # Проверяем свободна ли клетка
            return False
        if abs(x - x0) > 2 or abs(y - y0) > 2 or abs(x - x0) != abs(y - y0):
            # Проверка на корректность хода(по диагонали)
            return False
        if abs(x - x0) == 2:            # Проверка на корректность "срубания"
            x1, y1 = abs(x + x0)//2, abs(y + y0)//2
            if type(board[y1][x1]) == BlackShashka:
                return ((x, y), True, (x1, y1))
# Возвращаем координаты нового положения, маркер "срубания",
# координаты "срубаемого"
            return False
        if abs(x - x0) == 1:           # Проверка на корректность обычного хода
            if y0 <= y:
                return False
            if board[y][x] == 0:
                return ((x, y), False)
            return False


class BlackShashka():
    def __init__(self, y, x):
        self.koords = [x, y]

    def hod(self, board, x, y):
        y0, x0 = self.koords
        if x0 == x and y0 == y:
            return False
        if board[y][x] != 0:
            return False
        if abs(x - x0) > 2 or abs(y - y0) > 2 or abs(x - x0) != abs(y - y0):
            return False
        if abs(x - x0) == 2:
            x1, y1 = abs(x + x0)//2, abs(y + y0)//2
            if type(board[y1][x1]) == WhiteShashka:
                return ((x, y), True, (x1, y1))
            return False
        if abs(x - x0) == 1:
            if y0 >= y:
                return False
            if board[y][x] == 0:
                return ((x, y), False)
            return False


class Board():
    def __init__(self):
        self.desk = [[0, 2] * 4,
                     [2, 0] * 4,
                     [0, 2] * 4,
                     [0] * 8, [0] * 8,
                     [1, 0] * 4,
                     [0, 1] * 4,
                     [1, 0] * 4]
        for i in range(8):
            for j in range(8):
                if self.desk[i][j] == 2:
                    self.desk[i][j] = BlackShashka(j, i)
                elif self.desk[i][j] == 1:
                    self.desk[i][j] = WhiteShashka(j, i)
