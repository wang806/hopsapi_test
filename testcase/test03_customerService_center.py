import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='customerService_center').get_log()


class FoodCoupons(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getContentList(self):
        path = getParams.get_url('customerService_center', 'getContentList')
        params = getParams.get_params('customerService_center', 'getContentList')
        resp_c = getParams.get_resp_params('customerService_center', 'getContentList', 'code')
        resp_m = getParams.get_resp_params('customerService_center', 'getContentList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
