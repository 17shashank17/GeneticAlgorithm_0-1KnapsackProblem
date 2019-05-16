import random
import time

def knapSack(W, wt, val, n): 
    T = [[0 for x in range(W+1)] for x in range(n+1)] 

    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                T[i][w] = 0
            elif wt[i-1] <= w: 
                T[i][w] = max(val[i-1] + T[i-1][w-wt[i-1]],  T[i-1][w]) 
            else: 
                T[i][w] = T[i-1][w] 
  
    return T[n][W]

def knapsack(weight, value, MAX, popSize, mut, maxGen, percent):
  generation = 0
  pop = generate(value, popSize)
  fitness = getFitness(pop, weight, value, MAX)
  while(not test(fitness, percent) and generation < maxGen):
    generation += 1
    pop = newPopulation(pop, fitness, mut)
    fitness = getFitness(pop, weight, value, MAX)

  arr=selectElite(pop, fitness)
  return arr

def generate(value, popSize):
  length = len(value)
  pop = [[random.randint(0,1) for i in range(length)] for j in range(popSize)]
  return pop
  
def getFitness(pop, weight, value, MAX):
  fitness = []
  for i in range(len(pop)):
    sum_weight = MAX+1
    sum_value = 0
    while (sum_weight > MAX):
      sum_weight = 0
      sum_value = 0
      ones = []
      for j in range(len(pop[i])):
        if pop[i][j] == 1:
          sum_weight += weight[j]
          sum_value += value[j]
          ones += [j]
      if sum_weight > MAX:
        pop[i][ones[random.randint(0, len(ones)-1)]] = 0
    fitness += [sum_weight]
  return fitness

def newPopulation(pop, fit, mut):
  popSize = len(pop)
  newPop = []
  newPop += [selectElite(pop, fit)]
  while(len(newPop) < popSize):
    (mate1, mate2) = select(pop, fit)
    newPop += [mutate(crossover(mate1, mate2), mut)]
  return newPop
  
def selectElite(pop, fit):

  elite = 0
  for i in range(len(fit)):
    if fit[i] > fit[elite]:
      elite = i
  return pop[elite]

def select(pop, fit):
  size = len(pop)
  totalFit = sum(fit)
  lucky = random.randint(0, totalFit)
  tempSum = 0
  mate1 = []
  fit1 = 0
  for i in range(size):
    tempSum += fit[i]
    if tempSum >= lucky:
      mate1 = pop.pop(i)
      fit1 = fit.pop(i)
      break
  tempSum = 0
  lucky = random.randint(0, sum(fit))
  for i in range(len(pop)):
    tempSum += fit[i]
    if tempSum >= lucky:
      mate2 = pop[i]
      pop += [mate1]
      fit += [fit1]
      return (mate1, mate2)

def crossover(mate1, mate2):
  lucky = random.randint(0, len(mate1)-1)
  return mate1[:lucky]+mate2[lucky:]
  
def mutate(gene, mutate):
  for i in range(len(gene)):
    lucky = random.randint(1, mutate)
    if lucky == 1:
      gene[i] = bool(gene[i])^1
  return gene
    
def test(fit, rate):
  maxCount = mode(fit)
  if float(maxCount)/float(len(fit)) >= rate:
    return True
  else:
    return False

def mode(fit):
  values = set(fit)
  maxCount = 0
  for i in values:
    if maxCount < fit.count(i):
      maxCount = fit.count(i)
  return maxCount

def profit(arr,value):
  sum=0
  for i in range(0,len(arr)):
    if arr[i]==1:
      sum+=value[i]
  return sum

weight = [2,3,1,6,4,8,3,5]
value = [4,7,5,11,7,9,3,13]
maxWeight = 15
'''file=open("input.txt","r")
input_test=[]
for line in file:
  line=line.strip()
  input_test.append(line)
weight=[]
value=[]
for i in range(len(input_test)):
  input_test[i]=input_test[i].split()
  weight.append(int(input_test[i][1]))
  value.append(int(input_test[i][0]))
maxWeight=9384'''

popSize = 200
count=1
prof=knapSack(maxWeight,weight,value,len(value))
print("Total profit as given by DP: ",prof)

arr=knapsack(weight, value, maxWeight, popSize,10,80,0.1)
while profit(arr,value) != prof:
  count+=1
  arr=knapsack(weight, value, maxWeight, popSize,10,80,0.1) 

  print("Inputs:")
  print("Maximum weight of Sack:",maxWeight)
  print("Weight Array:",weight)
  print("Profit Array:",value)
  print("FINAL SOLUTION: " + str(arr))
  print("Number of trials: ",count)
  print("TOTAL PROFIT by GENETIC ALGORITHM: ",profit(arr,value))
