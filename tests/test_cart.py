
    def test_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test", "Cat", "Dir", 90, 100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
