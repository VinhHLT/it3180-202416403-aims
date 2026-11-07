import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Cat", "Dir", 90, 10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Cat", "Dir", 90, 10.0)))
