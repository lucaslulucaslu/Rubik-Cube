# Rubik-Cube
automatic Rubik's Cube robot, hardware and software, before any explaination let's see what I finally got.

## Video shows from an initial state to a given state
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/pOypncBmyBM/sddefault.jpg)](https://www.youtube.com/shorts/pOypncBmyBM)
## Video shows from above given state back to initial state
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yvKblBVN4P4/sddefault.jpg)](https://www.youtube.com/shorts/yvKblBVN4P4)

### I want to make a Rubik's cube Mosaics art
like this one

![The Last Supper – Josh Chalom](https://ruwix.com/pics/art/mosaics/last-supper-rubiks-cube-mosaic.jpg)

Because of my game room' wall limitation, my project involves using 2560 cubes arranged in a 64x40 grid. Each cube should be able to individually removed or changed, so they are supported by a specially designed system.

![supoort system - individual](support/cube-support-individual.jpg)
![support system - assembly](support/cube-support-assembly.jpg)

However, a significant challenge arose in manipulating each cube to achieve a specific configuration. Initially, I tried using the Beginner's method of cube solving, but quickly realized that manually adjusting each cube to a desired state (even for 1 face) was impractical—it could take weeks or even months. Unlike most cube-solving robots, which are designed to reset a cube to its original state, my project requires a robot capable of arranging cubes into any specified configuration.

After some research, I found that there wasn't a ready-made solution for this unique requirement. This realization led me to not only design and build the robot but also develop the necessary algorithm. I discovered a hardware solution at RCR3D(https://www.rcr3d.com/index.html), which offers 3D printable frames that, combined with several servo motors and screws, allow for the construction of a functional cube robot.

For the algorithm, after evaluating different methods, I opted to use the A\* algorithm to determine the quickest solution. The entire code, including this algorithm, is encapsulated in a 'solver.py' file. I plan to enhance this file with detailed comments to aid in understanding and modifying the program. The average solving time is around several minutes at the beginning, by set search queue length limit, I managed to decrease this down to 2s, so the algorithm may not find the best solution, but solve the cube much faster, I would accept this trade off.
![Rubik's cube initial state](cube-initial-state.jpg)
