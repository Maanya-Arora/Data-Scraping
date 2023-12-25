import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

profits_white_haven = np.array([825, 759, 823, 800, 705, 310, 866, 854, 744, 533, 488, 782, 790, 792, 980, 518, 810, 480, 909, 720]).reshape(-1, 1)

def calculate_and_plot_regression(x, y, resort_name):
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)

    # Plotting the actual data points
    plt.scatter(x, y, label='Actual Profit')

    # Plotting the regression line
    plt.plot(x, y_pred, color='red', label='Linear Regression')

    # Displaying the equation of the regression line and correlation coefficient
    equation = f'y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}'
    r2 = r2_score(y, y_pred)
    correlation_coefficient = np.sqrt(r2)
    plt.text(0.05, 0.85, f'Equation: {equation}\nCorrelation Coefficient: {correlation_coefficient:.2f}', transform=plt.gca().transAxes)
    plt.xticks(np.arange(min(x), max(x)+1, 1), rotation='vertical')
    plt.legend(loc='lower left')

    plt.title(f'Profit Trend for {resort_name}')
    plt.xlabel('Year')
    plt.ylabel('Profit ($ thousands)')
    plt.show()

years_white_haven = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

calculate_and_plot_regression(years_white_haven.reshape(-1, 1), profits_white_haven, 'White Haven')
