import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='business_management').get_log()


class FoodCoupons(unittest.TestCase):
    tradeNo = ''
    businessId = ''

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_daylistFloor(self):
        path = getParams.get_url('business_management', 'daylistFloor')
        params = getParams.get_params('business_management', 'daylistFloor')
        resp_c = getParams.get_resp_params('business_management', 'daylistFloor', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daylistFloor', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test02_daylistType(self):
        self.path = getParams.get_url('business_management', 'daylistType')
        params = getParams.get_params('business_management', 'daylistType')
        resp_c = getParams.get_resp_params('business_management', 'daylistType', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daylistType', 'msg')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test03_daylistUserId(self):
        path = getParams.get_url('business_management', 'daylistUserId')
        params = getParams.get_params('business_management', 'daylistUserId')
        resp_c = getParams.get_resp_params('business_management', 'daylistUserId', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daylistUserId', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test04_daylistAreatype(self):
        self.path = getParams.get_url('business_management', 'daylistAreatype')
        params = getParams.get_params('business_management', 'daylistAreatype')
        resp_c = getParams.get_resp_params('business_management', 'daylistAreatype', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daylistAreatype', 'msg')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test05_dayList(self):
        path = getParams.get_url('business_management', 'dayList')
        params = getParams.get_params('business_management', 'dayList')
        resp_c = getParams.get_resp_params('business_management', 'dayList', 'code')
        resp_m = getParams.get_resp_params('business_management', 'dayList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        FoodCoupons.tradeNo = response['data']['items'][0]['tradeNo']
        FoodCoupons.businessId = response['data']['items'][0]['businessId']
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test06_dayDetails(self):
        path = getParams.get_url('business_management', 'dayDetails')
        path = path + '/' + str(FoodCoupons.tradeNo) + '/' + str(FoodCoupons.businessId)
        resp_c = getParams.get_resp_params('business_management', 'dayDetails', 'code')
        resp_m = getParams.get_resp_params('business_management', 'dayDetails', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test07_daydetailsOperation(self):
        path = getParams.get_url('business_management', 'daydetailsOperation')
        path = path + '/' + str(FoodCoupons.tradeNo)
        resp_c = getParams.get_resp_params('business_management', 'daydetailsOperation', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daydetailsOperation', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test08_daydetailsBusiness(self):
        path = getParams.get_url('business_management', 'daydetailsBusiness')
        path = path + '/'+ str(FoodCoupons.businessId)
        resp_c = getParams.get_resp_params('business_management', 'daydetailsBusiness', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daydetailsBusiness', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test09_daySubmit(self):
        self.path = getParams.get_url('business_management', 'daySubmit')
        params = getParams.get_params('business_management', 'daySubmit')
        resp_c = getParams.get_resp_params('business_management', 'daySubmit', 'code')
        resp_m = getParams.get_resp_params('business_management', 'daySubmit', 'msg')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)

    def test10_dayReport(self):
        path = getParams.get_url('business_management', 'dayReport')
        params = getParams.get_params('business_management', 'dayReport')
        resp_c = getParams.get_resp_params('business_management', 'dayReport', 'code')
        resp_m = getParams.get_resp_params('business_management', 'dayReport', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
        print(resp_c, resp_m)