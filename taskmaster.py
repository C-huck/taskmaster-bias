# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:05:21 2020

@author: Jack
"""

import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("TaskmasterWins_s10.csv")#,usecols=['Percent_wins','Sex','POC','Points_per_ep','Series'])
df['Sex_text'] = ['Male' if x == 1 else 'Female' for x in df['Sex']]
#df = df[df['Sex']=='Female']
#formula = "Percent_wins ~ C(Sex)+POC"
#formula = "Percent_wins ~ POC + Sex"
formula = "Points_per_ep ~ POC + Sex_text"
md = smf.ols(formula,data=df).fit()
md = smf.mixedlm(formula,data=df,groups=df['Series']).fit()
print(md.summary())

#plt.figure(num=None, figsize=(16, 24), dpi=200, facecolor='w', edgecolor='k')
sns.catplot(x='POC',y='Rank',data=df,kind='box',legend=False)
sns.catplot(x='POC',y='Points_per_ep',hue='Sex_text',data=df,kind='box',legend=False)
sns.catplot(x='POC',y='Percent_wins',hue='Sex_text',data=df,kind='box',legend=False)
#sns.catplot(x='POC',y='Points_per_ep',data=df,kind='box',legend=False)
plt.xticks([0,1],['White','Non-White'])
plt.xlabel("Race")
plt.ylabel("Percent episodes won")
plt.title("Taskmaster Winners (Series 1 - 10)")
#plt.savefig("out.png")
plt.legend(loc='upper right')

df['Sex'].count("Male")
Counter(df['POC'])


for x in set(df['Series']):
    temp = df[df['Series']==x]
    temp['rank'] = temp['Total_points'].rank(method='max')
    print(temp)
    
    
df[df['POC']==1]['Rank'].mean()
df[df['POC']==0]['Rank'].mean()

pearsonr(df1[df1['tr_bin']=='g']['dist_from_50'],df1[df1['tr_bin']=='g']['embedding_score'])

smf.ols("embedding_score ~ dist_from_50",data=df1[df1['tr_bin']=='g']).fit().summary()
(-0.3106594461924802)**2
