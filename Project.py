#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plots
import plotly.express as px
import streamlit as st


# In[2]:

st.title('World Happiness Report 2021')
happy = pd.read_csv('/Users/iiiii/Desktop/world-happiness-report-2021.csv')
happy
st.markdown('This is the dataset of world happiness report in 2021.')
st.markdown('I am going to perform a series of data analysis on this dataset, to let you see what data science can really do.')

# In[3]:
head5 = happy.head(5)
head5
st.markdown('This is the first 5 lines of the dataset. As you can see, there are many columns, just ignore the column at the end that say "Explained by:".')
st.markdown('Lets first define all of the columns.')
# In[4]:
st.markdown('There are a lot of "Explained by:" columns in the table, they are optional, so I am going to delete them.')

happiest = happy[happy['Ladder score'] == max(happy['Ladder score'])]
happiest

# In[11]:

# ### Su-Saharan Africa is in the lower area, poor

# ### GDP up, Ladder score up

# ### Social support up, Ladder score up

# ### Social support up, GDP up

# ### These factors support each other

# In[7]:


st. px.scatter_3d(happy, x='Ladder score', y='Logged GDP per capita', z='Generosity', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name')


# ### GDP up, Ladder score up

# ### Interesting! Ladder: 7~3.5 
# ### Generosity: 0.1~-0.3

# ### May think that GDP up, generosity up. BUT NO

# In[7]:


happy


# In[8]:


px.scatter_3d(happy, x='Regional indicator', y='Ladder score', z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name')


# In[10]:


richest = happy[happy['Logged GDP per capita'] == max(happy['Logged GDP per capita'])]
richest


# ### Fast way of looking at data

# In[9]:


px.scatter_3d(happy, x='Freedom to make life choices', y='Social support',z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name')


# ### The point here 

# ### ![Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png](attachment:Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png)

# ### is Afghanistan, a very poor country, with a bunch of terrorists

# In[ ]:





# In[ ]:




