import numpy

# Chromosomes --> (+): [0,1,0,0,0,0,1,1,1,1]

def utility(chrm):
    sum = 0
    for i in range(10):
        if chrm[i]==1:
            sum = sum+i+1
    return abs(36-sum)

def crossOver(chrm1, chrm2):
    chrm3 = list()
    for i in range(10):
        if i%2==0:
            chrm3.append(chrm1[i])
        else:
            chrm3.append(chrm2[i])
    return chrm3

def mutation(chrm):
    count = 0
    for i in chrm:
        if i==1:
            count+=1
    if count>5:
        toChange = count-5
        low = 0
        high = 9
        changed = 0
        for i in range(toChange):
            if changed==toChange:
                break
            if chrm[low]==1:
                chrm[low] = 0
                changed+=1
            low+=1
            if changed==toChange:
                break
            if chrm[high]==1:
                chrm[high] = 0
                changed+=1
            high-=1
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
                    newPopulation.append( mutation(crossOver(population[i], population[r])) )

        chrmFitnesses = list()
        for chrm in newPopulation:
            chrmFitnesses.append( utility(chrm) )

        minfitt = numpy.argpartition(chrmFitnesses, 5)
        newGeneration = list()
        for i in minfitt:
            newGeneration.append(newPopulation[i])
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
