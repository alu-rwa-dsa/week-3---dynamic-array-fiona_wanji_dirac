# import ctypes


# Question
# Create a dynamic array subclass which also has the following basic methods:
# a. add(val) which adds an element to the end
# b. del() which removes the last element of the array
#
# the first thing we need to do is create a class and its init
# the init should add an array, which means it should have a
# fixed number of elements

class DynamicArraySubClass:

    def __init__(self, element):
        # default length will be zero so we can have a function
        # to count the number of elements in an array
        self.elements = []
        self.length = 0

        # function will cover


def array_length(arrayName):
    # count the name in the array specified
    length = len(arrayName)


array1 = DynamicArraySubClass([1, 2, 3])

print(array_length(array1.elements))

