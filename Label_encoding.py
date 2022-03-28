#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('Loan_data.csv')
df


# In[2]:


x = df.dtypes
for i in x:
    print(i)


# In[3]:


for i in x:
    if(i== 'object'):
        ohe = pd.get_dummies(df)
print(ohe)


# In[4]:


from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
l = list(ohe)


# In[5]:


lb.fit(l)


# In[6]:


lb.transform(l)


# In[7]:


from sklearn.preprocessing import OneHotEncoder


# In[8]:


enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(df)


# In[9]:


enc.transform(df).toarray()

