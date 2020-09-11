import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='member_marketing').get_log()


class MemberMarketing(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = getParams.get_url('member_marketing', 'getMemberList')
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_memberInfoList(self):
        params = getParams.get_params('member_marketing', 'getMemberList')
        resp_c = getParams.get_resp_params('member_marketing', 'getMemberList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getMemberList', 'msg')
        response = HttpUtil().do_post(self.url, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
