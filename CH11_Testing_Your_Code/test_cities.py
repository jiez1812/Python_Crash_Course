import unittest
from city_function import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_function.py'"""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        formatted_string = city_country('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does city, country, and population pass?"""
        formatted_string = city_country('santiago', 'chile', 5000000)

unittest.main()