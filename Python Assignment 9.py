#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python program to check if the given number is a Disarium Number?


# In[2]:


def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num

num = 25
print("\nIs",num,"is Disarium number?",is_disarium(num))
num = 89
print("\nIs",num,"is Disarium number?",is_disarium(num))


# In[3]:


### 2. Write a Python program to print all disarium numbers between 1 to 100?


# In[4]:


#calculateLength() will count the digits present in a number  
def calculateLength(n):  
    length = 0;  
    while(n != 0):  
        length = length + 1;  
        n = n//10;  
    return length;  
   
#sumOfDigits() will calculates the sum of digits powered with their respective position  
def sumOfDigits(num):  
    rem = sum = 0;  
    len = calculateLength(num);  
      
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem**len);  
        num = num//10;  
        len = len - 1;  
    return sum;  
    
result = 0;  
   
#Displays all disarium numbers between 1 and 100  
print("Disarium numbers between 1 and 100 are");  
for i in range(1, 101):  
    result = sumOfDigits(i);  
      
    if(result == i):  
        print(i),


# In[ ]:


### 3. Write a Python program to check if the given number is Happy Number?


# In[5]:


def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))


# In[6]:


### 4. Write a Python program to print all happy numbers between 1 and 100?


# In[8]:


def check_happy_num(my_num):
    remaining = sum_val = 0
    while(my_num > 0):
        remaining = my_num%10
        sum_val = sum_val + (remaining*remaining)
        my_num = my_num//10
    return sum_val
print("The list of happy numbers between 1 and 100 are : ")
for i in range(1, 101):
    my_result = i
    while(my_result != 1 and my_result != 4):
        my_result = check_happy_num(my_result)
    if(my_result == 1):
        print(i)


# In[9]:


### 5. Write a Python program to determine whether the given number is a Harshad Number?


# In[16]:


def test(n):
    if (n>0):
        a = 0
        b = n
        while b > 0:
            a = a +  b % 10
            b = b // 10
        return not n % a
     
n = 666
print("Check number:", n)
print("Check the said number is a Harshad number or not!")
print(test(n))
n = 11
print("\nCheck number:", n)
print("Check the said number is a Harshad number or not!")
print(test(n))


# In[17]:


### 6. Write a Python program to print all pronic numbers between 1 and 100?


# In[18]:


def isPronicNumber(num):  
    flag = False;  
      
    for j in range(1, num+1):  
        #Checks for pronic number by multiplying consecutive numbers  
        if((j*(j+1)) == num):  
            flag = True;  
            break;  
    return flag;  
   
#Displays pronic numbers between 1 and 100  
print("Pronic numbers between 1 and 100: ");  
for i in range(1, 101):  
    if(isPronicNumber(i)):  
        print(i),  
        print(" "),  


# In[ ]:




