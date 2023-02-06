#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python program to find words which are greater than given length k?


# In[2]:


def word_k(k, s):    
    # split the string where space comes
    word = s.split(" ")
    # iterate the loop for every word
    for x in word:
        # if length of current word
        if len(x)>k:
          # greater than k then
          print(x)
k = 3
s ="Python is good"
word_k(k, s)


# In[3]:


### 2. Write a Python program for removing i-th character from a string?


# In[5]:


def remove_char(s, i):
    a = s[ : i]
    b = s[i + 1: ]

    return a+b

string = "Python is good"
# Remove ith index element
i = 5
print(remove_char(string,i-1))


# In[6]:


### 3. Write a Python program to split and join a string?


# In[7]:


def split_string(string):
    # Splitting based on space delimiter
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    # Joining based on '-' delimiter
    string = '-'.join(list_string)
    return string

string = 'Welcome to study tonight'
# Splitting a string
list_string = split_string(string)
print("After Splitting: ",list_string)

# Join list of strings into one
res_string = join_string(list_string)
print("After joining: ",res_string)


# In[8]:


### 4. Write a Python to check if a given string is binary string or not?


# In[12]:


def check(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")
s1= "00110101"
# function calling
check(s1)
s2 = "1010100200111"
check(s2)


# In[13]:


### 5. Write a Python program to find uncommon words from two Strings?


# In[14]:


def uncommon_words(s1, s2):
    count = {}
    for word in s1.split():
        count[word] = count.get(word, 0) + 1
    # words of string s2
    for word in s2.split():
        count[word] = count.get(word, 0) + 1
    # return required list of words
    return [word for word in count if count[word] == 1]

s1="Studytonight"
s2="Welcome to Studytonight"
  
# Print required answer
print(uncommon_words(s1, s2))


# In[15]:


### 6. Write a Python to find all duplicate characters in string?


# In[ ]:


def find_duplicate():
    x = input("Enter a word = ")
    dup_letters = []
    dup_num = []

    for char in x:
        if char not in dup_letters and x.count(char) > 1:
            dup_letters.append(char)
            dup_num.append(x.count(char))

    return zip(dup_letters, dup_num)

dup = find_duplicate()

for i in dup


# In[ ]:


### 7. Write a Python Program to check if a string contains any special character?


# In[ ]:


import re

def find(string):
    special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    
    if special_char.search(string) == None:
        return "string is accepted"
    else:
        return "string not accpeted"
s="Hello15"
print(s)
print(find(s))


# In[ ]:




