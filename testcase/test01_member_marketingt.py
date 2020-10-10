import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='member_marketing').get_log()


class MemberMarketing(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_memberInfoList(self):
        path = getParams.get_url('member_marketing', 'getMemberList')
        params = getParams.get_params('member_marketing', 'getMemberList')
        resp_c = getParams.get_resp_params('member_marketing', 'getMemberList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getMemberList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getMemberAccountList(self):
        path = getParams.get_url('member_marketing', 'getMemberAccountList')
        params = getParams.get_params('member_marketing', 'getMemberAccountList')
        resp_c = getParams.get_resp_params('member_marketing', 'getMemberAccountList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getMemberAccountList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_viewMemberInfo(self):
        self.path = getParams.get_url('member_marketing', 'viewMemberInfo')
        resp_c = getParams.get_resp_params('member_marketing', 'viewMemberInfo', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'viewMemberInfo', 'msg')
        response = HttpUtil().do_get(self.path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_getMemberAccountList(self):
        path = getParams.get_url('member_marketing', 'editMemberInfo')
        params = getParams.get_params('member_marketing', 'editMemberInfo')
        resp_c = getParams.get_resp_params('member_marketing', 'editMemberInfo', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'editMemberInfo', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test05_addMember(self):
        path = getParams.get_url('member_marketing', 'addMember')
        params = getParams.get_params('member_marketing', 'addMember')
        resp_c = getParams.get_resp_params('member_marketing', 'addMember', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'addMember', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test06_viewMemberBehaviour(self):
        path = getParams.get_url('member_marketing', 'viewMemberBehaviour')
        params = getParams.get_params('member_marketing', 'viewMemberBehaviour')
        resp_c = getParams.get_resp_params('member_marketing', 'viewMemberBehaviour', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'viewMemberBehaviour', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_getMemberBehaviourList(self):
        path = getParams.get_url('member_marketing', 'getMemberBehaviourList')
        params = getParams.get_params('member_marketing', 'getMemberBehaviourList')
        resp_c = getParams.get_resp_params('member_marketing', 'getMemberBehaviourList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getMemberBehaviourList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test08_getMemberPlusList(self):
        self.path = getParams.get_url('member_marketing', 'getMemberPlusList')
        resp_c = getParams.get_resp_params('member_marketing', 'getMemberPlusList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getMemberPlusList', 'msg')
        response = HttpUtil().do_get(self.path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])



