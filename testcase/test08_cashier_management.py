import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='cashier_management').get_log()


class CashierManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getBusinessList(self):
        path = getParams.get_url('cashier_management', 'getBusinessList')
        params = getParams.get_params('cashier_management', 'getBusinessList')
        resp_c = getParams.get_resp_params('cashier_management', 'getBusinessList', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'getBusinessList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getBusinessInfo(self):
        path = getParams.get_url('cashier_management', 'getBusinessInfo')
