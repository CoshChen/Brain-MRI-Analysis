# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:19:08 2018

@author: Ko-Shin Chen
"""

import pandas as pd
from scipy.stats import ttest_ind
from collections import OrderedDict

row_list = []

for tab_name in ['_cortical_area', '_csf_vol', '_gm_vol', '_mean_thickness', '_wm_vol']:
    HC_group = pd.read_csv('HC' + tab_name + '.csv').drop(columns=['ID'])
    PD_group = pd.read_csv('PD' + tab_name + '.csv').drop(columns=['ID'])
    
    roi_list = HC_group.columns.tolist()
    
    for roi in roi_list:
        row = OrderedDict()
        row['ROI'] = roi + tab_name
        row['HC Mean'] = HC_group[roi].mean()
        row['HC Sd'] = HC_group[roi].std()
        row['PD Mean'] = PD_group[roi].mean()
        row['PD Sd'] = PD_group[roi].std()
        
        test = ttest_ind(HC_group[roi], PD_group[roi], equal_var=False)
        row['T Value'] = test[0]
        row['P Value'] = test[1]
        
        row_list.append(row)
        
pd.DataFrame(row_list).sort_values(by=['P Value']).to_csv('./ROI_two_groups_summary.csv', index=False)

