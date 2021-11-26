# waffle
Spinning waffle from waffle shaped python code

Based on a parametric curve: 

`r(t) = 2 - 2*sin(t) + (sin(t)*abs(cos(t)))/(sin(t) + 1.4)`

projected on to x/y coordinates with sin and cos. 

sin and cos are found by taylor expanding, with 69 terms. Easily expandable if you find where in the code to change it.
The terms' factorials are precalculated using recursion, put into a list, and fetched when needed from the list.

To draw the function, a 20x40 grid of points are used. 100 points on the parametric curve is used for distance calculation.
For each raster point, the distance to each of the 69 parametric points is calculated. If it is less than some value (0.1 works nicely),
then the point is represented with an x. Otherwise, it represented with a space. 

A basic os-check is performed, to figure out is `clear` or `cls` will clear the console.

pi = 3.1416

To rotate the waffle, the x- and y- coordinates are multiplied by the rotation matrix in the xy (i.e. screen)- plane (around the z-axis). Additionally, the waffle rotates around the y- axis (multiplying the x-coordinates with cos(time)).
