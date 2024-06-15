#!/usr/bin/env python
# coding: utf-8

# Project Example: Implement the Black-Scholes formula for European option pricing.

# In[ ]:





# In[2]:


from scipy.stats import norm
import numpy as np

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    
    return price

# Example usage
S = 100  # Current stock price
K = 100  # Strike price
T = 1.0  # Time to maturity (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

call_price = black_scholes(S, K, T, r, sigma, option_type='call')
put_price = black_scholes(S, K, T, r, sigma, option_type='put')

print(f"Call Price: {call_price}")
print(f"Put Price: {put_price}")


# In[ ]:




