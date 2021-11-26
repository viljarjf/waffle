0;             xr,                      yr=\
         (lambda x0,xn,            y0, yn,n:([x0+i
      *(xn-x0)/(2*n) for        i in range(2*n+1)],[y0
    + i*(yn - y0)/n for i in range(n+1)]))(-2.5,2.5,-2.5
  ,2.5, 20);ff = lambda t: t*ff(t-1) if t>1 else 1;fs=[ff(
i)for i in range(200)];f=lambda t: fs[t];sin=lambda t:sum([
(t)**(2*n+1)*(-1)**n /f(2*n + 1) for n in range(69)]);cos=\
lambda t: sum([(t)**(2*n) *(-1)**n / f(2*n) for n in range(
 69)]);r= lambda t: 0.9*(2 - 2*sin(t)+(sin(t)*abs(cos(t)))
  /(sin(t) +1.4));xg=lambda t:r(t)*cos(t);yg=lambda t:r(t
   )*sin(t);d =lambda x,y,x0,y0,t:((x(t)-x0)**2+(y(t)-y0
    )**2)**0.5;pl= lambda x,y,y0,t:"".join([" " if d0 >
     0.17 else "x"for d0 in[min([d(x,y,x0,y0,t0)for t0
      in t]) for x0 in xr]]);t=(lambda n:[-3.1416 + i
       *(3.1416 - -3.1416)/n for i in range(n+1)])(69
       );ys = [yg(t0) for t0 in t]; from os import \
        system as s;c = "cls" if not s("cls") else\
         "clear";[(lambda xs, cf, sf:(lambda x, y:
          print("\n".join(([pl(lambda t0:cf*(x(t0
           )*cf - y(t0)*sf), lambda t0:(x(t0)*sf
            +y(t0)*cf),y0,t)for y0 in reversed(
             yr)]+[s(c)])[:-1])))(lambda t0: \
              xs[t.index(t0)],lambda t0:1.7+\
               ys[t.index(t0)]))([xg(t0)for\
                t0 in t],cos(fr),sin(fr)) \
                 for fr in [(0.3*i)%6.2832 
                  for i in range(1000)]]
                   # the code took too 
                    # little space to
                     #completely fill
                      # the wedge of
                       # the waffle
                        # so I had
                         # to add
                          # this
                           # :)
