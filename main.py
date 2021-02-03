import numpy as np

# Question
# Create a dynamic array subclass which also has the following basic methods:
# a. add(val) which adds an element to the end
# b. del() which removes the last element of the array

# the first thing we should do is create an array using numpy
# this is the array we'll be using to test out our function
# i am using numpy and its append and del methods
array1 = np.array([1, 2, 3])
print(array1)

array2 = np.array([])
array3 = np.array([])


# this method adds an element to the end of the array using the numpy function append, which automatically creates a
# new array with the new element as the last element
# this is done because the size of an array is immutable, so this is a way around that
def add_end_element(original_array):
    value = int(input("Enter the element you want to add to the end of the array: "))
    # use numpy append method to add an element
    new_array = np.append(original_array, value)

    # both the arrays are printed so the difference can be seen
    # , is used instead of + as plus is a numpy function and gives an error
    print("Original array: ", original_array)
    print("New array, with added element: ", new_array)
    print(" ")


# this method removes the element at the end of the array using the numpy function delete, which automatically creates
# a new array without the last element
# this is done because the size of an array is immutable, so this is a way around that
def remove_end_element(original_array):
    new_array = np.delete(original_array, -1)

    # both the arrays are printed so the difference can be seen
    print("Original array: ", original_array)
    print("New array, with last element deleted: ", new_array)


# running the functions
add_end_element(array1)
remove_end_element(array1)

# how to add multiple with user input: value only takes one item at a time and using the function doesn't require
# user prompt
