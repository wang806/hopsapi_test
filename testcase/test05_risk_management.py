# noinspection PyUnresolvedReferences
import unittest
# noinspection PyUnresolvedReferences
from utils import getParams
# noinspection PyUnresolvedReferences
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='risk_management').get_log()


class FoodCoupons(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
         HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass


    def test01_riskrult(self):
        path = getParams.get_url('risk_management', 'riskrult')
        params = getParams.get_params('risk_management', 'riskrult')
        resp_c = getParams.get_resp_params('risk_management', 'riskrult', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'riskrult', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getAssembly(self):
        path = getParams.get_url('risk_management', 'getAssembly')
        params = getParams.get_params('risk_management', 'getAssembly')
        resp_c = getParams.get_resp_params('risk_management', 'getAssembly', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'getAssembly', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_getUnits(self):
        path = getParams.get_url('risk_management', 'getUnits')
        params = getParams.get_params('risk_management', 'getUnits')
        resp_c = getParams.get_resp_params('risk_management', 'getUnits', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'getUnits', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_strategy(self):
        path = getParams.get_url('risk_management', 'strategy')
        params = getParams.get_params('risk_management', 'strategy')
        resp_c = getParams.get_resp_params('risk_management', 'strategy', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'strategy', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_ruleList(self):
        path = getParams.get_url('risk_management', 'ruleList')
        params = getParams.get_params('risk_management', 'ruleList')
        resp_c = getParams.get_resp_params('risk_management', 'ruleList', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'ruleList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test06_getAssembly2(self):
        path = getParams.get_url('risk_management', 'getAssembly2')
        params = getParams.get_params('risk_management', 'getAssembly2')
        resp_c = getParams.get_resp_params('risk_management', 'getAssembly2', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'getAssembly2', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_getAssembly3(self):
        path = getParams.get_url('risk_management', 'getAssembly3')
        params = getParams.get_params('risk_management', 'getAssembly3')
        resp_c = getParams.get_resp_params('risk_management', 'getAssembly3', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'getAssembly3', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test08_Query(self):
        path = getParams.get_url('risk_management', 'Query')
        params = getParams.get_params('risk_management', 'Query')
        resp_c = getParams.get_resp_params('risk_management', 'Query', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'Query', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test09_Insert(self):
        path = getParams.get_url('risk_management', 'Insert')
        params = getParams.get_params('risk_management', 'Insert')
        resp_c = getParams.get_resp_params('risk_management', 'Insert', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'Insert', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test10_vigilant(self):
        path = getParams.get_url('risk_management', 'vigilant')
        params = getParams.get_params('risk_management', 'vigilant')
        resp_c = getParams.get_resp_params('risk_management', 'vigilant', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'vigilant', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test11_abnormal(self):
        path = getParams.get_url('risk_management', 'abnormal')
        params = getParams.get_params('risk_management', 'abnormal')
        resp_c = getParams.get_resp_params('risk_management', 'abnormal', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'abnormal', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test12_black(self):
        path = getParams.get_url('risk_management', 'black')
        params = getParams.get_params('risk_management', 'black')
        resp_c = getParams.get_resp_params('risk_management', 'black', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'black', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test13_batchTransfe(self):
        path = getParams.get_url('risk_management', 'batchTransfe')
        params = getParams.get_params('risk_management', 'batchTransfe')
        resp_c = getParams.get_resp_params('risk_management', 'batchTransfe', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'batchTransfe', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test14_Delete(self):
        path = getParams.get_url('risk_management', 'Delete')
        params = getParams.get_params('risk_management', 'Delete')
        resp_c = getParams.get_resp_params('risk_management', 'Delete', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'Delete', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test15_Delete2(self):
        path = getParams.get_url('risk_management', 'Delete2')
        params = getParams.get_params('risk_management', 'Delete2')
        resp_c = getParams.get_resp_params('risk_management', 'Delete2', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'Delete2', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test16_Delete3(self):
        path = getParams.get_url('risk_management', 'Delete3')
        params = getParams.get_params('risk_management', 'Delete3')
        resp_c = getParams.get_resp_params('risk_management', 'Delete3', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'Delete3', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test17_details(self):
        path = getParams.get_url('risk_management', 'details')
        params = getParams.get_params('risk_management', 'details')
        resp_c = getParams.get_resp_params('risk_management', 'details', 'code')
        resp_m = getParams.get_resp_params('risk_management', 'details', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])