import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
