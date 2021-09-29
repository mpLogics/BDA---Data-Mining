#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def calGraph(N,A):
    G = np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            if A[i]>A[j]:
                G[i][j] = 1
                G[j][i] = 1
    #print("Adjacency matrix for the graph obtained from the given array is : \n",G)
    #print()
    return G


# In[3]:


def findMin(degree,removed):
    a = max(degree)
    arg=-1
    for i in range(degree.size):
        if removed[i] == 0 and a>degree[i]:
            a = degree[i]
            arg = i
    return arg


# In[4]:


def displayAns(degree,A):
    Final = []
    Index = []
    for i in range(degree.size):
        if degree[i]!=0:
            Final.append(A[i])
            Index.append(i)
    print("\nMax possible set size: ",len(Final))
    print("Possible set of vertices are:",(Final),"at indices:",Index,"respectively")

# In[5]:


def findSubset(N,G):
    n=N
    removed = np.zeros(N)
    k=0
    while(n>=0):
        degree = np.sum(G,axis=1)
        s_vertex = findMin(degree,removed)
        removed[s_vertex]=1
        if degree[s_vertex] == n-1:
            break
        else:
            n-=1
            G[s_vertex,:] = 0
            G[:,s_vertex] = 0
        degree = np.sum(G,axis=1)
        k+=1
        #print("\nAfter ",k,"iteration(s): ")
        #print(G)
        #print()
    return degree


# In[7]:


if __name__ == "__main__":    
    # Test case
    #N = 6
    #A = [90 ,70 ,60, 50, 65, 55]
    
    N = (int)(input("Enter value for N (Number of elements in the array): "))
    A_list = input("Enter the elements: ")
    integer_map = map(int,A_list.split())
    A = list(integer_map)
    displayAns(findSubset(N,calGraph(N,A)),A)
    input("Press any key to exit")

# In[ ]:




