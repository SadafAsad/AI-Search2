import random
import math
import numpy
import matplotlib.pyplot as plt

def f(x):
    return math.sin(10*math.pi*x)/(2*x) + (x-1)**4

x_array = list()
for i in range(50):
    x_array.append( random.uniform(0.5, 2.5) )

step = 0.0078125
min_array = list()

for x in x_array:
    a = numpy.gradient([f(x-step), f(x), f(x+step)], [x-step, x, x+step])
    while not ( a[0]<0 and a[2]>0 ):
        if ( a[0]>0 and a[2]>0 ):
            x = x-step
            a = numpy.gradient([f(x-step), f(x), f(x+step)], [x-step, x, x+step])
            while not ( a[0]<0 and a[2]>0 ):
                x = x-step
                a = numpy.gradient([f(x-step), f(x), f(x+step)], [x-step, x, x+step])
            break
        x = x+step
        a = numpy.gradient([f(x-step), f(x), f(x+step)], [x-step, x, x+step])
    min_array.append( (x, f(x)) )

x_value, y_value = min_array[0]
for value in min_array:
    x_min, y_min = value
    if y_min<y_value:
        x_value = x_min
        y_value = y_min

print("x=" + str(x_value) + "  y=" + str(y_value))
fx = numpy.vectorize(f)
x = numpy.arange(0.5, 2.5, 0.0078125)
plt.plot(x, fx(x))
plt.scatter(x_value, y_value, color= "red", marker= "o", s=10)   
plt.xlabel('x') 
plt.ylabel('fx')
plt.show() 
