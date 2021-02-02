# we import the test file we want to test and the test modules we want
from Question_4 import *
import unittest


class TestAssociativeList(unittest.TestCase):

    # age = {"Lucy": 78}

    def test_adding_value(self):
        age = {"Lucy": 78}
        new_age = {}
        add_age(new_age, "Lucy", 78)
        assert new_age == age

    def test_remove_key(self):
        age = {"Lucy": 78}
        remove_age(age, "Lucy")
        assert len(age) == 0

    def test_modify_key(self):
        age = {"Lucy": 78}
        # modified_age = {}
        # modified_age =
        change_age(age, "Lucy", 90)
        # assert modified_age == {"Lucy" : 90}
        assert age == {"Lucy" : 90}
        # assert modified_age != age

    def test_look_up_key(self):
        age = {"Lucy": 78}
        person_age = lookup_age(age, "Lucy")
        assert person_age == 78
