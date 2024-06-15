#!/usr/bin/env python
# coding: utf-8

# Geometric Brownian Motion with stock price

# In[ ]:





# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100  # initial stock price
mu = 0.05  # expected return
sigma = 0.2  # volatility
T = 1.0  # time horizon
N = 252  # number of time steps
dt = T / N  # time increment

# Generate stock price paths
np.random.seed(0)
t = np.linspace(0, T, N+1)
W = np.random.standard_normal(size=N+1)
W = np.cumsum(W) * np.sqrt(dt)  # Brownian motion
X = (mu - 0.5 * sigma**2) * t + sigma * W
#X = (mu) * t + sigma * W
S = S0 * np.exp(X)  # stock price process

# Plot stock price paths
plt.figure(figsize=(10, 6))
plt.plot(t, S)
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Paths using GBM')
plt.show()

