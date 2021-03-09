import pylab

a = 0
b = 10 * pylab.pi
n = 1001

dx = (b - a) / (n - 1)


def get_max(x):
    if 1 > x:
        return 1
    return x


xs = [a + i * dx for i in range(n)]
ys = [(pylab.cos(x) ** 2) / pylab.sqrt(get_max(x)) for x in xs]

pylab.plot(xs, ys)
pylab.title(r'$\mathtt{f(x) = \frac{cos^2(x)}{\sqrt{max(1, 2x-1)}}}$')
pylab.axis([0,35*pylab.pi,0,1])
pylab.grid()
pylab.show()