
# coding: utf-8

# In[59]:


import csv
import httplib2
from apiclient.discovery import build
import urllib
import json

# This API key is provided by google as described in the tutorial
API_KEY = 'AIzaSyBWD2VkD7Rl5eJkzEP9snndRfOTZTaqNrg'

# This is the table id for the fusion table
TABLE_ID = '1jDNgu9rG3oHDZxOaroIwzK-XFA30Stqt0g9CZQc_'

try:
    fp = open("gdp.json")
    response = json.load(fp)
except IOError:
    service = build('fusiontables', 'v1', developerKey=API_KEY)
    query = "SELECT * FROM " + TABLE_ID
    response = service.query().sql(sql=query).execute()
    fp = open("gdp.json", "w+")
    json.dump(response, fp)


# In[60]:


print len(response['rows'])


# In[61]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[62]:


data_df = pd.DataFrame(response[u'rows'], columns = response[u'columns'])


# In[63]:


data_df.head()


# In[65]:


x = data_df[u'year']
y = data_df[u'GDP Amount']
plt.scatter(x, y)

x = data_df[u'year']
y = data_df[u'GDP Growth']
plt.scatter(x, y)