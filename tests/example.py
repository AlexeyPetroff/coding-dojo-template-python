import unittest
from src.program import Cart, get_price


class ExampleTest(unittest.TestCase):

    def test1_get_price(self):
        c = Cart()
        price = get_price('Part1')
        self.assertEqual(price, 8)

    def test2_if_cart_is_empty(self):
        c = Cart()
        self.assertEquals(c.count_all_items(), 0)

    def test3_add_to_cart(self):
        c = Cart()
        c.add_to_cart('Part1', 2)
        self.assertEquals(c.count_all_items(), 2)

    def test4_add_diff_books(self):
        c = Cart()
        c.add_to_cart('Part1',1)
        c.add_to_cart('Part2', 3)
        self.assertEquals(c.count_all_items(),4)

    def test5_get_price(self):
        c = Cart()
        c.add_to_cart('Part1', 1)
        self.assertEquals(c.count_price(), 8)

    def test6_get_price_for_two_same(self):
        c = Cart()
        c.add_to_cart('Part1', 2)
        self.assertEquals(c.count_price(), 16)

    def test7_get_price_for_two_different(self):
        c = Cart()
        c.add_to_cart('Part1', 1)
        c.add_to_cart('Part2', 1)
        self.assertEquals(c.count_price(), 15.2)

    def test8_get_price_for_p1_p1_p2(self):
        c = Cart()
        c.add_to_cart('Part1', 2)
        c.add_to_cart('Part2', 1)
        self.assertEquals(c.count_price(), 15.2+8)

if __name__ == '__main__':
    unittest.main()
