#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python program to find sum of elements in list?


# In[8]:


def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum = sum+list[i]
    return sum

#initialise list
list = [10, 9, 7, 5]
print(list)
print("sum of list: ",sumlist(list))


# In[9]:


### 2. Write a Python program to  Multiply all numbers in the list?


# In[10]:


def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# In[ ]:


### 3. Write a Python program to find smallest number in a list?


# In[11]:


a = [18, 52, 23, 41, 32]

# find smallest number using min() function
smallest = min(a)

# print the smallest number
print(f'Smallest number in the list is : {smallest}.')


# In[12]:


### 4. Write a Python program to find largest number in a list?


# In[13]:


a = [18, 52, 23, 41, 32]

# find largest number using min() function
largest = max(a)

# print the smallest number
print(f'largest number in the list is : {largest}.')


# In[14]:


### 5. Write a Python program to find second largest number in a list?


# In[17]:


a = [18, 52, 23, 41, 32]

# sorting the list 

a.sort()  
#displaying the second last element of the list 

print("The second largest element of the list is:", a[-2])


# In[24]:


### 6. Write a Python program to find N largest elements from a list?


# In[35]:


def N_Largest(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
         
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j];
                 
        list1.remove(max1);
        final_list.append(max1)
         
        print(final_list)
        
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

N_Largest(list1, N)


# In[36]:


### 7. Write a Python program to print even numbers in a list?


# In[37]:


list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")


# In[20]:


### 8. Write a Python program to print odd numbers in a List?


# In[38]:


list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 != 0:
        print(num, end=" ")


# In[21]:


### 9. Write a Python program to Remove empty List from List?


# In[39]:


test_list = [5, 6, [], 3, [], [], 9]
 
print("The original list is : " + str(test_list))
 
# Remove empty List from List

res = [ele for ele in test_list if ele != []]
 
print("List after empty list removal : " + str(res))


# In[22]:


### 10. Write a Python program to Cloning or Copying a list?


# In[41]:


def Cloning(li1):
    li_copy = li1[:]
    return li_copy
 
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# In[23]:


### 11. Write a Python program to Count occurrences of an element in a list?


# In[42]:


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x)))


# In[ ]:




