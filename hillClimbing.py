import random
import math
import numpy
import matplotlib.pyplot as plt

def f(x):
    return math.sin(10*math.pi*x)/(2*x) + (x-1)**4

x = random.uniform(0.5, 2.5)
step = 0.015625
a = numpy.gradient(f(x), x)
a1 = numpy.gradient(f(x), x-step)
a2 = numpy.gradient(f(x), x+step)

print(a)
print(a1)
print(a2)
print("here1")
while ( a1>a or a2>a ):
    print("here2")
    if a1<a:
        x = x-step
        a = numpy.gradient(f(x), x)
        a1 = numpy.gradient(f(x), x-step)
        a2 = numpy.gradient(f(x), x+step)
    else:
        x = x+step
        a = numpy.gradient(f(x), x)
        a1 = numpy.gradient(f(x), x-step)
        a2 = numpy.gradient(f(x), x+step)

x_value = x
y_value = f(x_value)
fx = numpy.vectorize(f)
x = numpy.arange(0.5, 2.5, 0.0078125)
plt.plot(x, fx(x))
plt.scatter(x_value, y_value, color= "red", marker= "o", s=20)   
plt.xlabel('x') 
plt.ylabel('fx')
plt.show() 
# print(x)
