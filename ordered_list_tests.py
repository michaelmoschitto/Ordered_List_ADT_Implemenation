import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_isEmpty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_add(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(34)
        self.assertEqual(t_list.python_list(), [10,34])
        t_list.add(12)
        t_list.add(7)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [7,10,12,34,50])

    def test_remove(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(34)
        self.assertEqual(t_list.python_list(), [10,34])
        t_list.add(12)
        t_list.add(7)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [7,10,12,34,50])
        self.assertTrue(t_list.remove(7))
        print(t_list.python_list())
        self.assertTrue(t_list.remove(10))
        print(t_list.python_list())

        self.assertTrue(t_list.remove(34))
        print(t_list.python_list())

        self.assertEqual(t_list.python_list(), [12,50])
        self.assertTrue(t_list.remove(12))
        print(t_list.python_list())

        self.assertFalse(t_list.remove(15))
        print(t_list.python_list())

        self.assertTrue(t_list.remove(50))
        print(t_list.python_list())

        self.assertTrue(t_list.is_empty())
        with self.assertRaises(IndexError):
            t_list.remove(15)
            

    def test_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)

        self.assertEqual(t_list.index(10),0)
        self.assertEqual(t_list.index(34),1)
        self.assertEqual(t_list.index(40),2)
        self.assertEqual(t_list.index(50),None)

    def test_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)
        self.assertEqual(t_list.pop(0),10)
        t_list.add(10)
        self.assertEqual(t_list.pop(1),34)
        t_list.add(34)
        self.assertEqual(t_list.pop(2),40)
        t_list.add(40)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        with self.assertRaises(IndexError):
            t_list.pop(10)

    def test_search(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(34))
        self.assertTrue(t_list.search(40))
        self.assertFalse(t_list.search(60))

    def test_pythonList(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)
        self.assertEqual(t_list.python_list(), [10,34,40])

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)
        self.assertEqual(t_list.size(), 3)

    def test_reverse(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        t_list.add(34)
        t_list.add(40)
        self.assertEqual(t_list.python_list_reversed(), [40,34,10])

if __name__ == '__main__':
    unittest.main()
