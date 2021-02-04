#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Examine how changes in GDP impact the unemployment rate
# 

# In[2]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In[3]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# In[4]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# In[5]:


gdp_df= pd.read_csv(links['GDP'])
gdp_df.head()


# In[6]:


gdp_df1= pd.read_csv(links['unemployment'])
gdp_df1.head()


# In[7]:


greater_than=gdp_df1['unemployment'] > 8.5
greater_than.head()


# In[8]:


x = gdp_df[['date']]
gdp_change =gdp_df[['change-current']]
unemployment = gdp_df1[['unemployment']]
title = ("GDP DAshboard")
file_name = "index.html"


# In[9]:


make_dashboard(x, gdp_change, unemployment, title, file_name)


# In[ ]:




