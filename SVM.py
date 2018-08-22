# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:43:46 2018

@author: Ko-Shin Chen
"""

import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

npzfile = './all_subjects_pca_2.npz'
data = np.load(npzfile)

X = data['X']
y = data['y']
pred_y = []

sample_size = X.shape[0]

for i in range(sample_size):
    X_train = X[[j for j in range(i)] + [j for j in range(i, sample_size)],:]
    y_train = y[[j for j in range(i)] + [j for j in range(i, sample_size)]]
    svm_model = svm.SVC(kernel='linear').fit(X_train, y_train)
    pred_y.append(svm_model.predict([X[i,:]]))
    
    print('Sample ' + str(i))
    print('True y = ' + str(y[i]))
    print('Predicted y = ' + str(pred_y[-1]))
    print()


print(confusion_matrix(pred_y, y))



