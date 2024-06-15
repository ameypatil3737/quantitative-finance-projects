#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

def binomial_tree(S, K, T, r, sigma, N, option_type='call'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize asset prices at maturity
    ST = np.zeros(N + 1)
    for i in range(N + 1):
        ST[i] = S * (u ** (N - i)) * (d ** i)
    
    # Initialize option values at maturity
    if option_type == 'call':
        option_values = np.maximum(0, ST - K)
    elif option_type == 'put':
        option_values = np.maximum(0, K - ST)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    
    # Step backwards through the tree
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = np.exp(-r * dt) * (p * option_values[i] + (1 - p) * option_values[i + 1])
    
    return option_values[0]

# Example usage
S = 100  # Current stock price
K = 100  # Strike price
T = 1.0  # Time to maturity (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility
N = 50  # Number of time steps

call_price = binomial_tree(S, K, T, r, sigma, N, option_type='call')
put_price = binomial_tree(S, K, T, r, sigma, N, option_type='put')

print(f"Call Price: {call_price}")
print(f"Put Price: {put_price}")


# In[ ]:




