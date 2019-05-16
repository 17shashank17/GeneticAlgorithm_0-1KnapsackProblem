import time
import random

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# Driver program to test above function 
wt = [2,3,1,6,4,8,3,5]
val = [4,7,5,11,7,9,3,13]
W = 15
'''file=open("input.txt","r")
input_test=[]
for line in file:
  line=line.strip()
  input_test.append(line)
wt=[]
val=[]
for i in range(len(input_test)):
  input_test[i]=input_test[i].split()
  wt.append(int(input_test[i][1]))
  val.append(int(input_test[i][0]))
W=9384'''
n = len(val) 
sec1=time.time()
print(knapSack(W, wt, val, n)) 
sec2=time.time()
print(sec2-sec1)