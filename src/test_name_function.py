import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """name_function.pyをテストする"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('test', 'taro')
        self.assertEqual(formatted_name,'Test Taro')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('test' , 'taro', 'hanako')
        self.assertEqual(formatted_name, 'Test Hanako Taro')

if __name__ == '__main__':
    unittest.main()