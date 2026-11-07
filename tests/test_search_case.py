import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearchCase(unittest.TestCase):
    def test_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", "Dir", 90, 19.95)]
        self.assertEqual(len(search_by_title(items, "lion")), 1)
