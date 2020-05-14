# Chromosomes --> (+): [0,1,0,0,0,0,1,1,1,1]

def utility(gen):
    sum = 0
    for i in range(9):
        if gen[i]==1:
            sum = sum+i+1
    return abs(36-sum)

