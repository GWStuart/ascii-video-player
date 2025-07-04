from os import get_terminal_size
import random
import time

class MatrixHandler:
    def __init__(self, path):
        self.path = path
        self.columns = get_terminal_size().columns
        self.rows = get_terminal_size().lines

        # grid stores matrix tiles as an array of rows
        self.grid = ["-"*self.columns for _ in range(self.rows)]

        self.init = True  # set to False when initial animation is finished
        self.lengths = [0]*self.columns  # length of each respective column

    def update(self):
        if self.init:
            for row in range(self.rows):
                new_row = ""
                for column in range(self.columns):
                    if row == self.lengths[column] and random.randint(1, 10) == 1:
                        new_row += "a"
                        self.lengths[column] += 1
                    else:
                        new_row += self.grid[row][column]
                self.grid[row] = new_row

    def render(self):
        print("\033c")
        if self.init:
            for row in self.grid:
                print("".join(row))



m = MatrixHandler("")
for i in range(50):
    m.update()
    m.render()
    time.sleep(0.2)
