# noinspection PyUnresolvedReferences
import unittest
# noinspection PyUnresolvedReferences
from utils import getParams
# noinspection PyUnresolvedReferences
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='financial_management').get_log()


class FoodCoupons(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
         HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_orderlist(self):
        path = getParams.get_url('financial_management', 'orderlist')
        params = getParams.get_params('financial_management', 'orderlist')
        resp_c = getParams.get_resp_params('financial_management', 'orderlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderlist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_createDownTask(self):
        path = getParams.get_url('financial_management', 'createDownTask')
        params = getParams.get_params('financial_management', 'createDownTask')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_temparlist(self):
        path = getParams.get_url('financial_management', 'temparlist')
        params = getParams.get_params('financial_management', 'temparlist')
        resp_c = getParams.get_resp_params('financial_management', 'temparlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'temparlist', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_chargelist(self):
        path = getParams.get_url('financial_management', 'chargelist')
        params = getParams.get_params('financial_management', 'chargelist')
        resp_c = getParams.get_resp_params('financial_management', 'chargelist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'chargelist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_sysdiction1(self):
        path = getParams.get_url('financial_management', 'sysdiction1')
        params = getParams.get_params('financial_management', 'sysdiction1')
        resp_c = getParams.get_resp_params('financial_management', 'sysdiction1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'sysdiction1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test06_sysdiction2(self):
        path = getParams.get_url('financial_management', 'sysdiction2')
        params = getParams.get_params('financial_management', 'sysdiction2')
        resp_c = getParams.get_resp_params('financial_management', 'sysdiction2', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'sysdiction2', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_sysdiction3(self):
        path = getParams.get_url('financial_management', 'sysdiction3')
        params = getParams.get_params('financial_management', 'sysdiction3')
        resp_c = getParams.get_resp_params('financial_management', 'sysdiction3', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'sysdiction3', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test08_orderInput(self):
        path = getParams.get_url('financial_management', 'orderInput')
        params = getParams.get_params('financial_management', 'orderInput')
        resp_c = getParams.get_resp_params('financial_management', 'orderInput', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderInput', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])