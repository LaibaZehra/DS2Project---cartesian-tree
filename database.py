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
        self.keys = []
        self.index = CartesianTree(self.keys,0,len(self.keys)-1)       
        


    def read(self, csvfile: str) -> None:
        '''Read and store records from the given CSV file.

        Parameters:
        - self: mandatory reference to this object
        - csvfile: path to a csv file that contains the records

        Returns:
        None
        '''
        # opening and reading csv file
        input_lines = open(csvfile,encoding='utf-8').readlines()
        self.header = None
        self.records = {}
        reader = csv.reader(input_lines)
        for i,row in enumerate(reader):
            if i == 0:
                self.header = row
                continue
            self.records[i] = row[1:]
            self.keys.append(i)
        return self.keys
    def create_dictionary(self, attribute: str) -> None:
        '''Construct an index using values of the specified attribute.

        attribute must be one of the column headers from the CSV file from which
        the records were read. all values for attribute must be unique.

        Any existing index is lost and a new one is constructed. The constructed
        index is empty if no records are currently stored.

        The index stores (key, value) pairs where the keys are the values of
        attribute. The value is the location, e.g. index, of the corresponding
        record. Note that the value is not the record itself.

        Parameters:
        - self: mandatory reference to this object
        - attribute: the attribute whose values are to be the keys in the index

        Returns:
        None
        '''
        #assigning keys to values according to the attribute we're using to act as key
        
        # keydictionary = {"Book Code" : 0, "Title" : 1, "Category" : 2,"Price" : 3, "Pages" : 4}
        # key = keydictionary[attribute]
        #then we use those keys to add the records in the skiplist
        # self.index.reset()                             #here we empty the index before reinserting values or else it repeats
        # for i in range(len(self.records)):             #in this loop we insert in our skiplist the records we have from the book file
        #     self.index.insert((self.records[i][key], i))
        
    def select(self, key: str) -> Optional[List[str]]:
        '''Return the record corresponding to the given key, None in case of
        error.

        The index is used to find the record. An error occurs if the index is
        not yet created or the key in invalid. This is indicated by a return of
        None.

        Parameters:
        - self: mandatory reference to this object
        - key: the key whose corresponding value is sought

        Returns:
        The record corresponding to key, None in case of error.
        '''
        val = self.index.find(key)                       #we use our skiplist find function to find the key
        if val != None:                                  #if the function does not return none, we return the value that is found from the skiplist of records
            return self.records[val]
        

    def select_range(self, start: str, end: str) -> Optional[List[List[str]]]:
        '''Returns the records corresponding to the keys in the range
        [start,end] inclusive, None in case of error.

        An error occurs if no index has been created, start or end is not a valid
        key in the index, or start is not less than end.

        Parameters:
        - self: mandatory reference to this object
        - start: the starting key value in the range of keys
        - end: the ending key value in the range of keys

        Returns:
        The records in the order of the keys in the range [start,end], None in
        case of error.
        '''

        #if self.index.is_empty(): return None       
        result = self.index.find_range(start,end)     #calling find_range function to find the values between start and end range keys
        lst =[]
        for i in result:
            lst.append(self.records[i])               #when key values are returned, appending the values from records by keeping those returned values as indexes
        return lst

    def delete(self, key: str) -> Optional[List[str]]:
        '''Deletes the record corresponding to key from the table and the index.
        Returns the deleted record, None in case of error.

        An error occurs if no index has been created, or key does not exist in
        it.

        Parameters:
        - self: mandatory reference to this object
        - from: the starting key value in the range of keys
        - to: the ending key value in the range of keys

        Returns:
        The deleted record,  None in case of error.
        '''
       
        record = self.index.remove(key)           #delete function call
        return self.records[record]               #returns deleted record
    

data = Table()
data.read('data/books.csv')