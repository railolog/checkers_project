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
    def __init__(self, x, y):
        self.koords = [x, y]
    
    
    def hod(self, x, y):
        global mas
        x0, y0 = self.koords
        if [x, y] in mas:
            return -1
        if abs(x - x0) > 2 or abs(y - y0) > 2:
            return -1
        if abs(x - x0) == 2:
            if x < x0:
                x1 = x + 1
            else:
                x1 = x - 1
            if y < y0:
                y1 = y + 1
            else:
                y1 = y - 1
            if [x1, y1] in masBlak:
                delit(x1, y1)
                setmove(self, x, y)
                return 0
            else:
                return -1
        setmove(self, x, y)
        return 0



class BlackShashka():
    def __init__(self, x, y):
        self.koords = [x, y]
    
    
    def hod(self, x, y):
        global mas
        x0, y0 = self.koords
        if x0 == x and y0 == y:
            changeCvet()
        if [x, y] in mas:
            return -1
        if abs(x - x0) > 2 or abs(y - y0) > 2:
            return -1
        if abs(x - x0) == 2:
            if x < x0:
                x1 = x + 1
            else:
                x1 = x - 1
            if y < y0:
                y1 = y + 1
            else:
                y1 = y - 1
            if [x1, y1] in masWhit:
                delit(x1, y1)
                setmove(self, x, y)
                return 0
            else:
                return -1
        setmove(self, x, y)
        return 0


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
                    self.desk[i][j] = BlackShashka(i, j)
                elif self.desk[i][j] == 1:
                    self.desk[i][j] = WhiteShashka(i, j)
a = Board()