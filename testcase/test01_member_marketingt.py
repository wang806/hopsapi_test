import unittest
import random
import string
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
from utils.mobile import mobile
logger = Log(logger='member_marketing').get_log()


class MemberMarketing(unittest.TestCase):
    ruleID = ''

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
        print(params)
        params['mMobile'] = mobile()
        print(params)
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

    def test09_viewMemberPlusInfo(self):
        self.path = getParams.get_url('member_marketing', 'viewMemberPlusInfo')
        resp_c = getParams.get_resp_params('member_marketing', 'viewMemberPlusInfo', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'viewMemberPlusInfo', 'msg')
        response = HttpUtil().do_get(self.path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test10_validityMemberPointList(self):
        path = getParams.get_url('member_marketing', 'validityMemberPointList')
        params = getParams.get_params('member_marketing', 'validityMemberPointList')
        resp_c = getParams.get_resp_params('member_marketing', 'validityMemberPointList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'validityMemberPointList', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test11_validityMemberPoint(self):
        path = getParams.get_url('member_marketing', 'validityMemberPoint')
        params = getParams.get_params('member_marketing', 'validityMemberPoint')
        resp_c = getParams.get_resp_params('member_marketing', 'validityMemberPoint', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'validityMemberPoint', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test12_viewValidityMemberPoint(self):
        self.path = getParams.get_url('member_marketing', 'viewValidityMemberPoint')
        resp_c = getParams.get_resp_params('member_marketing', 'viewValidityMemberPoint', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'viewValidityMemberPoint', 'msg')
        response = HttpUtil().do_get(self.path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test13_getPointRuleList(self):
        path = getParams.get_url('member_marketing', 'getPointRuleList')
        params = getParams.get_params('member_marketing', 'getPointRuleList')
        resp_c = getParams.get_resp_params('member_marketing', 'getPointRuleList', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'getPointRuleList', 'msg')
        response = HttpUtil().do_post(path, params)
        MemberMarketing.ruleID = response['rows'][0]['id']
        print(MemberMarketing.ruleID)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    # def test14_addPointRule(self):
    #     path = getParams.get_url('member_marketing', 'addPointRule')
    #     params = getParams.get_params('member_marketing', 'addPointRule')
    #     resp_c = getParams.get_resp_params('member_marketing', 'addPointRule', 'code')
    #     resp_m = getParams.get_resp_params('member_marketing', 'addPointRule', 'msg')
    #     response = HttpUtil().do_post(path, params)
    #     print(response)
    #     self.assertEqual(resp_c, response['code'])
    #     self.assertEqual(resp_m, response['msg'])

    def test15_deletePointRule(self):
        path = getParams.get_url('member_marketing', 'deletePointRule')
        print(path)
        path = path + str(MemberMarketing.ruleID)
        print(path)
        resp_c = getParams.get_resp_params('member_marketing', 'deletePointRule', 'code')
        resp_m = getParams.get_resp_params('member_marketing', 'deletePointRule', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
















