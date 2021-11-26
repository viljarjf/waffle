# x-range and y-range
# 20 lines, 40 characters per line
# x and y range from -2.5 to 2.5
xr, yr = (lambda x0, xn, y0, yn, n: (
    [x0 + i*(xn - x0)/(2*n) for i in range(2*n+1)],
    [y0 + i*(yn - y0)/n for i in range(n+1)]
    ))(-2.5, 2.5, -2.5, 2.5, 20)

# factorial factory, with recursion
ff = lambda t: t*ff(t-1) if t > 1 else 1
# list of factorials, to save computation later
fs = [ff(i) for i in range(200)]
# fetch factorials from the list
f = lambda t: fs[t]

# taylor expand sin and cos, 69 terms
sin = lambda t: sum([(t)**(2*n+1)*(-1)**n /f(2*n + 1) for n in range(69)])
cos = lambda t: sum([(t)**(2*n)*(-1)**n / f(2*n) for n in range(69)])

# r(theta), defining the curve to plot
r = lambda t: 0.9*(2 - 2*sin(t) + (sin(t)*abs(cos(t)))/(sin(t) + 1.4))

# x- and y-generators, transforming the r(theta) curve to cartesian coordinates
xg = lambda t: r(t)*cos(t)
yg = lambda t: r(t)*sin(t)

# distance function. 
# params: 
#   x: function of t, x coordinate of curve
#   y: function of t, y coordinate of curve
#   x0, x coordinate of a point to find distance to curve from
#   y0, y coordinate of a point to find distante to curve from
#   t0, time to evaluate the x- and y- functions
d = lambda x, y, x0, y0, t: ((x(t) - x0)**2 + (y(t) - y0)**2)**0.5

# get a string of a line of data to draw.
# params:
#   x: see above
#   y: see above
#   y0: see above
#   t: theta values where the parametric curve will be evaluated
# for all x-values x0 in the x-range list, calculate the distance from the point (x0, y0) to all parametric points (x(t), y(t)),
# and if the smallest distance calculated is less than 0.1, then the point is represented with an "x".
# otherwise, it is represented with a " ".
pl = lambda x, y, y0, t: "".join([" " if d0 > 0.1 else "x" for d0 in [min([d(x, y, x0, y0, t0) for t0 in t]) for x0 in xr]])

# list of theta values to calculate the parametric curve values for
t = (lambda n: [-3.1416 + i*(3.1416 - -3.1416)/n for i in range(n+1)])(70)

# y-values from the y-generator. Calculate them now to speed up processing later
ys = [yg(t0) for t0 in t]

# do a quick OS-check to figure out if "clear" or "cls" will clear the console
from os import system as s
c = "cls" if not s("cls") else "clear"

# loop to draw the heart
# input: generated x-values from the x-generator, cosine factor and sine factor
[[(lambda xs, cf, sf:(lambda x, y:

# call the line plot function and combine them.
# the y-coordinates are reversed since drawing is top first.
# the input x- and y-values are rotated over time by multiplying by the rotation matrix.
# i.e. x = (x*cos(time) - y*sin(time)), y = (x*sin(time) + y*cos(time))
# to make the rotation more interesting, the x-coordinate is further multiplied by cos(time),
# which is equivalent to rotating it along the y-axis (where the screen is the x-y-plane) and projecting onto the screen
print("\n".join(([pl(lambda t0: cf*(x(t0)*cf - y(t0)*sf), lambda t0: (x(t0)*sf + y(t0)*cf), y0,t) for y0 in reversed(yr)]+[s(c)])[:-1]))
# call with calculated x- and y- values, reduces computation
)(lambda t0: xs[t.index(t0)], lambda t0: 1.7 + ys[t.index(t0)])
# fr is a stand-in for time passing. It ranges from 0 to 2pi on a loop.
)([xg(t0) for t0 in t], cos(fr), sin(fr)) for fr in [(0.3*i)%6.2832 for i in range(63)]] for _ in iter(int, 1)]
