import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated = get_formatted_name('janis', 'joplin')
        self.assertEqual(formated, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()