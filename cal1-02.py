import pylab


def h(t):
    return 1.2732 * pylab.sin(2 * t) + 0.4244 * pylab.sin(6 * t) + 0.25465 * pylab.sin(10 * t) + 0.18189 * pylab.sin(14 * t) + 0.14147 * pylab.sin(18 * t)


def dh(t, c):
    return (h(t + c) - h(t)) / c


a = -pylab.pi
b = pylab.pi
n = 10001

dt = (b - a) / (n - 1)

ts = pylab.linspace(a, b, n)

hs = h(ts)
dhs = dh(ts, 0.0000001)

pylab.plot(ts, hs, label='h(t)', color='blue')
pylab.plot(ts, dhs, label="h'(t)", color='green')

pylab.title('sawtooth function approximation and derivative')
pylab.xlabel('t')
pylab.ylabel('S')
pylab.legend(loc=4)
pylab.grid()
pylab.show()
