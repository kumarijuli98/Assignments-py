#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python Program to Add Two Matrices?


# In[2]:


# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


# In[3]:


### 2. Write a Python Program to Multiply Two Matrices?


# In[4]:


# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


# In[ ]:


### 3. Write a Python Program to Transpose a Matrix?


# In[5]:


X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# In[6]:


### 4. Write a Python Program to Sort Words in Alphabetic Order?


# In[8]:


my_str = "Hello my Name is Juli"

# To take input from the user
# my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


# In[ ]:


### 5. Write a Python Program to Remove Punctuation From a String?


# In[ ]:


import string
 
test_str = 'coding, is best: for ! Python ;'
 
test_str = test_str.translate
    (str.maketrans('', '', string.punctuation))
print(test_str)

