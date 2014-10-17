import pandas as pd
import pylab as pl

from sklearn.datasets import load_svmlight_file
from sklearn import svm
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
 

# X, y = load_svmlight_file('datasets/home_2_5pt.svmlight')
X, y = load_svmlight_file('datasets/com1_2_itr4.svmlight')

# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=200)
 
 
features = ['density', 'sulphates', 'residual_sugar']
 
results = []
for n in range(1, 20, 1):
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    # accuracy = np.where(preds==test['high_quality'], 1, 0).sum() / float(len(test))
    accuracy = clf.score(X_test, y_test)
    print "Neighbors: %d, Accuracy: %3f" % (n, accuracy)
 
    results.append([n, accuracy])
     
results = pd.DataFrame(results, columns=["n", "accuracy"])
 
pl.plot(results.n, results.accuracy)
pl.title("Accuracy with Increasing K")
pl.show()