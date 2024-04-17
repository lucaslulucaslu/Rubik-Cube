# Rubik-Cube
automatic Rubik's Cube solve robot, hardware and software

### I want to make a Rubik's cube Mosaics art
like this one

![The Last Supper – Josh Chalom](https://ruwix.com/pics/art/mosaics/last-supper-rubiks-cube-mosaic.jpg)

But I want it bigger, so I desgined one with 2560 cubes (64\*40), I want each cube be remove/changable at any time, so I designed a supporting system like below


Then I have a issue that I have to turn each cube to a given state, I tried this at first, and I even learned Beginer's method, However there is no easy way to turn a cube to a any given state, if I do it hard way like most cube mosaic artist do, it takes weeks even months to finish my design, so I have to build a robot do this for me. After exploring this topic a little I found there is even no as-is solution for this, because most people build cube robot to turn back to initial state instead of to a given state. OK, so I not only have to build the robot but also the algorithm. Luckily there is one solution for hardware https://www.rcr3d.com/index.html
Frames can be 3D printed, just several servo motors and screws we can have a fully funcitonal cube robot.
Then the hard part - Algorithm, after a little research I choose to use A\* algorithm to search for fastest solve, everything is in solver.py file, I will add commments later.

## Video shows from an initial state to a given state
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/pOypncBmyBM/sddefault.jpg)](https://www.youtube.com/shorts/pOypncBmyBM)
## Video shows from above given state back to initial state
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yvKblBVN4P4/sddefault.jpg)](https://www.youtube.com/shorts/yvKblBVN4P4)
