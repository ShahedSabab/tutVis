# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:00:08 2018

@author: sabab05
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:43:03 2018

@author: sabab05
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 02:03:18 2018

@author: sabab05
"""

import pandas as pd 
from collections import Counter
import plotly.plotly as py
import plotly.tools as tls
import matplotlib.pyplot as plt
import numpy as np
import random
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 

path = r'''D:\CLoud\Academic\Research\___\Analysis (Photoshop)\4.2 Analysis Visualization - pyLDAvis (Using 750 symmetrical data)\1. Feature (Words)\Topic Model\Trial COdes\Model\dominant_topic_mallet_30_V1.csv'''
adv_topic_avg = []
beg_topic_avg = []
labels = ['Advance','Beginner']


def freq_dist(list_item):
    item_freq = Counter(list_item) 
    item_freq = sorted(item_freq.items(), key=lambda s: s[0])
    return item_freq       

def check_items(dict_item):
    global number_of_topics
    
    for x in range(1,number_of_topics+1):
        if float(x) not in dict_item.keys():
            dict_item[float(x)]=0
    dict_item = sorted(dict_item.items(), key=lambda s: s[0])
    return dict_item
    
        
number_of_adv=375 
number_of_beg=375    
number_of_topics = 30
opacity = 0.6
df = pd.read_csv(path) 


adv_rows = df.head(number_of_adv)
beg_rows = df.tail(number_of_beg)

adv_topic_list = adv_rows[(df.columns.values[1])]
beg_topic_list = beg_rows[(df.columns.values[1])]




adv_fd = dict(freq_dist(adv_topic_list))
beg_fd = dict(freq_dist(beg_topic_list))

#cehck items assign 0 to the missing topic value 
adv_fd = dict(check_items(adv_fd))
beg_fd = dict(check_items(beg_fd))

print(adv_fd)
print(beg_fd)

adv_sample = [adv_val for adv_val in adv_fd.values()]
beg_sample = [beg_val for beg_val in beg_fd.values()]


topic_wise_total_documents = [sum(x) for x in zip(adv_sample, beg_sample)]

print(topic_wise_total_documents)


N = number_of_topics
xtickLabel = []
for i in range (1,number_of_topics+1):    
    xtickLabel.append("T"+str (i))
    
    
number_of_colors = number_of_topics


# =============================================================================
# bar chart
    
topics = xtickLabel
adv = adv_sample
beg = beg_sample
ind = [x for x, _ in enumerate(topics)]

plt.bar(ind, adv, width=0.8, label='Advanced', color='blue',alpha = opacity)
plt.bar(ind, beg, width=0.8, label='Beginner', color='red', alpha = opacity,bottom=adv)

plt.xticks(ind, topics)
plt.ylabel("Number of Documents",fontsize=16)
plt.xlabel("Topics",fontsize=16)
plt.legend(loc="upper right",fontsize=16)
plt.title("Advanced vs Beginner Document Distribution Per Topic",fontsize=16)

plt.show()

# =============================================================================
