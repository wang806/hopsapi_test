import unittest
from utils.logger import Log
logger = Log(logger='FoodCoupons').get_log()


class FoodCoupons(unittest.TestCase):

    a = 0
    @classmethod
    def setUpClass(cls) -> None:
        print('setup')
        # cls.a = 6

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown')

    def test01_getFoodCouponsList(self):
        self.a = 1
        print(self.a)

    def test02_getFoodCouponsInfo(self):
        # self.a = 2
        FoodCoupons.a = 2
        print(self.a)

    def test03_foodCouponsEnable(self):
        print(self.a)

