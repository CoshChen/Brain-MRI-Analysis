# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:07:53 2018

@author: Ko-Shin Chen
"""

import pandas as pd
from collections import OrderedDict

group = 'PD'

subjects = []

if group == 'PD':
    ID_prefix = 'PD'
    # no 6 and 14
    subjects = [i for i in range(1,6)] + [i for i in range(7,14)] + [i for i in range(15, 22)]
elif group == 'HC':
    ID_prefix = 'H'
    subjects = [i for i in range(1, 21)]

thickness_list = []
gm_list = []
csf_list = []
wm_list = []
area_list = []

for subj_id in subjects:
    ID = ID_prefix + '00' + str(subj_id)
    if subj_id >= 10:
       ID = ID_prefix + '0' + str(subj_id)
        
    df = pd.read_csv('./'+ group + ' T1/' + ID + '_T1_stat.csv').set_index('ROI_ID', drop = False)
    
    thickness = OrderedDict([('ID', ID)])
    gm = OrderedDict([('ID', ID)])
    csf = OrderedDict([('ID', ID)])
    wm = OrderedDict([('ID', ID)])
    area = OrderedDict([('ID', ID)])
    
    for roi in df['ROI_ID']:
        if roi in [1,2,3]:
            continue
        
        thickness[roi] = df.loc[roi,'Mean_Thickness(mm)']
        gm[roi] = df.loc[roi,'GM_Volume(mm^3)']
        csf[roi] = df.loc[roi,'CSF_Volume(mm^3)']
        wm[roi] = df.loc[roi,'WM_Volume(mm^3)']
        
        area[str(roi) + 'Mid'] = df.loc[roi,'Cortical_Area_mid(mm^2)']
        area[str(roi) + 'Inner'] = df.loc[roi,'Cortical_Area_inner(mm^2)']
        area[str(roi) + 'Pial'] = df.loc[roi,'Cortical_Area_pial(mm^2)']
    
    thickness_list.append(thickness)
    gm_list.append(gm)
    csf_list.append(csf)
    wm_list.append(wm)
    area_list.append(area)

pd.DataFrame(thickness_list).to_csv('./'+group+'_mean_thickness.csv', index=False)
pd.DataFrame(gm_list).to_csv('./'+group+'_gm_vol.csv', index=False)
pd.DataFrame(csf_list).to_csv('./'+group+'_csf_vol.csv', index=False)   
pd.DataFrame(wm_list).to_csv('./'+group+'_wm_vol.csv', index=False)
pd.DataFrame(area_list).to_csv('./'+group+'_cortical_area.csv', index=False)
        



