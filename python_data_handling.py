#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 1
#Variables and Data Types

#Create three variables: one for storing your age (integer), one for your name (string), and one to check if you are a student (Boolean). Print the variables


# In[7]:


#integer
age=30 
#name
name="Zain"
#Student
std = True

print("Your Name is : " , name , "\nYour age is :" , age , "\nYou are a current student :" , std)


# In[ ]:


#b) Perform the following operations and print the results:


# In[8]:


# Add 25 to your age variable
age = int(input("Enter your age :"))
x = age + 25
print(x)


# In[14]:


# Concatenate your name with the string "Smith."
name = str(input("Enter your name :"))
print(name, "Smith")


# In[181]:


#Negate the Boolean variable (if True, make it False, and vice versa).
z = 'True'
print("Original Value :", z)
print("Negate Value :", z not in 'True') 
print("Negate Value :" ,z not in 'False') 


# In[191]:


# Task 2: Expressions and Operators


# In[192]:


# a) Find the area
width = 5.5
height = 3.25
area = width * height
print("Area is :", area)


# In[208]:


# b) Find the temperature in fahrenheit
celsius = 10
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit Values is :" , fahrenheit)


# In[216]:


# c) Find the area of circle
radius = 5
area_of_circle = 3.14 * radius**2
print("Area of circle is :",area_of_circle)


# In[ ]:


# Task 3: Introduction to Data Structures


# In[217]:


# a) Create a list called "fruits" containing the following fruits: "apple," "banana," "orange," "grape," and "kiwi." Print the list.
fruit_list = ["apple", "banana", "orange", "grapes", "kiwi"]
print(fruit_list)


# In[219]:


# b) Create a tuple named "months" with the names of the first three months of the year. Print the tuple
months = ("January", "February", "March")
print(months)


# In[ ]:


# Task 4: List Manipulation


# In[238]:


# a) Calculate the sum and average of these numbers
numbers = [12, 34, 45, 67, 89, 100, 23, 56]

num_sum = sum(numbers) # Sum Calculation
num_avg = num_sum/len(numbers) # Avg Calculation

print("Sum is :",num_sum)

print("Average is ",num_avg)


# In[245]:


# b) Remove the first and last elements from the "fruits" list 
f1 = fruit_list[1:4]
print("First and last element Removed\n",f1)


# In[ ]:


# Task 5: Dictionary Operations


# In[267]:


# a) Create a dictionary named "capitals" with three key-value pairs
capital = {"USA":"Washington D.C.", 
           "France":"Paris", 
           "Japan":"Tokyo"}
print(capital)


# In[270]:


# b) Add a new country and its capital to the "capitals" dictionary. 
capital["Germany"] = "Berlin"


# In[279]:


# c) Check if "France" exists in the "capitals" dictionary. 
if "France" in capital:
    print("France is in the dictionary")
else:
    print("France is not in the dictionary.")    


# In[ ]:


# Task 6: Comparison Operators, Logical Operators and If/Else:


# In[292]:


#a) Find the number is even or odd
user_input = int(input("Enter a Number :"))
if user_input % 2 == 0 :
    print("Number is even")
else:
    print("Number is odd")


# In[318]:


# b) Calculate age with GPA for Admission
age = 18
gpa = 3.25
if age >= 18 and gpa >= 3.0:
    print("Eligible for admission")
else:
    print("Not eligible for admission")    


# In[ ]:


#Task 7: Advanced Data Types


# In[322]:


#a) Create a set named "fruits_set" containing the following fruits: "apple," "banana," "orange," "grape," and "kiwi." 
fruit_set = {"apple", "banana", "orange", "grape", "kiwi"}
print(fruit_set)


# In[327]:


# b) Write Python code to perform the following operations and print the results:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# union 
print("Union :", set1 | set2) 
  
# intersection 
print("Intersection :", set1 & set2) 
  
# difference 
print("Difference :", set1 - set2) 
  
# subset difference 
set3 = set1.issubset(set2)
print("Symmetric difference :", set3) 


# In[ ]:


# Task 8: Strings Manipulation


# In[354]:


# a) Create a string variable containing the following sentence:
str1 = "Python programming is fun and powerful!"
print(str1)


# In[355]:


# - Find the length of the string.
print(len(str1))


# In[356]:


# - Convert the string to uppercase.
str2 = string.upper()
print(str2)


# In[357]:


# - Replace "fun" with "exciting
str3 = str2.replace("FUN","EXCITING")
print(str3)


# In[370]:


# - Check if the string contains the word "Python."
str4 = str1 in 'Python programming is fun and powerful!'
print("It's" , str4 , "Python word is available")


# In[376]:


# - Split the string into a list of words.
#str5 = str4.split()
str5 = str3.split()
print(str5)


# In[ ]:




