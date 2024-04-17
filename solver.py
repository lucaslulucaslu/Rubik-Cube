#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import bisect
from random import choice, randint

class RubiksCube:
    def __init__(self, parent=None, cubeString=None, cube=None, parentOperation=[0,0,0]):
        self.n = 3
        self.colors = ["w", "o", "g", "r", "b", "y"]
        self.parent = parent
        self.parentOperation = parentOperation
        if cubeString is None:
            self.cube = []
        else:
            self.cube = [
                [[cubeString[z * 9 + y * 3 + x] for x in range(3)] for y in range(3)]
                for z in range(6)
            ]
        self.f = 0
        self.h = 0
        self.g = 0

    def __lt__(self, other):
        return self.f < other.f

    def reset(self):
        self.cube = [
            [[color for x in range(self.n)] for y in range(self.n)]
            for color in self.colors
        ]

    def stringify(self):
        return "".join([i for r in self.cube for s in r for i in s])

    def show(self):
        spacing = f'{" " * (len(str(self.cube[0][0])) + 2)}'
        l1 = "\n".join(spacing + str(c) for c in self.cube[0])
        l2 = "\n".join(
            "  ".join(str(self.cube[i][j]) for i in range(1, 5))
            for j in range(len(self.cube[0]))
        )
        l3 = "\n".join(spacing + str(c) for c in self.cube[5])
        print(f"{l1}\n\n{l2}\n\n{l3}")

    def turn90(self, channel, direction):
        # channel 0-3, direction 1 clockwise, 2 counter clockwise
        if channel == 0:
            if direction == 1:
                self.cube[1][0], self.cube[2][0], self.cube[3][0], self.cube[4][0] = (
                    self.cube[2][0],
                    self.cube[3][0],
                    self.cube[4][0],
                    self.cube[1][0],
                )
                self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]
            elif direction == 2:
                self.cube[1][0], self.cube[2][0], self.cube[3][0], self.cube[4][0] = (
                    self.cube[4][0],
                    self.cube[1][0],
                    self.cube[2][0],
                    self.cube[3][0],
                )
                self.cube[0] = [list(x) for x in zip(*(self.cube[0]))][::-1]
        elif channel == 1:
            if direction == 1:
                self.cube[1][2], self.cube[2][2], self.cube[3][2], self.cube[4][2] = (
                    self.cube[4][2],
                    self.cube[1][2],
                    self.cube[2][2],
                    self.cube[3][2],
                )
                self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))]
            elif direction == 2:
                self.cube[1][2], self.cube[2][2], self.cube[3][2], self.cube[4][2] = (
                    self.cube[2][2],
                    self.cube[3][2],
                    self.cube[4][2],
                    self.cube[1][2],
                )
                self.cube[5] = [list(x) for x in zip(*(self.cube[5]))][::-1]
        elif channel == 2:
            if direction == 1:
                for i in range(self.n):
                    (
                        self.cube[0][i][0],
                        self.cube[2][i][0],
                        self.cube[4][-i - 1][-1],
                        self.cube[5][i][0],
                    ) = (
                        self.cube[4][-i - 1][-1],
                        self.cube[0][i][0],
                        self.cube[5][i][0],
                        self.cube[2][i][0],
                    )
                self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]
            elif direction == 2:
                for i in range(self.n):
                    (
                        self.cube[0][i][0],
                        self.cube[2][i][0],
                        self.cube[4][-i - 1][-1],
                        self.cube[5][i][0],
                    ) = (
                        self.cube[2][i][0],
                        self.cube[5][i][0],
                        self.cube[0][i][0],
                        self.cube[4][-i - 1][-1],
                    )
                self.cube[1] = [list(x) for x in zip(*(self.cube[1]))][::-1]
        elif channel == 3:
            if direction == 1:
                for i in range(self.n):
                    (
                        self.cube[0][i][2],
                        self.cube[2][i][2],
                        self.cube[4][-i - 1][-3],
                        self.cube[5][i][2],
                    ) = (
                        self.cube[2][i][2],
                        self.cube[5][i][2],
                        self.cube[0][i][2],
                        self.cube[4][-i - 1][-3],
                    )
                self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]
            elif direction == 2:
                for i in range(self.n):
                    (
                        self.cube[0][i][2],
                        self.cube[2][i][2],
                        self.cube[4][-i - 1][-3],
                        self.cube[5][i][2],
                    ) = (
                        self.cube[4][-i - 1][-3],
                        self.cube[0][i][2],
                        self.cube[5][i][2],
                        self.cube[2][i][2],
                    )
                self.cube[3] = [list(x) for x in zip(*(self.cube[3]))][::-1]

    def flip90(self, orient, direction):
        # orient 0 vertial 1 horizontal, direction 1 顺手 2 逆手
        if orient == 0:
            if direction == 1:
                self.cube[0], self.cube[2], self.cube[4], self.cube[5] = (
                    self.cube[2],
                    self.cube[5],
                    self.cube[0],
                    self.cube[4],
                )
                # 左右两面旋转
                self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]
                self.cube[1] = [list(x) for x in zip(*(self.cube[1]))][::-1]
                # 与背面相关的转后需要倒序一次
                self.cube[4] = [
                    [y for y in reversed(x)] for x in reversed(self.cube[4])
                ]
                self.cube[5] = [
                    [y for y in reversed(x)] for x in reversed(self.cube[5])
                ]
            elif direction == 2:
                self.cube[0], self.cube[2], self.cube[4], self.cube[5] = (
                    self.cube[4],
                    self.cube[0],
                    self.cube[5],
                    self.cube[2],
                )
                self.cube[3] = [list(x) for x in zip(*(self.cube[3]))][::-1]
                self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]
                self.cube[4] = [
                    [y for y in reversed(x)] for x in reversed(self.cube[4])
                ]
                self.cube[0] = [
                    [y for y in reversed(x)] for x in reversed(self.cube[0])
                ]
        elif orient == 1:
            if direction == 1:
                self.cube[1], self.cube[2], self.cube[3], self.cube[4] = (
                    self.cube[4],
                    self.cube[1],
                    self.cube[2],
                    self.cube[3],
                )
                self.cube[0] = [list(x) for x in zip(*(self.cube[0]))][::-1]
                self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))]
            elif direction == 2:
                self.cube[1], self.cube[2], self.cube[3], self.cube[4] = (
                    self.cube[2],
                    self.cube[3],
                    self.cube[4],
                    self.cube[1],
                )
                self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]
                self.cube[5] = [list(x) for x in zip(*(self.cube[5]))][::-1]
