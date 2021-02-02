import unittest
#import class

Array = __import__("Question_1").Array

print("==== Test case initializing empty list =====")
array_1 = Array()
print(array_1)
print("Expected value : []\n")

print("==== Test case initialization =======")
array_1 = Array([1, 2])
print(array_1)
print("Expected value : [1, 2]\n")

print("=== Test case _len function ====")
print(array_1._len())
print("Expected value : 2")

print("===Test case _get function =====")
print(array_1._get(1))
print("Expected value : 2")

class Test_class_1(unittest.TestCase):
    def test_new_instance(self):
        array_1 = Array()
        self.assertIsInstance(array_1, Array)
    
    def test_initialized_array(self):
        array_1  = Array([2, 3, 4])
        len_a = array_1._len()
        self.assertEqual(len_a, 3)
    
    def test(self):
        array_1 = Array([4, 6, 7])
        get_0 = array_1._get(0)
        self.assertEqual(get_0, 4)


if __name__ == "__main__":
    unittest.main()
