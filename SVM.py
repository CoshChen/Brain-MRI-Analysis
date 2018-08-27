# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:43:46 2018

@author: Ko-Shin Chen
"""

import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn import svm
from sklearn.metrics import confusion_matrix

npzfile = './all_subjects.npz'
data = np.load(npzfile)

c = 0.005

X = data['X']
y = data['y']
field_dict = data['field_dict'].item()

pred_y = []
model_coef = []

sample_size = X.shape[0]


for i in range(sample_size):
    X_train = X[[j for j in range(i)] + [j for j in range(i, sample_size)],:]
    y_train = y[[j for j in range(i)] + [j for j in range(i, sample_size)]]
    svm_model = svm.LinearSVC(C=c, penalty="l1", dual=False, fit_intercept=False).fit(X_train, y_train) 
    pred_y.append(svm_model.predict([X[i,:]])[0])
    model_coef.append(svm_model.coef_)
    
    if pred_y[-1] != y[i]:
        print('Wrong Prediction: Sample ' + str(i))

mean_coef = np.mean(model_coef, axis=0)[0]
row_list = []

for idx in range(np.shape(mean_coef)[0]):
    if mean_coef[idx] != 0:
        row = OrderedDict()
        row['ROI'] = field_dict[idx]
        row['Mean Coef'] = mean_coef[idx]
        row_list.append(row)

print()        
print(confusion_matrix(pred_y, y))

pd.DataFrame(row_list).sort_values(by=['Mean Coef'], ascending=False).to_csv('./SVM_'+str(c)+'.csv', index=False)



