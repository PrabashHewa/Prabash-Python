#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import SVG, display
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_regression
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *


# In[2]:


engine = create_engine('druid://druid-broker:8082/druid/v2/sql/')  # uses HTTP by default :(
cnxn = engine.connect()


# In[3]:


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


# In[60]:


sql1_temp = """
SELECT TIME_FLOOR(CAST(TIME_SHIFT(__time, 'PT15M', 8) AS TIMESTAMP), 'P1D') AS "local_time",
       LOOKUP(distName, 'cell_dn_site_id') AS "site_id",
       LOOKUP(distName, 'cell_dn_carrier') AS "carrier",
       sum("M55308C00005") AS "DATA_SLOT_PDSCH",
       sum("M55309C01001") AS "DL_MAC_SDU_VOL_DTCH",
       sum("M55308C02000") AS "ACC_UE_DL_DRB_DATA",
       sum("M55308C27001") AS "ACC_UE_DL_SLEEP_DATA",
       sum("M55308C00008") AS "DATA_SLOT_PDSCH_TIME",
       sum("M55304C00001") AS "MEAS_PERIOD_NR_MAC_PDU_TPU",
       sum("M55308C10001") AS "PRB_USED_PDSCH",
       sum("M55308C17001") AS "ACC_SCHED_UE_PDSCH",
       sum("M55308C10003") AS "PRB_AVAIL_PDSCH",
       sum("M55304C00001") AS "MEAS_PERIOD_NR_MAC_PDU_TPUT"
FROM "druid"."NR_NRCELL"
WHERE TIME_SHIFT(__time, 'PT15M', 8) >= '#TIME_START#'
  AND TIME_SHIFT(__time, 'PT15M', 8) < '#TIME_END#'
GROUP BY TIME_FLOOR(CAST(TIME_SHIFT(__time, 'PT15M', 8) AS TIMESTAMP), 'P1D'),
         LOOKUP(distName, 'cell_dn_site_id'),
         LOOKUP(distName, 'cell_dn_carrier')
ORDER BY "DATA_SLOT_PDSCH" DESC
LIMIT 1000 """


# In[61]:


sql2_temp = """
SELECT TIME_FLOOR(CAST(TIME_SHIFT(__time, 'PT15M', 8) AS TIMESTAMP), 'P1D') AS "local_time",
       LOOKUP(distName, 'cell_dn_site_id') AS "site_id",
       LOOKUP(distName, 'cell_dn_carrier') AS "carrier",
       8*sum(M55309C01001)/(sum(M55308C02000)*sum(M55308C00008)/sum(M55308C00005)) AS "Avg MAC user thp DL",
       8*sum(M55309C02001)/(sum(M55308C02002)*sum(M55308C00009)/sum(M55308C00006)) AS "Avg MAC user thp UL",
       8*SUM(NVL(M55309C01001, 0.0))/(SUM(NVL(M55308C02000, 0.0)-NVL(M55308C27001, 0.0))*SUM(NVL(M55308C00008, 0.0))/SUM(NVL(M55308C00005, 0.0))) AS "nr_5100c_avg_mac_user",
       100*SUM(NVL(M55308C00003, 0.0))/SUM(NVL(M55308C00001, 0.0)+NVL(M55308C00002, 0.0)+NVL(M55308C00003, 0.0)+NVL(M55308C00004, 0.0)) AS "nr_127a_5g_ss_burst_",
       (8*(SUM(NVL(M55304C01000, 0.0)+NVL(M55304C01001, 0.0)+NVL(M55304C01002, 0.0)+NVL(M55304C01003, 0.0)+NVL(M55304C01004, 0.0)+NVL(M55304C01005, 0.0)+NVL(M55304C01006, 0.0)+NVL(M55304C01007, 0.0)+NVL(M55304C01008, 0.0)+NVL(M55304C01009, 0.0)+NVL(M55304C01010, 0.0)+NVL(M55304C01011, 0.0)+NVL(M55304C01012, 0.0)+NVL(M55304C01013, 0.0)+NVL(M55304C01014, 0.0)+NVL(M55304C01015, 0.0)+NVL(M55304C01016, 0.0)+NVL(M55304C01017, 0.0)+NVL(M55304C01018, 0.0)+NVL(M55304C01019, 0.0)+NVL(M55304C01020, 0.0)+NVL(M55304C01021, 0.0)+NVL(M55304C01022, 0.0)+NVL(M55304C01023, 0.0)+NVL(M55304C01024, 0.0)+NVL(M55304C01025, 0.0)+NVL(M55304C01026, 0.0)+NVL(M55304C01027, 0.0)+NVL(M55304C01028, 0.0)+NVL(M55304C05000, 0.0)+NVL(M55304C05001, 0.0)+NVL(M55304C05002, 0.0)+NVL(M55304C05003, 0.0)+NVL(M55304C05004, 0.0)+NVL(M55304C05005, 0.0)+NVL(M55304C05006, 0.0)+NVL(M55304C05007, 0.0)+NVL(M55304C05008, 0.0)+NVL(M55304C05009, 0.0)+NVL(M55304C05010, 0.0)+NVL(M55304C05011, 0.0)+NVL(M55304C05012, 0.0)+NVL(M55304C05013, 0.0)+NVL(M55304C05014, 0.0)+NVL(M55304C05015, 0.0)+NVL(M55304C05016, 0.0)+NVL(M55304C05017, 0.0)+NVL(M55304C05018, 0.0)+NVL(M55304C05019, 0.0)+NVL(M55304C05020, 0.0)+NVL(M55304C05021, 0.0)+NVL(M55304C05022, 0.0)+NVL(M55304C05023, 0.0)+NVL(M55304C05024, 0.0)+NVL(M55304C05025, 0.0)+NVL(M55304C05026, 0.0)+NVL(M55304C05027, 0.0)))/SUM(NVL(M55304C00001, 0.0)))/(SUM(NVL(M55308C10001, 0.0))/SUM(NVL(M55308C10003, 0.0)))/(SUM(NVL(M55308C17001, 0.0))/SUM(NVL(M55308C00005, 0.0)+NVL(M55308C00015, 0.0)+NVL(M55308C00017, 0.0))) AS "nr_5244b_sched_mac_pd",
       100*SUM(M55308C00015)/SUM(M55308C00003) AS "nr_1239a_ssb_sl_sched"
FROM "druid"."NR_NRCELL"
WHERE TIME_SHIFT(__time, 'PT15M', 8) >= '#TIME_START#'
  AND TIME_SHIFT(__time, 'PT15M', 8) < '#TIME_END#'
GROUP BY TIME_FLOOR(CAST(TIME_SHIFT(__time, 'PT15M', 8) AS TIMESTAMP), 'P1D'),
         LOOKUP(distName, 'cell_dn_site_id'),
         LOOKUP(distName, 'cell_dn_carrier')
ORDER BY "Avg MAC user thp DL" DESC
LIMIT 1000"""


