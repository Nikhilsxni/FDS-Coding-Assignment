# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:51:27 2024

@author: Nikhil Soni
studentID: 22045846
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Update with your CSV file path
df = pd.read_csv("data6.csv")

# data is in the first column
salary_data = df.iloc[:, 0].values

# Create a histogram
plt.hist(salary_data, bins=30, density=True, alpha=0.7,
         color='green', edgecolor='black', linewidth=1.2)

# Calculate mean annual salary (W˜)
mean_salary = np.mean(salary_data)

# Calculate the fraction of population with salaries between W˜ and 1.25W˜ (X)
lower_bound = mean_salary
upper_bound = 1.25 * mean_salary
fraction_population = np.sum((salary_data >= lower_bound) & (
    salary_data <= upper_bound)) / len(salary_data)

# Print W˜ and X on the graph
plt.text(0.5, 0.95, f'Mean Salary ($W˜$): ${mean_salary:.2f}', transform=plt.gca(
).transAxes, fontsize=10, verticalalignment='top')
plt.text(0.5, 0.9, f'Fraction of Population between $W˜$ and $1.25W˜$ ($X$): {fraction_population:.2%}', transform=plt.gca(
).transAxes, fontsize=10, verticalalignment='top')

# Set labels and title
plt.xlabel('Salary')
plt.ylabel('Probability Density Function')
plt.title('Probability Density Function of Salaries')

# Display legend
plt.legend(['Salary Distribution'], loc="center right")

# Show the plot
plt.show()
