# Lab 1 Test Cases

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError): # used to check for exception
            max_list_iter(tlist)

        test_list = [1, 2, 3]
        self.assertEqual(max_list_iter(test_list), 3) # check for correct return
        self.assertEqual(max_list_iter([]), None) # check for empty list


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1]) # check for correct return
        self.assertEqual(reverse_rec([3, 1, 2]), [2, 1, 3]) # check non-ordered list
        self.assertEqual(reverse_rec([4, 1, 9, 0]), [0, 9, 1, 4]) # check longer non-ordered list
        self.assertEqual(reverse_rec([]), None) # check for empty list


    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(2, 3, 1, tlist)

        self.assertEqual(bin_search(2, 1, 4, []), None) # check for empty list

        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4) # target < mid
        self.assertEqual(bin_search(-1, low, high, list_val), None) # lower target not in list
        self.assertEqual(bin_search(9, low, high, list_val), 7) # target > mid
        self.assertEqual(bin_search(11, low, high, list_val), None) # higher target not in list


if __name__ == "__main__":
        unittest.main()

