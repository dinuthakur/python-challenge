#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:35:42 2023

@author: admin
"""

import numpy as np
import pandas as pd
import os

#check working directory
print(os.getcwd())

#change working directory if needed
#os.chdir('Documents/GitHub/python-challenge/PyBank')

#load the data from the CSV
findata = pd.read_csv('Resources/budget_data.csv')

print(findata)

#find total number of months
total_months = len(findata.index)

#find total
total = np.sum(findata['Profit/Losses'])

#find average change
findata['changeInProfit'] = findata['Profit/Losses'].diff()
average_change = np.mean(findata['changeInProfit'])

#find maximum and minimum change and where they are located

index_max = findata['Date'][findata['changeInProfit'].idxmax()]
max_profit = findata['changeInProfit'].max()

index_min = findata['Date'][findata['changeInProfit'].idxmin()]
min_profit = findata['changeInProfit'].min()

#print to console

print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months: " + str(total_months))
print("\nTotal: $" + str(total))
print("\nAverage Change: $%.2f" % average_change)
print("\nGreatest increase in profits: " + index_max +" ($%.0f)" %max_profit)
print("\nGreatest decrease in profits: " + index_min +" ($%.0f)" %min_profit)

#write to file
f = open('analysis/financial_analysis.txt', 'w')
f.write("Financial Analysis\n\n")
f.write("----------------------------\n\n")
f.write("Total Months: " + str(total_months))
f.write("\n\nTotal: $" + str(total))
f.write("\n\nAverage Change: $%.2f" % average_change)
f.write("\n\nGreatest increase in profits: " + index_max +" ($%.0f)" %max_profit)
f.write("\n\nGreatest decrease in profits: " + index_min +" ($%.0f)" %min_profit)
f.close()