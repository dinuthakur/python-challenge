#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:39:06 2023

@author: admin
"""

import numpy as np
import pandas as pd
import os

#check working directory
print(os.getcwd())

#change working directory if needed
#os.chdir("..")
#os.chdir("PyPoll")
#os.chdir('Documents/GitHub/python-challenge/PyPoll')

#load the data from the CSV
poldata = pd.read_csv('Resources/election_data.csv')

print(poldata)

#find total number of votes
total_votes = len(poldata.index)
print(total_votes)


#find number of votes per candidate
numvotes_charles_casper = np.sum(poldata['Candidate'] == 'Charles Casper Stockham')
numvotes_diana_degette = np.sum(poldata['Candidate'] == 'Diana DeGette')
numvotes_raymon_anthony = np.sum(poldata['Candidate'] == 'Raymon Anthony Doane')

#find percentage of votes per candidate
pctvotes_charles_casper = numvotes_charles_casper/total_votes*100
pctvotes_diana_degenette = numvotes_diana_degette/total_votes*100
pctvotes_raymon_anthony = numvotes_raymon_anthony/total_votes*100

#find winner
winner = poldata.mode()['Candidate'][0]

#print to console

print("Election Results\n")
print("----------------------------\n")
print("Total Months: " + str(total_votes))
print("\n----------------------------\n")
print("\nCharles Casper Stockham: %.3f" %pctvotes_charles_casper + "%" + " (" + str(numvotes_charles_casper) + ")")
print("\nDiana Degette: %.3f" %pctvotes_diana_degenette + "%" + " (" + str(numvotes_diana_degette) + ")")
print("\nRaymon Anthony Doane: %.3f" %pctvotes_raymon_anthony + "%" + " (" + str(numvotes_raymon_anthony) + ")")
print("\n----------------------------")
print("\nWinner: " + winner)

#write to file
f = open('analysis/election_results.txt', 'w')
f.write("Election Results\n")
f.write("\n----------------------------\n")
f.write("\nTotal Months: " + str(total_votes))
f.write("\n\n----------------------------\n")
f.write("\n\nCharles Casper Stockham: %.3f" %pctvotes_charles_casper + "%" + " (" + str(numvotes_charles_casper) + ")")
f.write("\n\nDiana Degette: %.3f" %pctvotes_diana_degenette + "%" + " (" + str(numvotes_diana_degette) + ")")
f.write("\n\nRaymon Anthony Doane: %.3f" %pctvotes_raymon_anthony + "%" + " (" + str(numvotes_raymon_anthony) + ")")
f.write("\n\n----------------------------")
f.write("\n\nWinner: " + winner)
f.close()