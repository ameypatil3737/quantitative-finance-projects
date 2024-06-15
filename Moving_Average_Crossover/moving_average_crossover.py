#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('./historical_stock_prices.csv', index_col='Date', parse_dates=True)
prices = data['Close']

# Calculate moving averages
short_window = 40
long_window = 100
signals = pd.DataFrame(index=prices.index)
signals['price'] = prices
signals['short_mavg'] = prices.rolling(window=short_window, min_periods=1, center=False).mean()
signals['long_mavg'] = prices.rolling(window=long_window, min_periods=1, center=False).mean()

# Generate signals
signals['signal'] = 0.0
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
signals['positions'] = signals['signal'].diff()

# Plot the signals
plt.figure(figsize=(12, 8))
plt.plot(signals['price'], label='Price')
plt.plot(signals['short_mavg'], label='40-day MA')
plt.plot(signals['long_mavg'], label='100-day MA')

plt.plot(signals.loc[signals.positions == 1.0].index, 
        signals.short_mavg[signals.positions == 1.0], 
        '^', markersize=10, 
        color='g', lw=0, label='Buy Signal')

plt.plot(signals.loc[signals.positions == -1.0].index, 
        signals.short_mavg[signals.positions == -1.0],
        'v', markersize=10,
        color='r', lw=0, label='Sell Signal')


plt.legend()
plt.show()




# In[ ]:




