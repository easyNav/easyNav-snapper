#!/usr/bin/python

import pickle


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


    def export(self, filepath=None):
        """ Exports to SVMLight format.  If filepath is specified, returns
            writes to the file.  Else returns output, as a string.
        """
        def getKeys(data):
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

        def exportString(data):
            """ Internal function to export to string format
            """
            keys = getKeys(self.data)
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
        self.saveFilepath = ''
        self.data = []



###################################
##  Main program defined here    ##
###################################

def runMain():
    """ Main function called when run as standalone daemon
    """
    snapper = Snapper()
    snapper.load('datasets/bField.dataset')


if __name__ == '__main__':
    runMain()

