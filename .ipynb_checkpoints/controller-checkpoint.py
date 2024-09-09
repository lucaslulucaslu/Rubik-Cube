#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import maestro
import solver


# In[2]:


servo = maestro.Controller("COM7")


# In[3]:


UpDownChannels = [0, 1, 2, 3]
RotateChannels = [6, 7, 8, 9]
UpDownPositions = [[2000, 2000, 2000, 2000], [1160, 1000, 1140, 1060]]
RotatePositions = [
    [1430, 1660, 1460, 1560],
    [2110, 2260, 2120, 2200],
    [730, 980, 780, 900],
]
for i in range(10):
    servo.setAccel(i, 110)


# In[4]:


def armReady(channel, position):
    while position != servo.getPosition(channel):
        time.sleep(0.1)


# In[5]:


def armRelease():
    for i in range(4):
        servo.setTarget(RotateChannels[i], 4 * RotatePositions[0][i])
        armReady(RotateChannels[i], 4 * RotatePositions[0][i])
    for i in range(3, -1, -1):
        servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[0][i])
        armReady(UpDownChannels[i], 4 * UpDownPositions[0][i])


# In[6]:


def armHold():
    for i in range(4):
        servo.setTarget(RotateChannels[i], 4 * RotatePositions[0][i])
        armReady(RotateChannels[i], 4 * RotatePositions[0][i])
    for i in range(4):
        servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[1][i])
        armReady(UpDownChannels[i], 4 * UpDownPositions[1][i])


# In[8]:


def turn90(channle, direction):
    # channel0-3, direction 1 clockwise, 2 counter clockwise
    if direction == 1:
        offset = 180
    else:
        offset = -180
    servo.setTarget(
        RotateChannels[channle], 4 * RotatePositions[direction][channle] + offset
    )
    armReady(RotateChannels[channle], 4 * RotatePositions[direction][channle] + offset)
    time.sleep(0.1)
    servo.setTarget(UpDownChannels[channle], 4 * UpDownPositions[0][channle])
    armReady(UpDownChannels[channle], 4 * UpDownPositions[0][channle])
    servo.setTarget(RotateChannels[channle], 4 * RotatePositions[0][channle])
    armReady(RotateChannels[channle], 4 * RotatePositions[0][channle])
    #time.sleep(0.1)
    servo.setTarget(UpDownChannels[channle], 4 * UpDownPositions[1][channle])
    armReady(UpDownChannels[channle], 4 * UpDownPositions[1][channle])
    time.sleep(0.1)


def flip90(orient, direction):
    # orient 0 vertical / 1 horizontal, direction 1 顺手 2 逆手
    if orient == 0:
        servo.setTarget(UpDownChannels[2], 4 * UpDownPositions[0][2])
        armReady(UpDownChannels[2], 4 * UpDownPositions[0][2])
        servo.setTarget(RotateChannels[2], 4 * RotatePositions[direction][2])
        armReady(RotateChannels[2], 4 * RotatePositions[direction][2])
        time.sleep(0.1)
        servo.setTarget(UpDownChannels[2], 4 * UpDownPositions[1][2])
        armReady(UpDownChannels[2], 4 * UpDownPositions[1][2])
        for i in range(0, 2):
            servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[0][i])
            armReady(UpDownChannels[i], 4 * UpDownPositions[0][i])

        servo.setTarget(RotateChannels[2], 4 * RotatePositions[0][2])
        servo.setTarget(RotateChannels[3], 4 * RotatePositions[direction][3])
        armReady(RotateChannels[2], 4 * RotatePositions[0][2])
        armReady(RotateChannels[3], 4 * RotatePositions[direction][3])
        time.sleep(0.1)
        
        for i in range(0, 2):
            servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[1][i])
            armReady(UpDownChannels[i], 4 * UpDownPositions[1][i])

        servo.setTarget(UpDownChannels[3], 4 * UpDownPositions[0][3])
        armReady(UpDownChannels[3], 4 * UpDownPositions[0][3])
        servo.setTarget(RotateChannels[3], 4 * RotatePositions[0][3])
        armReady(RotateChannels[3], 4 * RotatePositions[0][3])
        time.sleep(0.1)
        servo.setTarget(UpDownChannels[3], 4 * UpDownPositions[1][3])
        armReady(UpDownChannels[3], 4 * UpDownPositions[1][3])
        time.sleep(0.1)
    elif orient == 1:
        servo.setTarget(UpDownChannels[0], 4 * UpDownPositions[0][0])
        armReady(UpDownChannels[0], 4 * UpDownPositions[0][0])
        servo.setTarget(RotateChannels[0], 4 * RotatePositions[direction][0])
        armReady(RotateChannels[0], 4 * RotatePositions[direction][0])
        time.sleep(0.1)
        servo.setTarget(UpDownChannels[0], 4 * UpDownPositions[1][0])
        armReady(UpDownChannels[0], 4 * UpDownPositions[1][0])

        for i in range(2, 4):
            servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[0][i])
            armReady(UpDownChannels[i], 4 * UpDownPositions[0][i])

        servo.setTarget(RotateChannels[0], 4 * RotatePositions[0][0])
        servo.setTarget(RotateChannels[1], 4 * RotatePositions[direction][1])
        armReady(RotateChannels[0], 4 * RotatePositions[0][0])
        armReady(RotateChannels[1], 4 * RotatePositions[direction][1])
        time.sleep(0.1)

        for i in range(2, 4):
            servo.setTarget(UpDownChannels[i], 4 * UpDownPositions[1][i])
            armReady(UpDownChannels[i], 4 * UpDownPositions[1][i])
        time.sleep(0.1)

        servo.setTarget(UpDownChannels[1], 4 * UpDownPositions[0][1])
        armReady(UpDownChannels[1], 4 * UpDownPositions[0][1])
        servo.setTarget(RotateChannels[1], 4 * RotatePositions[0][1])
        armReady(RotateChannels[1], 4 * RotatePositions[0][1])
        time.sleep(0.1)
        servo.setTarget(UpDownChannels[1], 4 * UpDownPositions[1][1])
        armReady(UpDownChannels[1], 4 * UpDownPositions[1][1])
        time.sleep(0.1)


# In[ ]:


start_time = time.time()
cube = solver.RubiksCube()
cube.reset()
#target = [["g", "b", "y"], ["w", "g", "o"], ["y", "b", "y"]]
target = [["r", "g", "b"], ["o", "r", "w"], ["o", "o", "b"]]
[trys, path, operations] = solver.solve(cube, target)
print("Solve time: %.2f" % (time.time() - start_time))
for i in range(len(path)):
    print(path[i] + " - " + "".join([str(i) for i in operations[i]]) + "\n")


# In[17]:


for i in range(1,len(operations)):
    if operations[i][0]==1:
        turn90(operations[i][1],operations[i][2])
    elif operations[i][0]==2:
        flip90(operations[i][1],operations[i][2])


# In[18]:


for i in range(len(operations)-1,0,-1):
    if operations[i][0]==1:
        turn90(operations[i][1],3-operations[i][2])
    elif operations[i][0]==2:
        flip90(operations[i][1],3-operations[i][2])


# In[15]:


#armRelease()


# In[16]:


#armHold()


# In[11]:


#servo.close()


# In[ ]:




