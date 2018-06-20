import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def count_plot(df,column,x_numbers=10,rotation=0,color_list=["steelblue"],ABC=False,hline_cum=0.8):
    temp = pd.concat([pd.Series(df[column].value_counts().index),
                        pd.Series(df[column].value_counts().values),
                        pd.Series((df[column].value_counts().cumsum()/df[column].value_counts().sum()).values)],
                      axis=1)
    label_data,value_data,cum_data =temp[0][:x_numbers],temp[1][:x_numbers],temp[2][:x_numbers]
    plot(label_data,value_data,cum_data,x_numbers=x_numbers,rotation=rotation,color_list=color_list,ABC=ABC,hline_cum=hline_cum)
def group_sum_plot(df,group_column,sum_column,x_numbers=10,rotation=0,color_list=["steelblue"],ABC=False,hline_cum=0.8):
    temp = df.groupby(group_column)[sum_column].sum().sort_values(ascending=False)
    label_data = pd.Series(temp.index)[:x_numbers]
    value_data = pd.Series(temp.values)[:x_numbers]
    cum_data = pd.Series((temp.cumsum()/temp.sum()).values)[:x_numbers]
    plot(label_data,value_data,cum_data,x_numbers=x_numbers,rotation=rotation,color_list=color_list,ABC=ABC,hline_cum=hline_cum)

def plot(label_data,value_data,cum_data,x_numbers=10,rotation=0,color_list=["steelblue"],ABC=False,hline_cum=0.8):
    if ABC:
        color_list = cum_data.apply(lambda x: "r" if x <= 0.70 else "g" if x <= 0.9 else "b")        
    length = len(label_data)
    fig,ax1 = plt.subplots()
    ax1.bar(
            left = np.arange(length),
            height = value_data,
            tick_label = label_data,
            color = color_list
            )
    ax2 = ax1.twinx()
    ax2.plot(cum_data,color='k')
    plt.hlines([hline_cum],-1,length,linestyles="dashed")
    ax1.set_xticklabels(label_data,rotation = rotation)
    ax2.set_ylim([0,1.0])
    