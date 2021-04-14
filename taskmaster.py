# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:05:21 2020

@author: Chuck
"""

import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

##Read in data; data obtained from https://task.fandom.com/wiki/
df = pd.read_csv("TaskmasterWins_s10.csv")
df['Sex_text'] = ['Male' if x == 1 else 'Female' for x in df['Sex']]

##Regression
#Hypothesis 1: POCs earn fewer points per episode than white competitors
formula_H1 = "Points_per_ep ~ POC + Sex_text"
md_H1 = smf.ols(formula_H1,data=df).fit()
print(md_H1.summary())

#Hypothesis 2: POCs win fewer episodes than white competitors
formula_H2 = "Percent_wins ~ POC + Sex_text"
md_H2 = smf.ols(formula_H2,data=df).fit()
print(md_H2.summary())

#Hypothesis 2: POCs are ranked lower (1 = best, 5 = worst) than white competitors
formula_H3 = "Rank ~ POC + Sex_text"
md_H3 = smf.ols(formula_H3,data=df).fit()
print(md_H3.summary())

#Visualize results for each hypothesis
for analysis,label in zip(['Rank','Points_per_ep','Percent_wins'],['Rank','Points per episode','Percent wins']):
    sns.catplot(x='POC',y=analysis,data=df,kind='box',legend=False)
    plt.xticks([0,1],['White','Non-White'])
    plt.xlabel("Race")
    plt.ylabel(label)
    plt.title("Taskmaster Winners (Series 1 - 10)")
    plt.legend(loc='upper right')

