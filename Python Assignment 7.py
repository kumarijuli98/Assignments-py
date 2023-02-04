#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python Program to find sum of array?


# In[2]:


import array as ar

def SumofArray(arr):
    sum=0
    n = len(arr)
    for i in range(n):
        sum = sum + arr[i]
    return sum
  
#input values to list 
a = ar.array('i',[10, 21, 12, 13])
  
# display sum 
print ('Sum of the array is ', SumofArray(a) ) 


# In[ ]:


### 2. Write a Python Program to find largest element in an array?


# In[4]:


arr = [25, 11, 7, 75, 56];     
     
   
max = arr[0];    
     
  
for i in range(0, len(arr)):    
      
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: " + str(max)); 


# In[ ]:


### 3. Write a Python Program for array rotation?


# In[5]:


def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))


# In[6]:


### 4. Write a Python Program to Split the array and add the first part to the end?


# In[7]:


def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
            
        arr[n-1] = x
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[8]:


### 5. Write a Python Program to check if given array is Monotonic?


# In[9]:


def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c=[4,3,2]
print(ismonotone(c))
d=[1]
print(ismonotone(d))


# In[ ]:




