#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt
from IPython.display import SVG, display
#import plotly.graph_objects as go


# In[10]:


kpi_data = pd.read_csv('Quality Score1.csv')


# In[11]:


#X = kpi_data[['Resid BLER DL PDSCH','Avg DL MCS','Avg DL Rank']]
#y = kpi_data['Quality Score']
X=kpi_data[['Avg DL Rank','Resid BLER DL PDSCH', 'Avg DL MCS']]
y=kpi_data['Quality Score']


# In[12]:


mi_scores = mutual_info_regression(X, y)


# In[13]:


feature_scores = pd.Series(mi_scores, index=X.columns)
feature_scores.sort_values(ascending=False, inplace=True)


# In[14]:


print(feature_scores)


# In[27]:


plt.bar(feature_scores.index, feature_scores.values)
#plt.xticks(rotation=90)
plt.ylabel('MI Score')

# Save the plot as an SVG file
svg_MIscore = 'MIscore.svg'
plt.savefig(svg_MIscore, format='svg')

# Display the plot as SVG
display(SVG(svg_MIscore))


# In[ ]:




