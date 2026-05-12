import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

num=100
sales_volume=np.random.normal(1000,200,num)
unit_cost=np.random.uniform(5,15,num)
price=20
profit=(price-unit_cost)*sales_volume

plt.hist(profit,bins=50,edgecolor='black')
plt.title("Monte Carlo Simulation:Distribution of Profit")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()
print(f"Mean Profit: ${np.mean(profit):,.2f}")
print(f"5th percentile Profit: ${np.percentile(profit,5):,.2f}")