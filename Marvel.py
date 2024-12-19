#!/usr/bin/env python
# coding: utf-8

# Public Key : 53e7d05a21e6ce2a12e91b8c6b1ad51b
# 
# Private key : ad23db529ef5175a84696cdeefbcad9bfcffacd3
# 
# My ID : p8vbVH1371073140
# 
# Domain : developer.marvel.com

# In[1]:


pip install marvel


# In[1]:


from marvel import Marvel


# In[2]:


marvel = Marvel(PUBLIC_KEY = "###", PRIVATE_KEY = "###" )


# Creating and extraing data of all the Characters available.

# In[3]:


characters = marvel.characters


# In[61]:


ch = characters.all()


# In[11]:


a = characters.get('1017100')
a


# In[18]:


a['data']['results'][0]['name']


# In[60]:


char_details = []

for i in ch:
    char_id = i['id']
    char_name = i['name']
    char_desc = i['description']
    num_series = i['series']['available']
    num_comics = i['comics']['available']
    num_stories  = i['stories']['available']
    char_dect = {"char_id":i['id'], "char_name":i['name'], "char_desc":i['description'], "num_series":i['series']['available'], "num_comics":i['comics']['available'], "num_stories":i['stories']['available']}
    char_details.append(char_dect)


# In[61]:


char_details


# In[62]:


import pandas as pd
marvel_char = pd.DataFrame(char_details)


# In[56]:


marvel_char


# In[71]:


m = characters.all()
m


# In[11]:


m = "https://gateway.marvel.com:443/v1/public/characters?limit=99&offset=0&ts=1&apikey=53e7d05a21e6ce2a12e91b8c6b1ad51b&hash=89cb8451a4580652a231af3de284a6fa"


# In[12]:


import requests
import json


# In[13]:


re = requests.get(m)
l1 = re.json()
l1 = l1['data']['results']


# In[14]:


details = []

for i in l1:
    char_id = i['id']
    char_name = i['name']
    char_desc = i['description']
    num_series = i['series']['available']
    num_comics = i['comics']['available']
    num_stories  = i['stories']['available']
    char_dect = {"char_id":i['id'], "char_name":i['name'], "char_desc":i['description'], "num_series":i['series']['available'], "num_comics":i['comics']['available'], "num_stories":i['stories']['available']}
    char_details.append(char_dect)


# In[62]:


import requests
import json


# In[ ]:


set1 = set()

for i in range(20):
    m = "https://gateway.marvel.com:443/v1/public/characters?limit=99&offset=99&ts=1&apikey=53e7d05a21e6ce2a12e91b8c6b1ad51b&hash=89cb8451a4580652a231af3de284a6fa"
    mv_char = requests.get(m)
    l2 = mv_char.json()
    l2 = l2['data']['results']
    
    for i in l2:
        if i['name'] not in set1:
            set1.add(i['name'])
            char_id = i['id']
            char_name = i['name']
            char_desc = i['description']
            num_series = i['series']['available']
            num_comics = i['comics']['available']
            num_stories  = i['stories']['available']
            char_dect = {"char_id":i['id'], "char_name":i['name']}
            details.append(char_dect)


# In[9]:


import pandas as pd
data = pd.DataFrame(details)


# In[10]:


data.to_csv(r'D:\Data Engineering\Projects\marvel2.csv')


# In[ ]:




