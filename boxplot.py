#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:23:42 2022

@author: macbook
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats



import regex as re
df = pd.DataFrame()
df = pd.DataFrame()

winers = pd.DataFrame()
names = ["crossover_nhidden5_gen15_enemy[2, 5, 8]_winners","crossover_nhidden5_gen15_enemy[3, 4, 7]_winners",
         "crossover_nhidden5_gen15_enemy[2, 5, 8]_pop70_winners","crossover_nhidden5_gen15_enemy[3, 7, 4]_pop70_winners"]
plt.figure()
for file in names:
    df = pd.read_csv(f"{file}.csv")
    winers[f"{file}"] = df["gain"]

plt.boxplot(winers)
plt.xticks(np.arange(0, 2, 2))
plt.xticks([1, 2, 3, 4], ['Algorithm 1 \ngroup 1', 'Algorithm 1 \ngroup 2', 'Algorithm 2 \ngroup 1',"Algorithm 2 \ngroup 2"])

plt.ylabel("Individual Gain")
plt.xlabel('')
plt.title('Individual Gain\nAlgorithm 1 vs Algorithm 2')
plt.savefig(f"Boxplot/boxplotexp2", dpi=400)
plt.show()


print("******************************************************************")
print("Variance in algorithm 1 vs Variance in algorithm 2 for set 1")
print(np.var(winers.iloc[:,0]), np.var(winers.iloc[:,2]))
print("T-Test results:")
print(stats.ttest_ind(winers.iloc[:,0], winers.iloc[:,2], equal_var = False))
print("******************************************************************")

print("******************************************************************")
print("Variance in algorithm 1 vs Variance in algorithm 2 for set 2")
print(np.var(winers.iloc[:,1]), np.var(winers.iloc[:,3]))
print("T-Test results:")
print(stats.ttest_ind(winers.iloc[:,1], winers.iloc[:,3], equal_var = False))
print("******************************************************************")