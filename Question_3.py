import numpy as np
import sys

class Array:
    """ 
    class array 
    ===========
    instance attribute : A list
    """

    def __init__(self, array=[]):
        self.array = np.array(array)
    
    def _len(self):
        """return the length of the array"""
        if self.array is not None:
            return len(self.array)
        else:
            print(">>> List is None", file=sys.stderr)
            return None
    
    def _get(self, value):
        """get the element at index i"""
        if self.array is not None:
            len_array = self._len()
            if len_array == 0:
                return False
            elif value < len_array and value >= 0:
                return int(self.array[value])
        else:
            print(">>> List is None", file=sys.stderr)
            return None

    def _set(self, value, idx):
        """replace value at an index"""
        if self.array is None:
            """return false when the array is None"""
            print(">>> List is None", file=sys.stderr)
            return None
        len_array = self._len()
        if idx is not int:
            """when the index is not an integer"""
            raise TypeError(f"[idx] : {idx} should be an integer")
        if value is not int:
            """ when the user enter a value that is not an integer"""
            raise TypeError(f"[value] : {value} should be an integer")
        if idx < len_array and idx >= 0:
            """when the user what to modify at an index"""
            self.array[idx] = value
        else:
            """index error. Raise ValueError"""
            raise ValueError(f"[index]: {idx} out of range")
    
    def __str__(self):
        lst = self.array.tolist()
        return f"{lst}"



class DynamicArray(Array):

    def copy(self, array):
        """ copy element of an array to another"""
        if self.array is not None:
            for element in self.array:
                array.append(element) 

    def add(self, value):
        """ Add an new element at the end of the list""" 
        if self.array is not None:
            # use numpy append method to add an element
            self.array = np.append(self.array, value)
            print(">>> A new element was succesfullly added")
        else:
            print(f">>> [value] : {value} was not added in the list", file=sys.stderr)


    def remove(self):
        """remove the last element of the array"""
        if self.array is not None and self._len() > 0:
            self.array = np.delete(self.array, -1)
            print(">>>The last element was succesfully deleted")
        else:
            print(">>>The last element was not deleted", file=sys.stderr)

    def contains(self, value):
        """ check if the array contains the value as element"""
        if self.array is not None:
            for element in self.array:
                if element == value:
                    return True
            print(f">>>[vaue] : {value} not in the list", file=sys.stderr)
            return False
        else:
            print(">>>List is empty")
            return False

    def reverse(self):
        """reverse the array"""
        if self.array is not None and self._len() >= 0:
            new_array = np.array([])
            size = self._len() - 1
            while(size >= 0):
                new_array = np.append(new_array, self.array[size])
                size -= 1
            return new_array.tolist()
        else:
            print(">>> List is None", file=sys.stderr)
    
    def insert(self, value, idx):
        """insert value at a given index"""
        len_array = self._len()
        if self.array is not None and idx + 1 <= len_array and idx >= 0:
            tmp = []
            self.copy(tmp)
            self.array = np.array([])
            inserted = False
            i = 0
            for numb in range(0, len_array):
                if inserted == True:
                    #decrement the value of index after after inserting the value
                    numb -= 1
                if numb == idx and i == 0:
                    self.add(value)
                    inserted = True
                    i = 1
                else:
                    self.add(tmp[numb])
            #insert the last element
            self.add(tmp[-1])
        else:
            print(">>> Could not insert a value to the list", file=sys.stderr)


    
        