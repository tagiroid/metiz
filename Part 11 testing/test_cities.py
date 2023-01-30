import unittest

from city_functions import get_formatted_cities


class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = get_formatted_cities('Chile', 'Santiago')
        self.assertEqual(formatted, 'Santiago, Chile')
    def test_city_country_population(self):
        formatted = get_formatted_cities('Chile', 'Santiago', '5 000 000')
        self.assertEqual(formatted, "Santiago, Chile - Population 5 000 000")
if __name__ == '__main__':
    unittest.main()