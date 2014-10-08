#!/usr/bin/python

import pickle
import os
import operator

from sklearn import datasets
from sklearn.datasets import load_svmlight_file
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier



class Snapper:
    def __init__(self):
        self.data = []


    def load(self, filepath):
        """ Loads a new dataset
        """
        f = open (str(filepath), 'rb')
        self.data = pickle.load(f)
        f.close()


    def save(self, filepath):
        """Saves the dataset 
        """
        f = open (str(filepath), 'wb')
        pickle.dump(self.data, f, -1) # -1 to use latest protocol
        f.close()


    def append(self, record):
        """Adds a new record to the data. 
        Record must be in the form:
        {
            'target': <int>,
            'data': {
                'entry1' : <number>,
                'entry2' : <number>,
                ...
                ...
                ...
            }
        }
        """
        self.data.append(record)


    def getKeys(self, data):
        """ Internal function to generate unique keys
        """
        total = []
        for record in data:
            keys = list(record.get('data').keys())
            total = set().union(total, keys)
        total = list(total)
        total.sort()
        result = {}
        for i, key in enumerate(total):
            result[key] = i
        return result


    def export(self, filepath=None):
        """ Exports to SVMLight format.  If filepath is specified, returns
            writes to the file.  Else returns output, as a string.
        """

        def exportString(data):
            """ Internal function to export to string format
            """
            keys = self.getKeys(self.data)
            resultDoc = '## SVM Light exported output ##\n'
            for record in self.data:
                entry = str(record.get('target')) + ' '
                for key, val in record.get('data').iteritems():
                    entry += str(keys.get(key)) + ':' + str(val) + ' '
                entry += '\n'
                resultDoc += entry
            return resultDoc

        result = exportString(self.data)
        if (filepath == None):
            return result 
        else:
            f = open(filepath, 'w')
            f.write(result)
            f.close()


    def reset(self):
        """ Resets the data vector. 
        """
        self.data = []


    def train(self):
        """ Trains the data set. 
        """
        # Create a tmp file, then remove it for SKLearn dependency purposes
        self.export('.tmp.dataset.exptd')
        x_train, y_train = load_svmlight_file('.tmp.dataset.exptd')
        self.model = KNeighborsClassifier(n_neighbors=10)
        self.model.fit(x_train, y_train) 
        os.remove('.tmp.dataset.exptd')

        ## Creates keys to for predicting, later.
        self.keys = self.getKeys(self.data)


    def _recordToSvmRecord(self, features):
        """ Converts a record to SVM Light format 
        """
        length = 0
        for key, val in self.keys.iteritems():
            if (val > length):
                length = val
        length += 1
        result = [None] * length

        ## Key corresponds to integer idx, while keys 
        ## is a dictionary consisting of key mappings 
        ## to these integers.
        for key, val in features.iteritems():
            keys = self.keys
            result[keys.get(key)] = val

        print result
        return result


    def predict(self, features):
        """Predict whether a value will work 
        """
        toTest = [self._recordToSvmRecord(features)]
        print toTest
        print self.model.predict(toTest)





###################################
##  Main program defined here    ##
###################################

def runMain():
    """ Main function called when run as standalone daemon
    """
    print 'Welcome to Snapper.'
    print 'Snapper cannot be run headless.'
    print 'Please run Snapper from your code.'


if __name__ == '__main__':
    runMain()

