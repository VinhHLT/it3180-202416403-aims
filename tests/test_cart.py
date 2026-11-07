import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Cat", "Dir", 90, 10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Cat", "Dir", 90, 10.0)))

    def test_sort_cart(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("B", "Cat", "Dir", 90, 10.0))
        cart.add_dvd(DigitalVideoDisc("A", "Cat", "Dir", 90, 20.0))
        self.assertEqual([d.title for d in cart.sort_by_title()], ["A", "B"])
        self.assertEqual([d.cost for d in cart.sort_by_cost()], [20.0, 10.0])

    def test_sort_cart(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("B", "Cat", "Dir", 90, 10.0))
        cart.add_dvd(DigitalVideoDisc("A", "Cat", "Dir", 90, 20.0))
        self.assertEqual([d.title for d in cart.sort_by_title()], ["A", "B"])
        self.assertEqual([d.cost for d in cart.sort_by_cost()], [20.0, 10.0])
