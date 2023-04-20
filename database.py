from typing import List, Optional
from Cartesiantree import CartesianTree
import csv

class Table(object):
    '''A table that stores records and allows creation of an index on the
    records according to the values of a specified attribute. The index is used
    to efficiently retrieve records using key values. The index can be
    re-initialized in run-time using a different attribute.
    '''
    
    def __init__(self) -> None:
        '''Initialize this table with an empty index.

        The index is initialized with an empty skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        None
        '''
        self.records={}
        self.keys = []
        self.index = CartesianTree(self.keys,0,len(self.keys)-1,self.records)       
        


    def read(self, csvfile: str, key : str ) -> None:
        '''Read and store records from the given CSV file.

        Parameters:
        - self: mandatory reference to this object
        - csvfile: path to a csv file that contains the records

        Returns:
        None
        '''
        # opening and reading csv file
        choice = {'serial' : 0, 'pages' : 4}
        key1 = choice[key]
        input_lines = open(csvfile,encoding='utf-8').readlines()
        self.header = None
        reader = csv.reader(input_lines)
        for i,row in enumerate(reader):
            if i == 0:
                self.header = row
                continue
            if key1 == 0:
                self.records[row[0]] = row[1:]
                self.keys.append(row[0])
            elif key1 == 4:
                self.records[int(row[4])] = row[:4]
                self.keys.append(int(row[4]))
        print(self.keys)
        return self.records

# data = Table()
# value=data.read('data/books.csv','serial')
# for i in value:

# print(value)