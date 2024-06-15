#!/usr/bin/env python
# coding: utf-8

# In[8]:


pwd()


# In[12]:


import numpy as np
import pandas as pd

def calculate_var(prices, confidence_level=0.95):
    returns = prices.pct_change().dropna()
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    print("len(sorted_returns):",len(sorted_returns)) #{len(sorted_returns)}")
    var = abs(sorted_returns[index])
    return var

# Load data
data = pd.read_csv('./historical_stock_prices.csv', index_col='Date', parse_dates=True)
prices = data['Close']

# Calculate VaR
var_95 = calculate_var(prices, 0.95)
print(f"95% VaR: {var_95}")


# In[ ]:




