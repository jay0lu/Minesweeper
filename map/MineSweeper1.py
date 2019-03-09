#!/usr/bin/python
# coding:utf-8
# python Minesweeper

from __future__ import print_function
import sys
import random

# NotSure --> not reveal, but mine is not here
# Mine ---> not revel, but mine is here
# number --> reveled, mine nearby
# Cleaned --> reveled, mine not nearby


class Minesweeper:
    # initialize
    def __init__(self, row=5, cols=5, mineNum=10):
        self.row = row
        self.cols = cols
        self.score = 0
        self.mineNum = mineNum
        self.minemap = []
        self.initData()
        self.endGame = 0

    def initData(self):
        for i in range(self.row):
            each_row = []
            for ii in range(self.cols):
                each_row.append("NotSure")
            self.minemap.append(each_row)
        mineLeft = self.mineNum
        while mineLeft > 0:
            random_x = random.randint(0, self.row-1)
            random_y = random.randint(0, self.cols-1)
            if self.minemap[random_x][random_y] != "Mine":
                self.minemap[random_x][random_y] = "Mine"
                print("Set " + str(random_x) + "|" + str(random_y) + " mine...", end="")
                mineLeft -= 1

    def stillInRange(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.cols

    # Clean mine
    def mine_clear(self, click_x, click_y):
        print("Mine clearing for " + str(click_x) + "|" + str(click_y))
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        if self.minemap[click_x][click_y] == "Mine":
            self.endGame = True
            print("Trigger Mine!!! Game Over!!!")
            sys.exit()
        else:
            nearby_mine = 0
            for each_step in steps:
                if self.stillInRange(click_x+each_step[0], click_y+each_step[1]) and self.minemap[click_x+each_step[0]][click_y+each_step[1]] == "Mine":
                    nearby_mine += 1
            print(nearby_mine)
            if nearby_mine > 0:
                self.minemap[click_x][click_y] = nearby_mine
            else:
                self.minemap[click_x][click_y] = "Cleaned"
                nearby_cubes = []
                for each_neighbour_step in steps:
                    neighbour_x = click_x + each_neighbour_step[0]
                    neighbour_y = click_y + each_neighbour_step[1]
                    # only NotSure could be added into tree, otherwise infinite branch
                    if self.stillInRange(neighbour_x, neighbour_y) and self.minemap[neighbour_x][neighbour_y] == "NotSure":
                        nearby_cubes.append([neighbour_x, neighbour_y])
                        self.mine_clear(neighbour_x, neighbour_y)

    # display world
    def display_mineWorld(self):
        print("=" * 20)
        for each_row in self.minemap:
            for each_col in each_row:
                if each_col == "NotSure" or each_col == "Mine":
                    print("# ", end="")
                elif isinstance(each_col, int):
                    print(str(each_col) + " ", end="")
                elif each_col == "Cleaned":
                    print("O ", end="")
            print("\n")
        print("=" * 20)

    def gaming(self):
        while not self.endGame:
            self.display_mineWorld()
            p_x = int(raw_input("Enter row number:"))
            p_y = int(raw_input("Enter cols number:"))
            self.mine_clear(p_x, p_y)
            self.if_win()
            if self.endGame:
                print("Congratulation! You Win")
                self.display_mineWorld()
                sys.exit()

    # Check if win
    def if_win(self):
        for each_row in self.minemap:
            for each_cols in each_row:
                if each_cols == "NotSure":
                    return
        self.endGame = True


if __name__ == '__main__':
    ms = Minesweeper(5, 5, 2)
    ms.gaming()

