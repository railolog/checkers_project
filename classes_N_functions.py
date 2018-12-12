def sum_mas(mas):
    S = []
    for i in mas:
        S += i
    return mas



masWhit = sum_mas([[[(j + i%2 + 1) % 8, i] for j in range(0, 8, 2)]
                    for i in range(4)])
masBlak = sum_mas([[[(j + i%2 + 1) % 8, 7 - i] for j in range(0, 8, 2)]
                    for i in range(4)])
mas = masWhit + masBlak


class WhiteShashka():
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
            #print([str(x), str(y), str(x0), str(y0), str(x1), str(y1)])
            if type(board[y1][x1]) == BlackShashka:
                return ((x, y), True, (x1, y1))
            return False
        if abs(x - x0) == 1:
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
            #print([str(x), str(y), str(x0), str(y0), str(x1), str(y1)])
            x1, y1 = abs(x + x0)//2, abs(y + y0)//2
            if type(board[y1][x1]) == WhiteShashka:
                return ((x, y), True, (x1, y1))
            return False
        if abs(x - x0) == 1:
            if board[y][x] == 0:
                return ((x, y), False)
            return False


hodit = 0 #белые код 0; черные код 1


def hodit(self):
    global hodit
    if self.kod != hodit:
        return -1
    changeCvet()
    x, y = askKoordsHoda()
    self.hod(x, y)
    return 0


#while mas != []:
#    x, y, self = askKoordsHoda()
#    while hodit(self) == -1:
#        x, y, self = askKoordsHoda()
a = [0, BlackShashka(0, 2)]


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
a = Board()