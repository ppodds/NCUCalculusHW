import pylab
import numpy

a, b, m = 0, 100 * numpy.pi, 10000
angs = pylab.linspace(a, b, m)

rs = pylab.cos(numpy.pi * angs)

pylab.polar(angs, rs)

pylab.title('graph of cos(pi x) for x in [0,100pi] using 10000 points')

pylab.show()
