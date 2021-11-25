0;              xrange =                  [-2.5 + 
            i*(2.5 - -2.5)             /(40) for i\
        in range(41)];yr=[         -4.2 + i*(0.8 - -4.2)
    /20 for i in range(21)];ff=lambda t: t*ff(t-1) if t \
   >1 else 1;fs=[ff(i) for i in range(25)];f=lambda t:fs[t]
sin = lambda t: sum([(t)**(2*n+1)*(-1)**n /f(2*n + 1) for n\
in range(10)]);cos = lambda t:sum([(t)**(2*n)*(-1)**n / f(2*n) 
for n in range(10)]);r = lambda t: 2 - 2*sin(t) + (sin(t)*abs(
cos(t)))/(sin(t) + 1.4);xg=lambda t:r(t)*cos(t);yg=lambda t: r(t
)*sin(t);dist = lambda x0, y0, t: ((x(t) - x0)**2 + (y(t)-y0)**
2)**0.5;plotline = lambda y0, t: "".join([" " if d > 0.1 else 
 "x"for d in [min([dist(x0, y0, t0) for t0 in t]) for x0 in 
   xrange]]);t = [-3.1416 + i*(3.1416 - -3.1416)/100 for
     i in range(100 + 1)];fr = 0;ys = [yg(t0) for t0 in 
    t];from os import system as s;c = "cls" if not s(
       "cls") else "clear";y = lambda t0: ys[t.index(
          t0)]; # hackety hack, while true is whack
while True:xs = [xg(t0) for t0 in t]; cf = cos(fr
             );x=lambda t0:xs[t.index(t0)]*cf;\
               print("\n".join(([plotline(y0,
                 t) for y0 in reversed(yr)] 
                   + [s(c)])[:-1]));fr \
                       += 0.3;fr %= \
                           3.1416