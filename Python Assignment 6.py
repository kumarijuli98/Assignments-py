#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?


# In[2]:


# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[3]:


### 2. Write a Python Program to Find Factorial of Number Using Recursion?


# In[4]:


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[5]:


### 3. Write a Python Program to calculate your Body Mass Index?


# In[6]:


height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


# In[7]:


### 4. Write a Python Program to calculate the natural logarithm of any number?


# In[8]:


import math

number = int(input("Enter the number: "))

ans = math.log(number)

print("The value is:",ans)


# In[9]:


### 5. Write a Python Program for cube sum of first n natural numbers?


# In[10]:


def CubeSum(n):
    s=0
    for i in range(n+1):
        s+=i**3
    return s
n=int(input("enter n: "))
print("sum of cubes of first {} natural numbers: ".format(n),CubeSum(n))


# In[ ]:




