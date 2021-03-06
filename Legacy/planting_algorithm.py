"""Tree Planting Algorhythm, Program will gather Land Management related
information the fill the pice in the most efficient square wat"""

from pathlib import Path
import time
from graphics import *
BAG_SIZE = 20


class PICE:
    """
    User friendly way to manipulate characters in pice_data
    """
    def __init__(self, file):
        """
        Creates pice class object
        @param self PICE
        @param file txtfile pice as a txt file
        @rtype None
        """
        # Pice Data
        self.data = []

        # PlanterClasses Data
        self.trees_planted = 0
        self.bag_size = BAG_SIZE
        self.trees_baged = 0
        self.x = 0
        self.y = 0
        self.planting = False

        # Hole Data
        self.h_move_prev = 'none'
        self.hole_num = 0
        self.hole_total = 0
        self.hole_list = []

        # Hole Data
        self.dire = 'N'
        self.last_dire = 'N'

        # Importing Pice Data
        pice = open(file, 'r')
        line = pice.readline()

        while line != '':
            spaced_line = []
            line = line[0: len(line) - 1]

            for space in line:
                spaced_line.append(space)

            self.data.append(spaced_line)
            line = pice.readline()

        # Pice Data Information
        self.width = (max(len(line) for line in self.data))
        self.height = len(self.data)

    def in_pice(self, x, y):
        """
        Returns True iff data point is in range of pice

        @param pice Pice
        @param x int
        @param y int
        @rtype bool
        """
        # print('Y: ' + str(y) + ' X: ' + str(x))
        # print('len Y: ' + str(len(self.data)) + ' len X: ' + str(len(self.data[y])))
        if y + 1 > len(self.data) or x + 1 > len(self.data[y]):
            return False
        else:
            return True

    def see(self, x, y):
        """
        Returns the Character at colum x and row y
        @param x int
        @param y int
        @rtype str
        """
        if self.in_pice(x, y) is True:
            return self.data[y][x]
        else:
            return 'Error not in pice'

    def find_char(self, char):
        """
        Returns the coordonits of the cash

        @param self PICE
        @param char str
        @rtype list
        """
        c_y = 0
        while c_y < self.height:
            c_x = 0
            while c_x < len(self.data[c_y]):
                if self.see(c_x, c_y) == char:
                    return [c_x, c_y]
                else:
                    c_x += 1
            c_y += 1
        return 'E'

    def plant(self, x, y):
        """
        Plant a tree in the specified space

        @param self Pice
        @param x int
        @param y int
        @rtype None
        """
        self.data[y][x] = 'T'

    def finished(self):
        """
        Returns True iff pice is finished

        @rtype bool
        """
        if self.find_char('�') == 'E' and self.find_char(1) == 'E':
            return True
        else:
            return False

    def planter_here(self, x, y):
        """
        returns what is left behind the planter when it leaves

        @param self PICE
        @param x int
        @param y int
        @rtype str
        """
        if self.see(x, y) == '�':
            if self.trees_baged > 0:
                return 'T'
            else:
                return 'D'

        elif self.see(x, y) == 'C':
            return 'C'

        elif self.see(x, y) == 'S':
            if self.trees_baged > 0:
                return 'T'
            else:
                return 'D'

        elif self.see(x, y) == 'T':
            return 'D'

        elif self.see(x, y) == 'D':
            return 'D'

        elif isinstance(self.see(x, y), int):
            return 'T'
        return 'E'

    def draw_char(self, windw, x, y, ch, colour='red'):
        """
        Draws character on window
        @param self PICE
        @param windw Window
        @param x int
        @param y int
        @param ch str
        @param colour str
        @rtype None
        """
        # find appropriate colour
        if colour == 'red':
            if ch == 'T':
                colour = 'green2'
            if ch == 'D':
                colour = 'red'
                ch = 'T'
            if ch == 'C':
                colour = 'pink3'
            if ch == '�':
                colour = 'white'
            if ch == '?':
                colour = 'yellow'

        # Erasses Previous Character
        label_box = Text(Point((x + 1) * 18, (y + 1) * 21), '�')
        label_box.setTextColor('black')
        label_box.draw(windw)

        # Draws New Character
        label_hole = Text(Point(
            (x + 1) * 18, (y + 1) * 21), ch)
        label_hole.setTextColor(colour)
        label_hole.draw(windw)

    def starts(self, windw):
        """
        Returns the first place to plant from

        @param windw Window
        @rtype list
        """
        r = 0
        done = False

        while not done:

            r += 1
            x = self.find_char('C')[0] + r
            y = self.find_char('C')[1] - r

            for i in range(4):
                if i == 0:
                    for j in range(r*x):
                        if self.in_pice(x, y) and\
                                self.planter_here(x, y) == 'T':
                            self.draw_char(windw, x, y, 'S', 'yellow')
                            return [x, y]
                        # self.draw_char(windw, x, y, 'S', 'pink2')
                        x += -1

                elif i == 1:
                    for j in range(r*x):
                        if self.in_pice(x, y) and\
                                self.planter_here(x, y) == 'T':
                            self.draw_char(windw, x, y, 'S', 'yellow')
                            return [x, y]
                        # self.draw_char(windw, x, y, 'S', 'pink2')
                        y += 1
                elif i == 2:
                    # x += 1
                    for j in range(r*x):
                        if self.in_pice(x, y) and\
                                self.planter_here(x, y) == 'T':
                            self.draw_char(windw, x, y, 'S', 'yellow')
                            return [x, y]
                        # self.draw_char(windw, x, y, 'S', 'pink2')
                        x += 1

                elif i == 3:
                    # y += -1
                    for j in range(r*x):
                        if self.in_pice(x, y) and\
                                self.planter_here(x, y) == 'T':
                            self.draw_char(windw, x, y, 'S', 'yellow')
                            return [x, y]
                        # self.draw_char(windw, x, y, 'S', 'pink2')
                        y += -1

    def check_stuck(self):
        """
        Returns True iff planter has to dead walk the following move
        @self: PICE
        @rtype bool
        """
        if self.planter_here(self.x + 1, self.y) != 'T' and \
                self.planter_here(self.x - 1, self.y) != 'T' and \
                self.planter_here(self.x, self.y + 1) != 'T' and \
                self.planter_here(self.x, self.y - 1) != 'T':
            return False  # Does not have to deadwalk

        return True  # PlanterClasses IS STUCK!

    def clear_num(self, windw):
        """
        resets all hole numbers data
        @param self PICE
        @param windw Window
        @rtype None
        """
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                if isinstance(self.data[row][col], int):
                    self.data[row][col] = '�'
                    self.draw_char(windw, col, row, '�')

    def line_back(self, windw, move='none'):
        """
        Will derive and draw information dictatind where to move on way back
        @param self PICE
        @param windw Window
        @param list pos: position of number
        @rtype list
        """
        time.sleep(0.0)
        # CHECK If PLAYER OR hole_list IS STUCK
        print(self.hole_list)
        if self.planting is False or self.check_stuck() is False:
            return

        if len(self.hole_list) > 2 and \
                [self.hole_list[len(self.hole_list) - 1][0],
                 self.hole_list[len(self.hole_list) - 1][1]] \
                == [self.hole_list[len(self.hole_list) - 2][0],
                    self.hole_list[len(self.hole_list) - 2][1]]:
            self.hole_list = []
            self.hole_total = 0
            self.hole_num = 0
            self.clear_num(windw)
            return

        # ESTABLISH STARTING POSITION
        if (self.hole_list == []) or (self.hole_total == 0):  # checks starting
            self.hole_list = []
            self.hole_total = 0
            self.hole_num = 0
            pos = (self.starts(windw))  # makes gives starting position

        else:
            # print(self.hole_list)
            pos = self.hole_list[len(self.hole_list) - 1]  # pos from list

            if [pos[0], pos[1]] == [int(self.x), int(self.y)]:  # hole on plantr
                if len(self.hole_list) != 1:
                    self.hole_list.pop()
                pos = self.hole_list[len(self.hole_list) - 1]

        h_x = pos[0]
        h_y = pos[1]

        # print(self.hole_list)
        # START RECURSION
        if [h_x + 1, h_y] == [self.x, self.y] or\
            [h_x - 1, h_y] == [self.x, self.y] or\
            [h_x, h_y + 1] == [self.x, self.y] or\
            [h_x, h_y - 1] == [self.x, self.y] or \
                [h_x, h_y] == [int(self.x), int(self.y)]:  # if beside stop
            return

        elif self.see(h_x + 1, h_y) == '�':
            h_x += 1

        elif self.see(h_x, h_y - 1) == '�':
            h_y += -1

        elif self.see(h_x - 1, h_y) == '�':
            h_x += -1

        elif self.see(h_x, h_y + 1) == '�':
            h_y += 1

        # else:
        #   self.hole_list = []

        pos = [h_x, h_y]
        self.hole_list.append(pos)

        if len(self.hole_list) <= 2 or\
                (self.hole_list[len(self.hole_list) - 1][0]
                    == self.hole_list[len(self.hole_list) - 2][0]
                    == self.hole_list[len(self.hole_list) - 3][0]) or (
            self.hole_list[len(self.hole_list) - 1][1]
            == self.hole_list[len(self.hole_list) - 2][1]
                == self.hole_list[len(self.hole_list) - 3][1]):  # is streight
            self.hole_num += 1
        else:  # esle reset to zero for new line
            self.hole_num = 0

        #  append hole number to new pos in hole_list
        self.hole_list[len(self.hole_list) - 1].append(self.hole_num)
        self.hole_total = len(self.hole_list)

        #  update map
        self.data[h_y][h_x] = self.hole_num
        self.draw_char(windw, h_x, h_y, str(self.hole_num))

        self.line_list_upodate(windw)
        self.line_back(windw, move)

    def line_list_upodate(self, windw):
        """
        updates self.hole_list so that values of numvers are accurate and
        uptades map to new hole_list

        @param self: PICE
        @param windw: Window
        @r_type: NoneType
        """
        count = 0
        if self.hole_list == []:
            return

        for i in range(len(self.hole_list) - 1):
            if self.hole_list[i][2] == 0:
                count = 0
            if self.hole_list[i][2] == count:
                pass
            else:
                mod = self.hole_list.pop(i)  # remove incorect pop
                mod.pop()  # correct incorect pop
                mod.append(count)
                self.hole_list.insert(i, mod) # insert incorect pop
                # update map
                self.data[mod[1]][mod[0]] = count
                self.draw_char(windw, mod[0], mod[1], str(count))

            count += 1

        # self.hole_num = count

    def move(self, dir, windw):
        """
        Moves planter in desired direction while planting a tree, if possible,
        else leaves a dead walk marker

        @param self PICE
        @param dir str direction planter moves
        @param windw graphics window
        @rtype None
        """
        # Establish Data
        move_x = 0
        move_y = 0
        if dir == 'r':
            move_x = 1
        elif dir == 'l':
            move_x = -1
        elif dir == 'u':
            move_y = -1
        elif dir == 'd':
            move_y = 1

        # draw charaters

        time.sleep(0.1)
        self.line_back(windw)

        self.draw_char(windw, self.x, self.y,
                       self.planter_here(self.x, self.y))
        self.draw_char(windw, self.x + move_x, self.y + move_y, '?')

        # Update Data Info and Panter Info ---------------------------------
        self.data[self.y][self.x] = self.planter_here(self.x, self.y)
        if self.data[self.y][self.x] == 'T':
            self.trees_baged += -1

        self.x += move_x
        self.y += move_y

        self.last_dire = self.dire
        self.dire = dir

        self.line_back(windw)

    def in_trees(self):
        """
        Returns True iff planter is in trees

        @param self PICE
        @rtype: bool
        """
        if (self.see(self.x + 1, self.y) == 'T' or
            self.see(self.x + 1, self.y) == 'X') and \
            (self.see(self.x - 1, self.y) == 'T' or
                self.see(self.x - 1, self.y) == 'X') and \
            (self.see(self.x, self.y + 1) == 'T' or
                self.see(self.x, self.y + 1) == 'X') and \
            (self.see(self.x, self.y - 1) == 'T' or
                self.see(self.x, self.y - 1) == 'X'):
            return True
        else:
            return False

    def close_wall(self, len):
        """
        Returns the dirrection iff the direction is less then len away. up is a
        priority the left, nothing else is considered

        @param self PICE
        @param len int
        @rtype: str
        """
        if len == 0:
            return 'N'
        if self.planter_here(self.x, self.y - 1) == 'T' and\
                self.see(self.x, self.y - len) == 'X':
            return 'U'
        if self.planter_here(self.x - 1, self.y) == 'T' and\
                self.see(self.x - len, self.y) == 'X':
            return 'R'
        else:
            self.close_wall(len - 1)


