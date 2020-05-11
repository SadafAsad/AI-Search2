import random
import math
import numpy

x = random.uniform(0.5, 2.5)
fx = math.sin(10*math.pi*x)/(2*x) + (x-1)**4
step = 0.03125
a = numpy.gradient(fx, x)
a1 = numpy.gradient(fx, x-step)
a2 = numpy.gradient(fx, x+step)

while ( a1<a or a2<a ):
    if a1<a:
        x = x-step
        a = numpy.gradient(fx, x)
        a1 = numpy.gradient(fx, x-step)
        a2 = numpy.gradient(fx, x+step)
    else:
        x = x+step
        a = numpy.gradient(fx, x)
        a1 = numpy.gradient(fx, x-step)
        a2 = numpy.gradient(fx, x+step)

print(x)
