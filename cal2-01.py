import pylab
import numpy


def P(x, n):
    s = 0
    for k in range(n+1):
        s += (numpy.power(-1, numpy.floor(k/2))) * (numpy.power(x, k) / numpy.math.factorial(k))
    return s



a, b, m = 0, 3 * numpy.pi, 100
xs = numpy.linspace(a,b,m)



for i in range(1, 21, 2):
    pylab.plot(xs, P(xs, i), label='P' + str(i))


pylab.plot(xs, pylab.sin(xs) + pylab.cos(xs), label='sin(x)+cos(x)')

pylab.title('Taylor polynomials with different order for sin(x)+cos(x)')
pylab.legend()
pylab.xlabel('X')
pylab.ylabel('Y')
pylab.ylim(-2,2)
pylab.grid()
pylab.show()
