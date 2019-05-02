from random import randint, random

class Board:
    def __init__(self):
        self.mat = [[0 for _ in range(3)] for _ in range(3)]

        for _ in range(2):
            (r, c) = self.get_random_field()
            self.mat[r][c] = 2

    def step(self, dir):
        '''
        Moves all fields in the direction specified by dir and adds the adjacent ones if they are equal

        direction:
            0 - up
            1 - down
            2 - left
            3 - right
        '''

        self.mat = self.move(dir, self.mat)
        self.mat = self.add(dir)
        self.generate_field()

    def move(self, dir, mat):
        '''
        Moves all fields in a given matrix in a direction given by dir 
        (int, [[int]]) -> [[int]]
        '''
        steps = [ (-1, 0), (1, 0), (0, -1), (0, 1) ] # up, down, left, right
        loop = [ (0, 3, 1), (2, -1, -1) ]

        (s, e, st) = loop[dir%2]

        result = [row[:] for row in mat]

        for row in range(s, e, st):
            for col in range(s, e, st):
                if not result[row][col]:
                    continue
                (row_step, col_step) = steps[dir]
                r = row
                c = col

                if self.in_moving_bounds(r, c, dir):
                    r += row_step
                    c += col_step

                    if result[r][c]:
                        continue

                while not result[r][c] and self.in_moving_bounds(r, c, dir):
                    r += row_step
                    c += col_step

                if result[r][c] and (r != row or c != col):
                    r -= row_step
                    c -= col_step

                #print('({}, {}) -> ({}, {})'.format(row, col, r, c))

                if r != row or c != col:
                   # print('Moving')
                    result[r][c] = result[row][col]
                    result[row][col] = 0

        return result
    def add(self, dir):
        '''
        Adds adjacent fields of the same value in a direction given by dir
        '''
        steps = [ (-1, 0), (1, 0), (0, -1), (0, 1) ] # up, down, left, right
        loop = [ (0, 3, 1), (2, -1, -1) ]

        (s, e, st) = loop[dir%2]

        result = [row[:] for row in self.mat]

        for row in range(s, e, st):
            for col in range(s, e, st):
                (row_step, col_step) = steps[dir]

                next_row = row + row_step
                next_col = col + col_step

                if self.in_adding_bounds(next_row, next_col) and result[next_row][next_col] == result[row][col]:
                    result[next_row][next_col] *= 2
                    result[row][col] = 0
                    self.mat = result
                    result = self.move(dir, result)

        return result

    def generate_field(self):
        '''
        Generates a new value in a random field
        4 is generated 10% of the time with the rest being 2
        '''

        (r, c) = self.get_random_field()

        while self.mat[r][c]:
            (r, c) = self.get_random_field()

        if random() > 0.9:
            self.mat[r][c] = 4
        else:
            self.mat[r][c] = 2

    '''
    Helpers
    '''
    def get_random_field(self):
        '''
        Generates a random row and column
        '''
        r = randint(0, 2)
        c = randint(0, 2)

        return (r, c)

    def in_moving_bounds(self, r, c, dir):
        '''
        Checks if a field given by r and c can be moved according to dir 
        '''

        if dir == 0:
            return (r > 0 and r <= 2)
        elif dir == 1:
            return (r >= 0 and r < 2)
        elif dir == 2:
            return (c > 0 and c <= 2)
        elif dir == 3:
            return (c >= 0 and c < 2)
    
    def in_adding_bounds(self, r, c):
        return r >= 0 and r <= 2 and c >= 0 and c <= 2