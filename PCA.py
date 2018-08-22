# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:39:16 2018

@author: Ko-Shin Chen
"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


data = np.load('./all_subjects.npz')
X = data['X']
y = data['y']

stX = StandardScaler().fit_transform(X)

n = 2 #23
pca = PCA(n_components=n)
X_pca = pca.fit_transform(X = stX)

print(pca.explained_variance_)
np.savez('./all_subjects_pca_'+str(n)+'.npz', X = X_pca, y=y)