# In[2]:


# Load the data
kpi_data = pd.read_csv("Quality Score1.csv")


# In[3]:


#sqla = sql1_temp.replace("#TIME_START#", time_start_str).replace("#TIME_END#", time_end_str)
#sqlb = sql2_temp.replace("#TIME_START#", time_start_str).replace("#TIME_END#", time_end_str)


# In[4]:


#kpi_data1 = pd.read_sql(sqla, cnxn)
#kpi_data2 = pd.read_sql(sqlb, cnxn)


# In[5]:


#kpi_data =  pd.merge(kpi_data1, kpi_data2)


# In[3]:


# Drop any rows with missing data
kpi_data = kpi_data.drop(['Local time', 'Site ID', 'Cell name'] , axis=1)


# In[4]:


# perform normalization
kpi_data = (kpi_data - kpi_data.mean()) / kpi_data.std()


# In[5]:


# Convert the target variable to numeric
kpi_data['Quality Score'] = pd.to_numeric(kpi_data['Quality Score'], errors='coerce')


# In[6]:


# Convert categorical variables to one encoding
#kpi_data = pd.get_dummies(kpi_data, columns=['nr_5244b_sched_mac_pd'])
#print(kpi_data)


# In[6]:


# Compute the correlation matrix
corr = kpi_data.corr()
print(corr)


# In[7]:


# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))
print(mask)


# In[8]:


# Select the features with the highest correlation to the target variable
kpi_data = kpi_data.astype(float)
selector = SelectKBest(f_regression, k=3)
selector.fit(kpi_data.drop(columns=['Quality Score']), kpi_data['Quality Score'])


# In[9]:


# Get the indices of the selected features
selected_features = np.argsort(selector.scores_)[::-1][:5]


# In[10]:


# Print the selected features
print(kpi_data.drop(columns=['Quality Score']).columns[selected_features])


# In[23]:


# Plot the correlation matrix
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True)
svg_CFSscore = 'correlation_heatmap.svg'
plt.savefig(svg_CFSscore, format='svg')
#plt.savefig("correlation_heatmap.svg", format='svg')

# Display the plot as SVG

# Display the plot as SVG
display(SVG(svg_CFSscore))
#Display the plot as SVG
plt.show()
#sns.pairplot(selected_features)


# In[12]:





# In[ ]:




