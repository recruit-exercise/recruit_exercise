import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def plot(df,column,x_numbers=10,rotation=0,color_list=["steelblue"]):
    temp = pd.concat([pd.Series(df[column].value_counts().index),
                        pd.Series(df[column].value_counts().values),
                        pd.Series((df[column].value_counts().cumsum()/df[column].value_counts().sum()).values)],
                      axis=1)
    label_data,value_data,cum_data =temp[0][:x_numbers],temp[1][:x_numbers],temp[2][:x_numbers]
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
    plt.hlines([0.8],-1,length,linestyles="dashed")
    ax1.set_xticklabels(label_data,rotation = rotation)
    ax2.set_ylim([0,1.0])
    