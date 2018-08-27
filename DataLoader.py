# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:19:31 2018

@author: Ko-Shin Chen
"""

import pandas as pd
import numpy as np


groups = ['HC', 'PD']
tab_names = ['_cortical_area', '_csf_vol', '_gm_vol', '_mean_thickness', '_wm_vol']

group_combined_tabs = []
group_label = -1
labels = []
field_list = []
field_collect_done = False

for g in groups:
    sample_size = None
    tab_collect = []
    group_label += 1
    
    for tab in tab_names:
        df = pd.read_csv('./'+ g + tab + '.csv').set_index('ID').dropna(axis=1, how='all')
        df = df.apply(lambda x: x.fillna(x.mean()), axis=0)
        
        if sample_size is None:
            sample_size = df.shape[0]
            print('Sample size in ' + g + ': ' + str(sample_size))
            labels.append(np.zeros(sample_size) + group_label)
                
        tab_collect.append(df)
        
        if not field_collect_done:
            field_list.extend([name+tab for name in df.columns.values.tolist()])
        
    group_combined_tabs.append(pd.concat(tab_collect, axis=1))
    
    if not field_collect_done:
        field_collect_done = True
    
all_samples = pd.concat(group_combined_tabs, axis=0)
X = all_samples.values
y = np.concatenate(labels)

field_dict = {}
for idx in range(len(field_list)):
    field_dict[idx] = field_list[idx]

print(X.shape)
print(y.shape)

np.savez('./all_subjects.npz', X=X, y=y, field_dict=field_dict)

