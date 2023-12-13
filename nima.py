# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:47:47 2023

@author: admin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy.stats import skew

#import seaborn as sns


def read_data(filename):
    # Reads data from csv file
    df_co2 = pd.read_csv(filename, skiprows= 4)
    # Returns the dataframe
    return df_co2
    
df = read_data("climatedataset.csv")

def co2_data( df, column, value, countries, years):
    # Groups data with column value
    cdf = df.groupby(column, group_keys=True)
    cdf =  cdf.get_group(value)
    # Resets the index
    cdf =  cdf.reset_index()
    
    cdf.set_index('Country Name', inplace=True)
    cdf =  cdf.loc[:, years]
    cdf =  cdf.loc[countries,:]
    # Clean the dataframe
    cdf =  cdf.dropna(axis=1)
    # Reset the index
    cdf=  cdf.reset_index()
    # Transposing the index of the dataframe
    trnspsd_data =  cdf.set_index('Country Name')
    trnspsd_data = trnspsd_data.transpose()
    # Returns normal dataframe and transposed dataframe
    return  cdf, trnspsd_data

def bar_plot( df, title, xlabel, ylabel):
    df.plot.bar(x='Country Name', rot=0, figsize=(50,25), fontsize=50)
    plt.yticks()
    plt.legend(fontsize=50)
    plt.title(title.upper(), fontsize=60, fontweight='bold')
    plt.xlabel(xlabel, fontsize=60)
    plt.ylabel(ylabel, fontsize=60)
    plt.savefig(title + '.png')
    plt.show()
    return

def line_plot( df, title, xlabel, ylabel):
    df.plot.line(figsize=(50,30), fontsize=60, linewidth=6.0)
    plt.yticks()
    plt.title(title.upper(), fontsize=70, fontweight='bold')
    plt.xlabel(xlabel, fontsize=70)
    plt.ylabel(ylabel, fontsize=70)
    plt.legend(fontsize=60)
    plt.savefig(title + '.png')
    plt.show()
    return

def stat_data(df, col, value, yr, a):
    df_stat = df.groupby(col,group_keys=True)
    df_stat = df_stat.get_group(value)
    df_stat = df_stat.reset_index()
    df_stat.set_index('Indicator Name', inplace=True)
    df_stat = df_stat.loc[:,yr]
    df_stat = df_stat.transpose()
    df_stat = df_stat.loc[:, a]
    return df_stat

def heat_map(data):
    plt.figure(figsize=(80, 40))
    sns.heatmap(data.corr(), annot=True, annot_kws={"size": 32})
    plt.title("Brazil's Heatmap".upper(), size=40, fontweight='bold')
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=50)
    plt.yticks(rotation=0,fontsize=50)
    plt.savefig('Heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    return data

#Calling functions


#creating list of countries and years for plotting bar plot
country1 = ['Canada', 'Afghanistan', 'India', 'Nigeria']
year1 = ['2000', '2005', '2010', '2015', '2020']

# Reads data from csv file
world_data = read_data("climatedataset.csv")
world_data1, transdata1 = co2_data(world_data, 'Indicator Name', 'Urban population', country1 ,year1 )
#prints filtered data and transposed data
print(world_data1)
print(transdata1)
# Calling bar plot function with indicator as population growth
bar_plot(world_data1, 'Year', 'Countries','Urban population growth (annual %)')

# Calling line plot function with indicator as population growth
line_plot(world_data1, 'Year', 'Countries','Urban population growth (annual %)')

world_data2, transdata2 = co2_data(world_data, 'Indicator Name', 'Population, total',country1 ,year1 )
#prints filtered data and trasposed data
print(world_data2)
print(transdata2)

# Calling bar plot function with indicator as total population
bar_plot(world_data1, 'Year', 'countries','Population, total')

# Calling line plot function with indicator as total population 
line_plot(world_data1, 'Year', 'countries','Population, total')

#creating variable with years
year_ht =['2000', '2005', '2010', '2015', '2020']
#creating variable for heat map
indicators= ['Urban population (% of total population)', 'Population, total','CO2 emissions from liquid fuel consumption (kt)',
           'Agricultural land (sq. km)','Cereal yield (kg per hectare)']
data_ht= stat_data(world_data,'Country Name','Iraq' ,year_ht , indicators)

print(data_ht.head())
#calling function heat map
heat_map(data_ht)

start = 2000
end= 2020
yeardes = [str(i) for i in range (start, end+1)]
indicator2 = ['Urban population (% of total population)', 'Population, total','CO2 emissions from liquid fuel consumption (kt)','Agricultural land (sq. km)']
descr = stat_data(world_data, 'Country Name','Iraq',yeardes ,indicator2 )
stats_summary = descr.describe()
print(stats_summary)
skewness = descr['Urban population (% of total population)'].skew()
print(f'Skewness: {skewness}')