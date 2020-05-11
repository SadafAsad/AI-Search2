import random
import math
import numpy
import matplotlib.pyplot as plt

def f(x):
    return math.sin(10*math.pi*x)/(2*x) + (x-1)**4

# x = random.uniform(0.5, 2.5)
# step = 0.03125
# a = numpy.gradient(f(x), x)
# a1 = numpy.gradient(f(x), x-step)
# a2 = numpy.gradient(f(x), x+step)

# print("here1")
# while ( a1<a or a2<a ):
#     print("here2")
#     if a1<a:
#         x = x-step
#         a = numpy.gradient(f(x), x)
#         a1 = numpy.gradient(f(x), x-step)
#         a2 = numpy.gradient(f(x), x+step)
#     else:
#         x = x+step
#         a = numpy.gradient(f(x), x)
#         a1 = numpy.gradient(f(x), x-step)
#         a2 = numpy.gradient(f(x), x+step)

# x_value = x
# y_value = f(x_value)
fx = numpy.vectorize(f)
x = numpy.arange(0.5, 2.5, 1)
plt.plot(x, fx(x)) 
plt.xlabel('x') 
plt.ylabel('fx') 
plt.show() 
# print(x)
