from Question_2 import Array
from Question_2 import DynamicArray


# running the functions
new_ar = DynamicArray()
new_ar.add_end_element(1)
print(new_ar._len())
print(new_ar._get(0))

new_ar.remove_end_element()
print(new_ar._len())

# remove elements in an empty array
new_ar.remove_end_element()
new_ar.remove_end_element()
