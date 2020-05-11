import random
import math
import numpy

fx = math.sin(10*math.pi*x)/(2*x) + (x-1)**4
x1 = random.uniform(0.5, 2.5)
step = 0.03125
a = numpy.gradient(fx, x1)
a1 = numpy.gradient(fx, x1-step)
a2 = numpy.gradient(fx, x1+step)

while ( a1<a or a2<a ):
    if a1<a:
        x1 = x1-step
        a = numpy.gradient(fx, x1)
        a1 = numpy.gradient(fx, x1-step)
        a2 = numpy.gradient(fx, x1+step)
    else:
        x1 = x1+step
        a = numpy.gradient(fx, x1)
        a1 = numpy.gradient(fx, x1-step)
        a2 = numpy.gradient(fx, x1+step)

print(x1)
