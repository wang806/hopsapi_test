import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='cms_Members').get_log()


class MembersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.path = getParams.get_url('members', 'getMemberList')
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getMemberList(self):
        path = getParams.get_url('members', 'getMemberList')
        params = getParams.get_params('members', 'getMemberList')
        resp_c = getParams.get_resp_params('members', 'getMemberList', 'code')
        resp_m = getParams.get_resp_params('members', 'getMemberList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getMemberInfo(self):
        params = getParams.get_params('members', 'getMemberInfo')
        path = getParams.get_url('members', 'getMemberInfo')+'/'+params
        resp_c = getParams.get_resp_params('members', 'getMemberInfo', 'code')
        resp_m = getParams.get_resp_params('members', 'getMemberInfo', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_getMemberVipBeyRecords(self):
        params = getParams.get_params('members', 'vipBeyRecords')
        path = getParams.get_url('members', 'vipBeyRecords')
        resp_c = getParams.get_resp_params('members', 'vipBeyRecords', 'code')
        resp_m = getParams.get_resp_params('members', 'vipBeyRecords', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_getCouponsType(self):
        params = getParams.get_params('members', 'coupons_type')
        path = getParams.get_url('members', 'coupons_type')
        resp_c = getParams.get_resp_params('members', 'coupons_type', 'code')
        resp_m = getParams.get_resp_params('members', 'coupons_type', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_members_export(self):
        params = getParams.get_params('members', 'members_export')
        path = getParams.get_url('members', 'members_export')
        resp_c = getParams.get_resp_params('members', 'members_export', 'code')
        response = HttpUtil().do_download_file(path, params)
        self.assertEqual(resp_c, response.status_code)