def drawpice(win, pice):
    """
    refreshes room so that a move has been made
    @param win Window
    @param pice Pice
    @rtype None
    """
    """
    rect = Rectangle(Point(0, 0), Point(pice.width*20, pice.height*24))
    rect.setFill('black')
    rect.draw(win)
    """
    r = 0
    for line in pice.data:
        r += 1
        c = 0
        for space in line:

# Create PlanterClasses ---------------------------------------------------------------
[pice.x, pice.y] = [pice.find_char('C')[0], pice.find_char('C')[1]]
cash_locati = [pice.x, pice.y]

drawpice(win, pice)
moves = 1

while not pice.finished():
    if pice.trees_baged > 0:
        pice.planting = True
    else:
        pice.planting = False

    if [pice.x, pice.y] == cash_locati:  # cash breake
        pice.trees_baged = BAG_SIZE

        pice.hole_list = []
        pice.planting = False
        print('BAGED UP' + str(pice.trees_baged))

    # Planting Algorhythm- -----------------------------------------------------
    # Planting Back To Cash
    if pice.trees_baged <= pice.hole_total:
        pice.planting = False

        """
        # I DONT KNOW IF IS NESSESARY

        if pice.see(pice.x - 1, pice.y) == 'T' and\
                pice.hole_total == pice.trees_baged:
            pice.line_back(win)

        if pice.hole_total == pice.trees_baged + 1:
            pice.line_back(win)
        """
        if pice.close_wall(3) == 'L':  # Checks LEFT close to wall
            pice.move('l', win)

        elif isinstance(pice.see(pice.x - 1, pice.y), int):
            pice.move('l', win)
        elif isinstance(pice.see(pice.x, pice.y + 1), int):
            pice.move('d', win)
        elif isinstance(pice.see(pice.x + 1, pice.y), int):
            pice.move('r', win)
        elif isinstance(pice.see(pice.x, pice.y - 1), int):
            pice.move('u', win)
        # Dead walk to cash ----------------------------------------------------

        elif pice.see(pice.x, pice.y + 1) in ['T', 'D', 'C', '�']:
            pice.move('d', win)
        elif pice.see(pice.x + 1, pice.y) in ['T', 'D', 'C', '�']:
            pice.move('r', win)

    # Squaring off -------------------------------------------------------------
    elif pice.see(pice.x, pice.y) in [0, 1, 2] and\
            isinstance(pice.see(pice.x + 1, pice.y), int) and\
            pice.hole_num != pice.hole_total and\
            pice.hole_total > 4:
        pice.move('r', win)

    elif pice.see(pice.x, pice.y) in [0, 1, 2] and\
            isinstance(pice.see(pice.x, pice.y + 1), int) and\
            pice.hole_num != pice.hole_total and\
            pice.hole_total > 4:
        pice.move('d', win)

    # Normal Planting ---------------------------------------------------------
    elif pice.planter_here(pice.x + 1, pice.y) == 'T':
        pice.move('r', win)

    elif pice.planter_here(pice.x, pice.y - 1) == 'T':
        pice.move('u', win)

    elif pice.close_wall(3) == 'U':  # check if UP wall is close
        pice.move('u', win)

    elif pice.planter_here(pice.x - 1, pice.y) == 'T':
        pice.move('l', win)

    elif pice.close_wall(3) == 'L':  # Check if LEFT wall is close
        pice.move('l', win)

    elif pice.planter_here(pice.x, pice.y + 1) == 'T':
        pice.move('d', win)

    # Dead Walking -------------------------------------------------------------
    elif pice.see(pice.x - 1, pice.y) in ['T', 'D']:
        pice.planting = False
        pice.move('l', win)

    elif pice.see(pice.x, pice.y + 1) in ['T', 'D']:
        pice.planting = False
        pice.move('d', win)

    elif pice.see(pice.x + 1, pice.y) in ['T', 'D']:
        pice.planting = False
        pice.move('r', win)

    elif pice.see(pice.x, pice.y - 1) in ['T', 'D']:
        pice.planting = False
        pice.move('u', win)

    else:
        print('Player IS STUCK')

    # print(moves)
    print(pice.trees_baged)
    moves += 1

time.sleep(5.0)
win.close()
            c += 1
            label = Text(Point(c * 18, r * 21), space)
            if space == 'T':
                label.setTextColor('green2')
            elif space == '?':
                label.setTextColor('yellow')
            elif space == 'C':
                label.setTextColor('pink3')
            else:
                label.setTextColor('white')
            label.draw(win)

# Helper Functions

pice = PICE('pice1.txt')
# print(pice.height)
# print(pice.width)
# print(pice.see(10, 11))
# print(pice.finished())
# print(pice.find_char('C'))
# print(pice.see(pice.find_char('C')[0], pice.find_char('C')[1]))

# Making Window ----------------------------------------------------------------
win = GraphWin('Tree Plnting Land Management', pice.width*20, pice.height*24)
win.setBackground('black')


"""
if __name__ == '__main__':

    # Gathers information
    pice = Path(input('Imput pice URL: '))
    bag_size = input('Imput size of bag-ups: ')

    while (not (bag_size.isdigit() and int(bag_size) == float(bag_size))) or \
            not (pice.is_file()):  # checks validity of information
        print('\n Invalid Input \n')
        pice = Path(input('Imput pice URL: '))
        bag_size = input('Imput size of bag-ups: ')

    # Read File
"""