#!/usr/bin/python

from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
 

# X, y = load_svmlight_file('datasets/home_2_5pt.svmlight')
# X, y = load_svmlight_file('datasets/com1_2_itr4.svmlight')
X, y = load_svmlight_file('datasets/com1_2_181014_itr5.svmlight')


# print X.shape
X_new = SelectKBest(chi2, k=8).fit_transform(X, y)
print "x_Old:", X.shape
print "X_New:", X_new.shape
