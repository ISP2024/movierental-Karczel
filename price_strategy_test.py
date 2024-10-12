import unittest
from price_strategy import RegularPrice, ChildrensPrice, NewRelease


class PriceStrategyTest(unittest.TestCase):

    def test_regular_price_singleton(self):
        instance1 = RegularPrice()
        instance2 = RegularPrice()
        self.assertIs(instance1, instance2, "RegularPrice instances are not the same singleton instance.")

    def test_childrens_price_singleton(self):
        instance1 = ChildrensPrice()
        instance2 = ChildrensPrice()
        self.assertIs(instance1, instance2, "ChildrensPrice instances are not the same singleton instance.")

    def test_new_release_singleton(self):
        instance1 = NewRelease()
        instance2 = NewRelease()
        self.assertIs(instance1, instance2, "NewRelease instances are not the same singleton instance.")

    def test_subclass_instances_are_different(self):
        regular_price = RegularPrice()
        childrens_price = ChildrensPrice()
        new_release = NewRelease()

        self.assertIsNot(regular_price, childrens_price,
                         "RegularPrice and ChildrensPrice should not be the same instance.")
        self.assertIsNot(regular_price, new_release, "RegularPrice and NewRelease should not be the same instance.")
        self.assertIsNot(childrens_price, new_release, "ChildrensPrice and NewRelease should not be the same instance.")


if __name__ == '__main__':
    unittest.main()
