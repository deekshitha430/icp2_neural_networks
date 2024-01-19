#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name
fName= input("Enter your First Name : ")
lName= input("Enter your Last Name : ")
print(Full_name(fName, lName))


# In[2]:


def string_alternative(string):
    return string[::2]
def main():
    print(string_alternative("Good Evening"))
if __name__ == "__main__":
    main()


# In[3]:


with open('input.txt','r') as ip_file:
    lines=ip_file.read()
    word=lines.split()
    data=[]
    with open('output.txt','w') as op_file:
        for i in word:
            if i not in data:
                data.append(i)
                op_file.write(i+':'+str(word.count(i))+'\n')      
op_file=open('output.txt','r')
print(op_file.read())


# In[4]:


L1 = list(map(float, input().split()))
L2= []

for i in L1:
    L2.append(i*2.54)
print(L2) 

L3=[i*2.54 for i in L1]
print(L3)


# In[ ]:




