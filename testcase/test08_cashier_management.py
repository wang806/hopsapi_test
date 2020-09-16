import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
import re
logger = Log(logger='cashier_management').get_log()


class CashierManagement(unittest.TestCase):
    businessId = ''
    cashierID = ''
    terminalNo = ''
    pattern = re.compile(r'\d\d\d\d\d\d')
    patternCashier = re.compile(r'\d\d\d\d\d\d\d\d')

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

    # @unittest.skip
    def test03_updateBusinessInfo(self):
        path = getParams.get_url('cashier_management', 'updateBusiness')
        params = getParams.get_params('cashier_management', 'updateBusiness')
        params['businessId'] = CashierManagement.businessId
        resp_c = getParams.get_resp_params('cashier_management', 'updateBusiness', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'updateBusiness', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    # @unittest.skip
    def test04_updateBusinessStatus(self):
        path = getParams.get_url('cashier_management', 'updateBusinnessStatus')
        params = getParams.get_params('cashier_management', 'updateBusinnessStatus')
        params = re.sub(self.pattern, CashierManagement.businessId, params)
        resp_c = getParams.get_resp_params('cashier_management', 'updateBusinnessStatus', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'updateBusinnessStatus', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    # @unittest.skip
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
        params = re.sub(self.pattern, CashierManagement.cashierID, params)
        resp_c = getParams.get_resp_params('cashier_management', 'getCashierList', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'getCashierList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test08_updateCashier(self):
        path = getParams.get_url('cashier_management', 'updateCashier')
        params = getParams.get_params('cashier_management', 'updateCashier')
        params['account'] = CashierManagement.cashierID
        resp_c = getParams.get_resp_params('cashier_management', 'updateCashier', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'updateCashier', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test09_disableCashier(self):
        path = getParams.get_url('cashier_management', 'disableCashier')
        params = getParams.get_params('cashier_management', 'disableCashier')
        params = re.sub(self.patternCashier, CashierManagement.cashierID, params)
        resp_c = getParams.get_resp_params('cashier_management', 'disableCashier', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'disableCashier', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test10_enableCashier(self):
        path = getParams.get_url('cashier_management', 'enableCashier')
        params = getParams.get_params('cashier_management', 'enableCashier')
        params = re.sub(self.patternCashier, CashierManagement.cashierID, params)
        resp_c = getParams.get_resp_params('cashier_management', 'enableCashier', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'enableCashier', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test11_resetCashierPWD(self):
        path = getParams.get_url('cashier_management', 'resetCashierPWD')
        params = getParams.get_params('cashier_management', 'resetCashierPWD')
        params = re.sub(self.patternCashier, CashierManagement.cashierID, params)
        resp_c = getParams.get_resp_params('cashier_management', 'resetCashierPWD', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'resetCashierPWD', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test12_terminalList(self):
        path = getParams.get_url('cashier_management', 'terminalList')
        params = getParams.get_params('cashier_management', 'terminalList')
        resp_c = getParams.get_resp_params('cashier_management', 'terminalList', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'terminalList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        CashierManagement.terminalNo = response['data']['items'][0]['terminalNo']
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test13_viewTerminal(self):
        path = getParams.get_url('cashier_management', 'viewTerminal')
        params = getParams.get_params('cashier_management', 'viewTerminal')
        params = re.sub(self.patternCashier, CashierManagement.terminalNo, params)
        resp_c = getParams.get_resp_params('cashier_management', 'viewTerminal', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'viewTerminal', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test14_disableTerminal(self):
        path = getParams.get_url('cashier_management', 'disableTerminal')
        params = getParams.get_params('cashier_management', 'disableTerminal')
        params = re.sub(self.patternCashier, CashierManagement.terminalNo, params)
        resp_c = getParams.get_resp_params('cashier_management', 'disableTerminal', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'disableTerminal', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test15_enableTerminal(self):
        path = getParams.get_url('cashier_management', 'enableTerminal')
        params = getParams.get_params('cashier_management', 'enableTerminal')
        params = re.sub(self.patternCashier, CashierManagement.terminalNo, params)
        resp_c = getParams.get_resp_params('cashier_management', 'enableTerminal', 'code')
        resp_m = getParams.get_resp_params('cashier_management', 'enableTerminal', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
