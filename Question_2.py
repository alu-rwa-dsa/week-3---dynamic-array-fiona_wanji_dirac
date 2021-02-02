import numpy as np

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
        print(">>> List is None")
        return None
    
    def _get(self, value):
        """get the element at index i"""
        if self.array is not None:
            len_array = self._len()
            if len_array == 0:
                return False
            elif value < len_array and value >= 0:
                return int(self.array[value])
        print(">>> List is None")
        return None

    def _set(self, value, idx):
        """replace value at an index"""
        if self.array is None:
            """return false when the array is None"""
            return False
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


# Question
# Create a dynamic array subclass which also has the following basic methods:
# a. add(val) which adds an element to the end
# b. del() which removes the last element of the array

# the first thing we should do is create an array using numpy
# this is the array we'll be using to test out our function
# i am using numpy and its append and del methods

class DynamicArray(Array):

# this method adds an element to the end of the array using the numpy function append, which automatically creates a
# new array with the new element as the last element
# this is done because the size of an array is immutable, so this is a way around that
    def add_end_element(self, value):
        """ Add an new element at the end of the list""" 
        if self.array is not None:
            # use numpy append method to add an element
            self.array = np.append(self.array, value)
            print(">>> A new element was succesfullly added")
        else:
            print(f">>> [value] : {value} was not added in the list")


# this method removes the element at the end of the array using the numpy function delete, which automatically creates
# a new array without the last element
# this is done because the size of an array is immutable, so this is a way around that
    def remove_end_element(self):
        if self.array is not None and self._len() > 0:
            self.array = np.delete(self.array, -1)
            print(">>>The last element was succesfully deleted")
        else:
            print(">>>The last element was not deleted")

