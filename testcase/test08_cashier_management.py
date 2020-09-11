import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
import re
logger = Log(logger='cashier_management').get_log()


class CashierManagement(unittest.TestCase):
    businessId = ''
    cashierID = ''
    pattern = re.compile(r'\d\d\d\d\d\d')

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
        CashierManagement.businessId = response['data']['items'][0]['businessId']
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getBusinessInfo(self):
        path = getParams.get_url('cashier_management', 'getBusinessInfo')
        params = getParams.get_params('cashier_management', 'getBusinessInfo')
        params = re.sub(self.pattern, CashierManagement.businessId, params)
        resp_c = getParams.get_resp_params('cashier_management', 'getBusinessInfo', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'getBusinessInfo', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_updateBusinessInfo(self):
        path = getParams.get_url('cashier_management', 'updateBusiness')
        params = getParams.get_params('cashier_management', 'updateBusiness')
        params['businessId'] = CashierManagement.businessId
        resp_c = getParams.get_resp_params('cashier_management', 'updateBusiness', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'updateBusiness', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_updateBusinessStatus(self):
        path = getParams.get_url('cashier_management', 'updateBusinnessStatus')
        params = getParams.get_params('cashier_management', 'updateBusinnessStatus')
        params = re.sub(self.pattern, CashierManagement.businessId, params)
        resp_c = getParams.get_resp_params('cashier_management', 'updateBusinnessStatus', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'updateBusinnessStatus', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_resetBusinessPwd(self):
        path = getParams.get_url('cashier_management', 'resetBusinessPwd')
        params = getParams.get_params('cashier_management', 'resetBusinessPwd')
        params = re.sub(self.pattern, CashierManagement.businessId, params)
        resp_c = getParams.get_resp_params('cashier_management', 'resetBusinessPwd', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'resetBusinessPwd', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test06_getCashierList(self):
        path = getParams.get_url('cashier_management', 'getCashierList')
        params = getParams.get_params('cashier_management', 'getCashierList')
        resp_c = getParams.get_resp_params('cashier_management', 'getCashierList', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'getCashierList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        CashierManagement.cashierID = response['data']['items'][0]['account']
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_viewCashier(self):
        path = getParams.get_url('cashier_management', 'viewCashier')
        params = getParams.get_params('cashier_management', 'viewCashier')
        params = re.sub(self.pattern, CashierManagement.businessId, params)
        resp_c = getParams.get_resp_params('cashier_management', 'getCashierList', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'getCashierList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

