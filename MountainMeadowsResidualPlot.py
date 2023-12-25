import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

years = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
profits = np.array([911, 850, 900, 925, 901, 1020, 999, 903, 800, 503, 489, 881, 903, 844, 870, 475, 809, 463, 893, 884])

years_reshape = years.reshape(-1, 1)

# Fit linear regression model
model = LinearRegression().fit(years_reshape, profits)

# Predict profits
predicted_profits = model.predict(years_reshape)

# Calculate residuals
residuals = profits - predicted_profits

# Plot residuals
plt.scatter(years, residuals)
plt.axhline(0, color='red', linestyle='--', linewidth=2) 
plt.title('Residuals for Mountain Meadows')
plt.xlabel('Year')
plt.ylabel('Residual')
plt.show()
