#!/usr/bin/env python
# coding: utf-8

# In[70]:


# import necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.feature_selection import SelectKBest, f_regression
from pydruid.db import connect
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from IPython.display import SVG, display


# In[4]:


import datetime
#get current date and time
time_now = datetime.datetime.now()

from datetime import datetime, timedelta
import math

def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta

number_of_days = 7
delta = timedelta(days=1)
offset = timedelta(days=number_of_days)
offset_sec = timedelta(seconds=1)

time_now_day = round_dt(time_now,delta)

#convert date and time to string
time_start_str = str(time_now_day - offset)
time_end_str = str(time_now_day - offset_sec)

#print the date and time string
print(time_start_str)
print(time_end_str)


# In[131]:


# load the dataset
kpi_data = pd.read_csv('Performance 4.csv')


# In[48]:


#print(kpi_data)


# In[132]:


# perform data preprocessing
# drop irrelevant columns
kpi_data = kpi_data.drop(['Local time', 'Site ID', 'Cell name'] , axis=1)


# In[6]:


# perform normalization
#kpi_data_norm = (kpi_data - kpi_data.mean()) / kpi_data.std()


# In[133]:


# perform feature selection
# select top 5 most correlated features to the target variable
X = kpi_data.drop('MAC Cell thp PDSCH data slot t', axis=1)
y = kpi_data['MAC Cell thp PDSCH data slot t']

#print(X)
#print(y)


# In[134]:


selector = SelectKBest(f_classif, k=6)
#selector.fit(X, y)
#X_new = selector.transform(X)
X_new = SelectKBest(f_regression, k=6).fit_transform(X, y)
X_new = SelectKBest(mutual_info_regression, k=6).fit_transform(X, y)
#selected_features = X.columns[selector.get_support(indices=True)]


# In[25]:


# split the dataset into training and testing datasets
#split_index = int(0.3 * len(X_new))
#X_test = X_new[:split_index]
#y_test = y[:split_index]
#X_train = X_new[split_index:]
#y_train = y[split_index:]
#X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.3, random_state=500)


# In[135]:


split_index = int(len(X_new) * 0.7)

# Split the data into training and testing sets
X_train, X_test = X_new[:split_index], X_new[split_index:]
y_train, y_test = y[:split_index], y[split_index:]


# In[136]:


# train the model
#lab = preprocessing.LabelEncoder()
#y_transformed = lab.fit_transform(y_train)
#X_transformed = lab.fit_transform(X_train)

rfc = RandomForestRegressor(random_state=500)
rfc.fit(X_train, y_train)


# In[137]:


# evaluate the model
y_pred_RF = rfc.predict(X_test)
#print(y_pred_RF)


# In[138]:


print("Mean Squared Error:", mean_squared_error(y_test, y_pred_RF))
print("R-squared:", r2_score(y_test, y_pred_RF))
print('MAE: ', mean_absolute_error(y_test, y_pred_RF))
print('RMSE: ', np.sqrt(mean_squared_error(y_test, y_pred_RF)))


# In[55]:


# fine-tune the hyperparameters of the model
param_grid = {
    'n_estimators': [500, 1000, 1500],
    'max_depth': [20, 30, 40],
    'min_samples_split': [20, 25, 30],
    'min_samples_leaf': [8, 16, 20],
    'max_features': ['auto', 'sqrt', 'log2']
}

grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=10, scoring='neg_mean_squared_error')

# Label encoding

grid_search.fit(X_train, y_train)

#print(X_train)

#print(y_train)


# In[120]:


best_params = grid_search.best_params_
print("Best Parameters:", best_params)


# In[139]:


print(y)


# In[122]:


# create a new Random Forest Classifier object with the best hyperparameters
rfc_best = RandomForestRegressor (n_estimators= 1500 ,#best_params['n_estimators'],
                                   max_depth= 20   ,#best_params['max_depth'],
                                   min_samples_split= 20  ,#best_params['min_samples_split'],
                                   min_samples_leaf=  8 , #best_params['min_samples_leaf'],
                                   max_features=  'auto'   ,#best_params['max_features'],
                                   random_state=500)


rfc_best.fit(X_train, y_train)


y_pred_ev_RF = rfc_best.predict(X_test)


#print(y_pred_ev_RF)
#print(y_test)


# In[123]:


# evaluate the model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_ev_RF))
print("R-squared:", r2_score(y_test, y_pred_ev_RF))
print('MAE: ', mean_absolute_error(y_test, y_pred_ev_RF))
print('RMSE: ', np.sqrt(mean_squared_error(y_test, y_pred_ev_RF)))


# In[140]:


import matplotlib.pyplot as plt

