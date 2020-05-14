# Chromosomes --> (+): [0,1,0,0,0,0,1,1,1,1]

def utility(chrm):
    sum = 0
    for i in range(9):
        if chrm[i]==1:
            sum = sum+i+1
    return abs(36-sum)

def crossOver(chrm1, chrm2):
    chrm3 = list()
    chrm3.append(chrm1[0])
    chrm3.append(chrm2[1])
    chrm3.append(chrm2[2])
    chrm3.append(chrm1[3])
    chrm3.append(chrm2[4])
    chrm3.append(chrm2[5])
    chrm3.append(chrm1[6])
    chrm3.append(chrm2[7])
    chrm3.append(chrm2[8])
    chrm3.append(chrm1[9])
    return chrm3

def mutation(chrm):
    count = 0
    for i in chrm:
        if i==1:
            count+=1
    if count>5:
        toChange = 5-count
        low = 0
        high = 9
        changed = 0
        for i in range(toChange-1):
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


            
