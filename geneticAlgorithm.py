import numpy
import random

# Chromosomes --> (+): [0,1,0,0,0,0,1,1,1,1]

def utility(chrm):
    sum = 0
    for i in range(10):
        if chrm[i]==1:
            sum = sum+i+1
    return abs(36-sum)

def crossOver(chrm1, chrm2):
    chrm3 = list()
    chrm4 = list()

    i = random.randint(1,9)

    for r in range(i):
        chrm3.append(chrm1[r])
        chrm4.append(chrm2[r])
    for r in range(10-i):
        chrm3.append(chrm2[i])
        chrm4.append(chrm1[i])
        i+=1
    
    return (chrm3, chrm4)

# def popMute(population):
#     for i in range(25):
#         for r in range(25):
#             if population[i+5]==population[r+5]:

def mutation(chrm):
    count = 0
    for i in chrm:
        if i==1:
            count+=1 

    if count>5:
        toChange = count-5
        while toChange!=0:
            index = random.randint(0,9)
            if chrm[index]==1:
                chrm[index] = 0
                toChange-=1
    elif count<5:
        toChange = 5-count
        while toChange!=0:
            index = random.randint(0,9)
            if chrm[index]==0:
                chrm[index] = 1
                toChange-=1
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
    while solution(population)==[]:
        newPopulation = list()
        for chrm in population:
            newPopulation.append(chrm)

        for i in range(5):
            for r in range(5):
                if i!=r:
                    gen1, gen2 = crossOver(population[i], population[r])
                    newPopulation.append( mutation(gen1) )
                    newPopulation.append( mutation(gen2) )

        chrmFitnesses = list()
        for chrm in newPopulation:
            chrmFitnesses.append( utility(chrm) )

        minfitt = numpy.argpartition(chrmFitnesses, 5)
        newGeneration = list()
        for i in range(5):
            newGeneration.append(newPopulation[minfitt[i]])
        population = newGeneration
    return solution(population)

firstGeneration = [
    [1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1],
    [1,1,0,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,0,1],
    [1,1,1,0,0,1,0,1,0,0]
]

ansSum = env(firstGeneration)
