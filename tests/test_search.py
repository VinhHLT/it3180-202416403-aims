import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category

class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        items = [DigitalVideoDisc("Lion King", "Animation", "Dir", 90, 19.95)]
        self.assertEqual(len(search_by_category(items, "animation")), 1)
