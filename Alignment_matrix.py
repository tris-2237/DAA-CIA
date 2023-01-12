import numpy as np
#Human genes match score=5 and mismatch=-4
num=0
e=0
f=0
a=['A','G','C','A','T','C','G','A','T','G','C','A']
b=['A','C','T','A','G','C','T','A','C','T','G','A']
arr = np.zeros([13, 13], dtype = int) 

def fill(arr,j,num):
#     print(j)
    for i in range(len(a)):
#         print(i)
        if(a[i]==b[j]):
            max=arr[i][j]
            if(max+5>num): 
                num=5+max
                c=i+1
                d=j+1
            arr[i+1][j+1]=max+5
        elif(a[i]!=b[j]):
            max=arr[i][j];
            if(arr[i][j+1]>max): 
                max=arr[i][j+1]
            if(arr[i+1][j]>max): 
                max=arr[i+1][j]
            if(max-1>num):
                num=max-4
                c=i+1
                d=j+1
            arr[i+1][j+1]=max-4
    if(j==len(a)-1):
        return c,d
    else:
        j+=1
        return fill(arr,j,num)
    
j=0
e,f=fill(arr,j,num)
print(arr)
# Prim's Algorithm in Python


INF = 9999999

V = 12

selected = [0, 0, 0, 0, 0,0, 0, 0, 0, 0,0,0]
# set number of edge to 0
no_edge = 0

selected[0] = True
print("prims traceback sequence")
#print("Edge : Weight\n")
while (no_edge < V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and arr[i][j]):  
                    if minimum > arr[i][j]:
                        minimum = arr[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(arr[x][y]))
    selected[y] = True
    no_edge += 1
