import random
import math
import numpy
import matplotlib.pyplot as plt

def f(x):
    return math.sin(10*math.pi*x)/(2*x) + (x-1)**4

def temperature(fraction):
    return max( 0.01, min(1, 1-fraction) )

def probability(cost, new_cost, temp):
    if new_cost<cost:
        return 1
    else:
        return numpy.exp(-(new_cost-cost)/temp)

x = random.uniform(0.5, 2.5)
for cycle in range(1000):
    fraction = cycle/1000
    t = temperature(fraction)
    while True:
        x_next = random.uniform(0.5, 2.5)
        if x_next != x:
            break
    if probability(f(x), f(x_next), t)>random.uniform(0, 1):
        x = x_next

x_value = x
y_value = f(x_value)
print("x=" + str(x_value) + "  y=" + str(y_value))
fx = numpy.vectorize(f)
x = numpy.arange(0.5, 2.5, 0.0078125)
plt.plot(x, fx(x))
plt.scatter(x_value, y_value, color= "red", marker= "o", s=10)   
plt.xlabel('x') 
plt.ylabel('fx')
plt.show() 
