import random
import numpy
import matplotlib.pyplot as plt

# Chromosomes --> (+): [0,1,0,0,0,0,1,1,1,1]

def utility(chrm):
    sum = 0
    for i in range(10):
        if chrm[i]==1:
            sum = sum+i+1
    sum_error = abs(36-sum)/36*100

    product = 1
    for i in range(10):
        if chrm[i]==0:
            product = product*(i+1)
    product_error = abs(360-product)/360*100

    return (sum_error+product_error)/2

def crossOver(chrm1, chrm2):
    chrm3 = list()
    chrm4 = list()

    i = random.randint(1,9)

    for r in range(i):
        chrm3.append(chrm1[r])
        chrm4.append(chrm2[r])
    
    temp = i
    for r in range(10-i):
        chrm3.append(chrm2[temp])
        chrm4.append(chrm1[temp])
        temp+=1
    
    return (chrm3, chrm4)

def mutation(chrm):
    for i in range(4):
        index = random.randint(0,9)
        if chrm[index]==1:
            chrm[index] = 0
        else:
            chrm[index] = 1
    return chrm

def summation(chrm):
    sum = 0
    for i in range(10):
        if chrm[i]==1:
            sum = sum+i+1
    return sum

def production(chrm):
    product = 1
    for i in range(10):
        if chrm[i]==0:
            product = product*(i+1)   
    return product

def solution(population):
    for chrm in population:
        if summation(chrm)==36:
            if production(chrm)==360:
                return chrm
            return []
    return []

def env(population):
    fitness_avgs = list()
    cycle = 1
    while solution(population)==[]:

        #adadye fitness 4ta chrm ha ro peyda mikone
        fitness_array = list()
        for chrm in population:
            fitness_array.append(utility(chrm))

        #avg fitness e har nasl inja zakhre mikonm
        fitness_sum = 0
        for fitness in fitness_array:
            fitness_sum+=fitness
        fitness_avgs.append((cycle, fitness_sum/4))
        
        #bad tarin ro peyda mikone
        index = 0
        index_fitness = 0
        max_fitness = fitness_array[0]
        for i in fitness_array:
            if i>max_fitness:
                max_fitness = i
                index_fitness = index
            index+=1

        #population jadid bad az selection
        new_population_after_selection = list()
        for i in range(4):
            if i!=index_fitness:
                new_population_after_selection.append(population[i])
        random_chrm_index = random.randint(0,3)
        while random_chrm_index==index_fitness:
            random_chrm_index = random.randint(0,3)
        new_population_after_selection.append(population[random_chrm_index])

        #cross over va mutate rooye in 4ta
        if new_population_after_selection[2]!=new_population_after_selection[3]:
            gen1, gen2 = crossOver(new_population_after_selection[0], new_population_after_selection[1])
            population[0] = mutation(gen1)
            population[1] = mutation(gen2)
            gen1, gen2 = crossOver(new_population_after_selection[2], new_population_after_selection[3])
            population[2] = mutation(gen1)
            population[3] = mutation(gen2)
        else:
            gen1, gen2 = crossOver(new_population_after_selection[0], new_population_after_selection[2])
            population[0] = mutation(gen1)
            population[1] = mutation(gen2)
            gen1, gen2 = crossOver(new_population_after_selection[1], new_population_after_selection[3])
            population[2] = mutation(gen1)
            population[3] = mutation(gen2)

        cycle+=1

    return (solution(population), fitness_avgs)

def plot(fitness_list):
    x_values = list()
    y_values = list()
    for fitness in fitness_list:
        x, avg = fitness
        x_values.append(x)
        y_values.append(avg)
    
    plt.plot(x_values, y_values, color='green', linestyle='dashed', linewidth = 3, 
            marker='o', markerfacecolor='blue', markersize=10) 

    plt.ylim(1,100) 
    plt.xlim(1,10) 
    plt.xlabel('generation') 
    plt.ylabel('fitness average') 
    plt.title('genetic algorithm speed change') 
    plt.show() 

firstGeneration = [
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,1,0,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,0,1]
]

ansSum, fitness_list = env(firstGeneration)
print(ansSum)
plot(fitness_list)
