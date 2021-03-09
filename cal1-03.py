import pylab
import numpy

pi = pylab.pi

a, b, n = 0, pi / 2, 100

xs, h = pylab.linspace(a, b, n + 1, retstep=True)
ys = numpy.power(pylab.sin(3 * xs),[2]) * pylab.cos(3 * xs)

rsum, lsum, usum, tsum = 0, 0, 0, 0

y1 = ys[0]

for y2 in ys[1:]:

    rsum += y1
    if y1 < y2:
        lsum += y1
        usum += y2
    else:
        lsum += y2
        usum += y1
    tsum += y1 + y2
    y1 = y2
rsum *= h
lsum *= h
usum *= h
tsum *= h/2
isum = -1 / 9

print('數學積分 :', round(isum, 9), end='\n\n')
print('迴圈求積:')
print('矩形積分　  :', round(rsum, 9), '誤差:', round(abs(isum - rsum), 10))
print('上矩形積分  :', round(usum, 9), '誤差:', round(abs(isum - usum), 10))
print('梯形積分法  :', round(tsum, 9), '誤差:', round(abs(isum - tsum), 10))
print()

isum1 = h * sum(ys[:-1])
isum2 = h * sum([ys[0], 2 * sum(ys[1:-1]), ys[-1]]) / 2
isum3 = h * sum([ys[0], 4 * sum(ys[1:-1:2]), 2 * sum(ys[2:-1:2]), ys[-1]]) / 3

print('公式求積:')
print('矩形積分法  :', round(isum1, 9), '誤差:', round(abs(isum - isum1), 10))
print('梯形積分法  :', round(isum2, 9), '誤差:', round(abs(isum - isum2), 10))
print('Simpson積分:', round(isum3, 9), '誤差:', round(abs(isum - isum3), 10))
