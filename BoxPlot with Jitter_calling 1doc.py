# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:52:31 2021

@author: Sarah
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import scipy
import pandas as pd

# Working directory
Dir =r"C:\_Analysis"
if Dir[-1]!="/":
    Dir = Dir+"//"

#File to read
fileName = "name.xlsx"
filepath = Dir + fileName
df1 = pd.read_excel(filepath, skiprows=0, index_col=None)
data1 =df1.to_numpy()

# plot params
Plot_Name = 'name'
IndexCols = [0,1,2,3] # select column to plot and order
xtickslabel = ['A',"B",'C',"D"] #  plot headlines
ColorPalette = ["blue","magenta","orange", "green"]

xlim_min = 0
xlim_max = 1000


##
masterCols = []
for i in range(len(IndexCols)):
    masterCols.append(data1[:,IndexCols[i]])

nlabel = len(xtickslabel)
fig1 = sns.boxplot(data=masterCols, color='black',medianprops={'color':'black'}, boxprops=dict(facecolor="White"), width=0.15)
fig1 = sns.swarmplot(data=masterCols, alpha=0.5, palette = ColorPalette)
#plt.ylim([xlim_min, xlim_max])
plt.xticks(np.arange(nlabel), xtickslabel, rotation=45)
#sns.set_context('poster')


plt.savefig(Plot_Name+'.png' , dpi = 300, bbox_inches = 'tight')
#plt.show()
