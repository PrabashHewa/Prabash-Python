#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# In[11]:


kpi_data = pd.read_csv('Performance 2.csv')


# In[12]:


kpi_data = kpi_data.drop(['Local time', 'Site ID', 'Cell name'] , axis=1)


# In[13]:


kpi_data = kpi_data.dropna()


# In[14]:


kpi_data_norm = (kpi_data - kpi_data.mean()) / kpi_data.std()


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(kpi_data_norm.drop('Quality Score, axis=1), kpi_data_norm['Quality Score'], test_size=0.2, random_state=0)


# In[16]:


# Perform Recursive Feature Elimination to select the most important features
estimator = LinearRegression()
selector = RFE(estimator, n_features_to_select=5, step=5)
selector.fit(X_train, y_train)


# In[17]:


# Print the selected features
selected_features = X_train.columns[selector.support_]
print('Selected Features:', selected_features)


# In[18]:


# Train the model using the selected features
model = LinearRegression()
model.fit(X_train[selected_features], y_train)


# In[19]:


# Evaluate the performance of the model
y_pred = model.predict(X_test[selected_features])
print('R-squared:', r2_score(y_test, y_pred))
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))

