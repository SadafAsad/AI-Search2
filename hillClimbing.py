import random
import math
import numpy
import matplotlib.pyplot as plt

def f(x):
    return math.sin(10*math.pi*x)/(2*x) + (x-1)**4

def plot(x):
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

def hillClimbing():
    x = random.uniform(0.5, 2.5) 
    step = 0.0078125
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
    return x

x = hillClimbing()
plot(x)