index = np.arange(2767, 3954)

modified_index = np.arange(len(index))

plt.plot(modified_index, y_test, label='Real Throughput Values')
#plt.plot( y_test, label='Real Throughput Values')
plt.plot(y_pred_RF , label='Predicted Throughput Values')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Forest Based Prediciton')
plt.legend()
plt.show()


# In[61]:


# Define an initial range for epoch and batch size
epoch_range = [100, 250, 500, 1000, 1500]
batch_size_range = [64, 128, 256, 512, 1024]

# Track the best performing combination
best_epoch = None
best_batch_size = None
best_mse = np.inf

# Iterate through different combinations
for epoch in epoch_range:
    for batch_size in batch_size_range:
        # Create the LSTM model
        model = Sequential()
        model.add(LSTM(50, input_shape=(X_new.shape[1], 1)))
        model.add(Dense(1))
        
        # Compile the model
        model.compile(loss='mean_squared_error', optimizer='adam')
        
        # Train the model
        model.fit(X_train, y_train, epochs=epoch, batch_size=batch_size, verbose=0)
        
        # Evaluate the model on the test set
        mse = model.evaluate(X_test, y_test, verbose=0)
        
        # Track the best performing combination
        if mse < best_mse:
            best_mse = mse
            best_epoch = epoch
            best_batch_size = batch_size

# Print the best performing combination
print("Best Epoch:", best_epoch)
print("Best Batch Size:", best_batch_size)
print("Best MSE:", best_mse)


# In[141]:


# Train the model
# LSTM Model Development
model = Sequential()
model.add(LSTM(50, input_shape=(X_new.shape[1], 1)))
model.add(Dense(1))


# In[142]:


X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
model.compile(loss='mean_squared_error', optimizer='adam')
#model.fit(X_train, y_train, epochs=best_epoch, batch_size=best_batch_size, validation_data=(X_test, y_test))
model.fit(X_train, y_train, epochs=1500, batch_size=64, validation_data=(X_test, y_test))


# In[143]:


y_pred_LSTM = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_LSTM))
print("R-squared:", r2_score(y_test, y_pred_LSTM))
print('MAE: ', mean_absolute_error(y_test, y_pred_LSTM))
print('RMSE: ', np.sqrt(mean_squared_error(y_test, y_pred_LSTM)))


# In[18]:


import sys
get_ipython().system('{sys.executable} -m pip install seaborn')


# In[25]:


import seaborn as sns
sns.pairplot(kpi_data)


# In[96]:


import matplotlib.pyplot as plt

index = np.arange(1038, 1484)
modified_index = np.arange(len(index))
plt.plot(modified_index, y_test, label='Real Throughput Values')

plt.plot(y_pred_LSTM, label='Predicted Throughput-LSTM')
plt.plot(y_pred_RF, label='Predicted Throughput-RF')

plt.xlabel('Number of Samples')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput Prediction')
plt.legend()
plt.show()


# In[144]:



# Your previous code

index = np.arange(2767, 3954)
modified_index = np.arange(len(index))
plt.plot(modified_index, y_test, label='Real Throughput Values')
plt.plot(y_pred_LSTM, label='Predicted Throughput-LSTM')
plt.plot(y_pred_RF, label='Predicted Throughput-RF')
plt.xlabel('Number of Samples')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput Prediction')
plt.legend()

# Save the plot as an SVG file
svg_filename = 'throughput_prediction.svg'
plt.savefig(svg_filename, format='svg')

# Display the plot as SVG
display(SVG(svg_filename))


# In[24]:


kpi_data.describe()


# In[145]:


fig, axes = plt.subplots(3, 1, figsize=(8, 12))


# Customize each subplot
axes[0].plot(y_pred_RF, label='Predicted Values RF')
axes[0].set_title('Predicted Values RF')
axes[0].set_xlabel('Number of Samples')
axes[0].set_ylabel('Throughput (Mbps)')

axes[1].plot(y_pred_LSTM, label='Predicted Values LSTM')
axes[1].set_title('Predicted Values LSTM')
axes[1].set_xlabel('Number of Samples')
axes[1].set_ylabel('Throughput (Mbps)')

axes[2].plot(modified_index, y_test, label='Real Throughput Values')
axes[2].set_title('Throughput Value')
axes[2].set_xlabel('Number of Samples')
axes[2].set_ylabel('Throughput (Mbps)')

# Adjust spacing between subplots
plt.tight_layout()

# Save the plot as an SVG file
svg_filename = 'subplot_plots.svg'
plt.savefig(svg_filename, format='svg')

# Display the plot as SVG
display(SVG(svg_filename))


# In[ ]:





# In[ ]:




