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
