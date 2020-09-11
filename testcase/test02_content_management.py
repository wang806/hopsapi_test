import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='content_management').get_log()


class ContentManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.path = getParams.get_url('content_management', 'getActivityClassificationList')
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_activityClassificationList(self):
        path = getParams.get_url('content_management', 'getActivityClassificationList')
        params = getParams.get_params('content_management', 'getActivityClassificationList')
        resp_c = getParams.get_resp_params('content_management', 'getActivityClassificationList', 'code')
        resp_m = getParams.get_resp_params('content_management', 'getActivityClassificationList', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