def hValue(state, targetFace):
    cornerWeight = 2
    edgeWeight = 4
    for i in range(len(state)):
        if state[i][1][1] == targetFace[1][1]:
            stateFace = state[i]
            break
    minH = (cornerWeight + edgeWeight) * 4
    for i in range(3):
        temp = (cornerWeight + edgeWeight) * 4
        for x in range(3):
            for y in range(3):
                if stateFace[x][y] == targetFace[x][y] and not (x == 1 and y == 1):
                    if (x + y) % 2 == 0:
                        temp = temp - cornerWeight
                    else:
                        temp = temp - edgeWeight
        if temp == 0:
            return 0
        if temp < minH:
            minH = temp
        stateFace = [list(x) for x in zip(*reversed(stateFace))]
    return minH

def solve(startCube, targetFace):
    trys = 0
    open_list_Limit = 5000
    startCube.h = hValue(startCube.cube, targetFace)
    startCube.f = startCube.h
    open_list = [startCube]
    close_list = set()
    while len(open_list) > 0:
        #open_list=open_list[0:open_list_Limit]
        trys = trys + 1
        currentCube = open_list[0]
        open_list.pop(0)
        close_list.add(currentCube.stringify())
        if currentCube.h == 0:
            path = []
            operations=[]
            current = currentCube
            while current is not None:
                path.append(current.stringify())
                operations.append(current.parentOperation)
                current = current.parent
            return [trys,path[::-1],operations[::-1]]
        for i in range(4):
            for j in range(1,3):
                child = RubiksCube(cubeString=currentCube.stringify())
                child.turn90(i, j)
                if child.stringify() not in close_list:
                    child.parent = currentCube
                    child.parentOperation = [1,i,j]
                    child.g = currentCube.g + 1
                    child.h = hValue(child.cube, targetFace)
                    child.f = child.g + child.h
                    bisect.insort_left(open_list,child)
                    if len(open_list)>open_list_Limit:
                        open_list.pop()
        for i in range(1):
            for j in range(1,3):
                child = RubiksCube(cubeString=currentCube.stringify())
                child.flip90(i, j)
                if child.stringify() not in close_list:
                    child.parent = currentCube
                    child.parentOperation = [2,i,j]
                    child.g = currentCube.g + 1
                    child.h = hValue(child.cube, targetFace)
                    child.f = child.g + child.h
                    bisect.insort_left(open_list,child)
                    if len(open_list)>open_list_Limit:
                        open_list.pop()
    return False


# In[ ]:


start_time = time.time()
cube = RubiksCube()
cube.reset()
#target = [['y', 'y', 'y'], ['y', 'b', 'y'], ['g', 'y', 'y']]#~9s
#target=[['y', 'w', 'y'], ['b', 'y', 'b'], ['y', 'b', 'y']] #~15s
#target=[['o', 'b', 'o'], ['o', 'g', 'r'], ['o', 'y', 'o']] #~12s
#target=[['b', 'r', 'w'], ['r', 'b', 'b'], ['b', 'r', 'y']] #~5s
target=[['g', 'r', 'b'], ['r', 'w', 'r'], ['g', 'r', 'w']] #86s
[trys, path, operations] = solve(cube, target)
print("Time: %.2f" % (time.time() - start_time))
for i in range(len(path)):
    print(path[i] + " - " + "".join([str(i) for i in operations[i]]) + "\n")


# In[ ]:


#test random 500 target cubes, calcuate average time for solve one cube
n = 500
minTime = 2000
maxTime = 0
totalTime = 0
totalSteps=0
for i in range(n):
    start_time = time.time()
    cube = RubiksCube()
    cube.reset()
    target = [[choice(cube.colors) for x in range(3)] for y in range(3)]
    
    [trys, path, operations]=solve(cube, target)
    diffTime = time.time() - start_time
    print(str(target)+' - Time: %.2f'%diffTime+' - trys: '+str(trys)+' - Steps: '+str(len(path)))
    if minTime > diffTime:
        minTime = diffTime
    if maxTime < diffTime:
        maxTime = diffTime
    totalTime = totalTime + diffTime
    totalSteps=totalSteps+len(path)
print(
    "maxTime: %.2f" % (maxTime)
    + " / minTime: %.2f" % (minTime)
    + " / avgTime: %.2f" % (totalTime / n)
    + " / avgStep: %.2f" % (totalSteps/n)
)


# In[ ]:




