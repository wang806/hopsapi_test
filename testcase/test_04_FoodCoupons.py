import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='FoodCoupons').get_log()


class FoodCoupons(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getFoodCouponsList(self):
        path = getParams.get_url('food_coupons', 'getFoodCouponsList')
        params = getParams.get_params('food_coupons', 'getFoodCouponsList')
        resp_c = getParams.get_resp_params('food_coupons', 'getFoodCouponsList', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'getFoodCouponsList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getFoodCouponsInfo(self):
        params = getParams.get_params('food_coupons', 'foodCouponsInfo')
        path = getParams.get_url('food_coupons', 'foodCouponsInfo')
        resp_c = getParams.get_resp_params('food_coupons', 'foodCouponsInfo', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'foodCouponsInfo', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_foodCouponsEnable(self):
        path = getParams.get_url('food_coupons', 'foodCouponsEnable')
        params = getParams.get_params('food_coupons', 'foodCouponsEnable')
        resp_c = getParams.get_resp_params('food_coupons', 'foodCouponsEnable', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'foodCouponsEnable', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_businessMessage(self):
        path = getParams.get_url('food_coupons', 'businessMessage')
        params = getParams.get_params('food_coupons', 'businessMessage')
        resp_c = getParams.get_resp_params('food_coupons', 'businessMessage', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'businessMessage', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_foodCouponsUpdate(self):
        path = getParams.get_url('food_coupons', 'foodCouponsUpdate')
        params = getParams.get_params('food_coupons', 'foodCouponsUpdate')
        resp_c = getParams.get_resp_params('food_coupons', 'foodCouponsUpdate', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'foodCouponsUpdate', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test06_presentCoupons(self):
        path = getParams.get_url('food_coupons', 'presentCoupons')
        params = getParams.get_params('food_coupons', 'presentCoupons')
        resp_c = getParams.get_resp_params('food_coupons', 'presentCoupons', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'presentCoupons', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_foodCouponsQuantity(self):
        path = getParams.get_url('food_coupons', 'foodCouponsQuantity')
        params = getParams.get_params('food_coupons', 'foodCouponsQuantity')
        resp_c = getParams.get_resp_params('food_coupons', 'foodCouponsQuantity', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'foodCouponsQuantity', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test08_getCouponsMarketings(self):
        path = getParams.get_url('food_coupons', 'getCouponsMarketings')
        params = getParams.get_params('food_coupons', 'getCouponsMarketings')
        resp_c = getParams.get_resp_params('food_coupons', 'getCouponsMarketings', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'getCouponsMarketings', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test09_marketingEnable(self):
        path = getParams.get_url('food_coupons', 'marketingEnable')
        params = getParams.get_params('food_coupons', 'marketingEnable')
        resp_c = getParams.get_resp_params('food_coupons', 'marketingEnable', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'marketingEnable', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test10_friendHelpInfo(self):
        path = getParams.get_url('food_coupons', 'friendHelpInfo')
        params = getParams.get_params('food_coupons', 'friendHelpInfo')
        resp_c = getParams.get_resp_params('food_coupons', 'friendHelpInfo', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'friendHelpInfo', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test11_friendHelpEdit(self):
        path = getParams.get_url('food_coupons', 'friendHelpEdit')
        params = getParams.get_params('food_coupons', 'friendHelpEdit')
        resp_c = getParams.get_resp_params('food_coupons', 'friendHelpEdit', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'friendHelpEdit', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test12_presentCouponsList(self):
        path = getParams.get_url('food_coupons', 'presentCouponsList')
        params = getParams.get_params('food_coupons', 'presentCouponsList')
        resp_c = getParams.get_resp_params('food_coupons', 'presentCouponsList', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'presentCouponsList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test13_getCouponsList(self):
        path = getParams.get_url('food_coupons', 'getCouponsList')
        params = getParams.get_params('food_coupons', 'getCouponsList')
        resp_c = getParams.get_resp_params('food_coupons', 'getCouponsList', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'getCouponsList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test14_setPresentCoupons(self):
        path = getParams.get_url('food_coupons', 'setPresentCoupons')
        params = getParams.get_params('food_coupons', 'setPresentCoupons')
        resp_c = getParams.get_resp_params('food_coupons', 'setPresentCoupons', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'setPresentCoupons', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test15_foodCouponsSort(self):
        path = getParams.get_url('food_coupons', 'foodCouponsSort')
        params = getParams.get_params('food_coupons', 'foodCouponsSort')
        resp_c = getParams.get_resp_params('food_coupons', 'foodCouponsSort', 'code')
        resp_m = getParams.get_resp_params('food_coupons', 'foodCouponsSort', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test16_exportFile(self):
        path = getParams.get_url('food_coupons', 'exportFile')
        params = getParams.get_params('food_coupons', 'exportFile')
        resp_c = getParams.get_resp_params('food_coupons', 'exportFile', 'code')
        response = HttpUtil().do_download_file(path, params)
        # print(response.status_code)
        self.assertEqual(resp_c, response.status_code)

    # def test04_valuePutTest(self):
    #     path = getParams.get_url('food_coupons', 'getFoodCouponsList')
    #     params = getParams.get_params('food_coupons', 'getFoodCouponsList')
    #     print(params)
    #     ct = int(time.time())
    #     print(ct)
    #     print(ct*1000)
    #     ct = str((ct+60)*1000)
    #     params['startTime'] = ct
    #     print(params)
    #     # resp_c = getParams.get_resp_params('food_coupons', 'getFoodCouponsList', 'code')
    #     # resp_m = getParams.get_resp_params('food_coupons', 'getFoodCouponsList', 'msg')
    #     # response = HttpUtil().do_post(path, params)
    #     # self.assertEqual(resp_c, response['code'])
    #     # self.assertEqual(resp_m, response['msg'])
