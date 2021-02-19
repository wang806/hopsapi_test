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
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_temparlist(self):
        path = getParams.get_url('financial_management', 'temparlist')
        params = getParams.get_params('financial_management', 'temparlist')
        resp_c = getParams.get_resp_params('financial_management', 'temparlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'temparlist', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test04_chargelist(self):
        path = getParams.get_url('financial_management', 'chargelist')
        params = getParams.get_params('financial_management', 'chargelist')
        resp_c = getParams.get_resp_params('financial_management', 'chargelist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'chargelist', 'msg')
        response = HttpUtil().do_post(path, params)
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
        response = HttpUtil().do_get_with_params(path,params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test07_sysdiction3(self):
        path = getParams.get_url('financial_management', 'sysdiction3')
        params = getParams.get_params('financial_management', 'sysdiction3')
        resp_c = getParams.get_resp_params('financial_management', 'sysdiction3', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'sysdiction3', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
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

    def test09_orderInput1(self):
        path = getParams.get_url('financial_management', 'orderInput1')
        params = getParams.get_params('financial_management', 'orderInput1')
        resp_c = getParams.get_resp_params('financial_management', 'orderInput1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderInput1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test10_orderInput2(self):
        path = getParams.get_url('financial_management', 'orderInput2')
        params = getParams.get_params('financial_management', 'orderInput2')
        resp_c = getParams.get_resp_params('financial_management', 'orderInput2', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderInput2', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test11_createDownTask1(self):
        path = getParams.get_url('financial_management', 'createDownTask1')
        params = getParams.get_params('financial_management', 'createDownTask1')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test12_orderList001(self):
        path = getParams.get_url('financial_management', 'orderList001')
        params = getParams.get_params('financial_management', 'orderList001')
        resp_c = getParams.get_resp_params('financial_management', 'orderList001', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderList001', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test13_shangpindingdan(self):
        path = getParams.get_url('financial_management', 'shangpindingdan')
        params = getParams.get_params('financial_management', 'shangpindingdan')
        resp_c = getParams.get_resp_params('financial_management', 'shangpindingdan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'shangpindingdan', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test14_yuezudingdan(self):
        path = getParams.get_url('financial_management', 'yuezudingdan')
        params = getParams.get_params('financial_management', 'yuezudingdan')
        resp_c = getParams.get_resp_params('financial_management', 'yuezudingdan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'yuezudingdan', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test15_zhifuleixing(self):
        path = getParams.get_url('financial_management', 'zhifuleixing')
        params = getParams.get_params('financial_management', 'zhifuleixing')
        resp_c = getParams.get_resp_params('financial_management', 'zhifuleixing', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhifuleixing', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test16_chqakan(self):
        path = getParams.get_url('financial_management', 'chqakan')
        params = getParams.get_params('financial_management', 'chqakan')
        resp_c = getParams.get_resp_params('financial_management', 'chqakan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'chqakan', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
    def test17_daochu1(self):
        path = getParams.get_url('financial_management', 'daochu1')
        params = getParams.get_params('financial_management', 'daochu1')
        resp_c = getParams.get_resp_params('financial_management', 'daochu1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'daochu1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test18_kaquandingdan(self):
        path = getParams.get_url('financial_management', 'kaquandingdan')
        params = getParams.get_params('financial_management', 'kaquandingdan')
        resp_c = getParams.get_resp_params('financial_management', 'kaquandingdan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'kaquandingdan', 'msg')
        response = HttpUtil().do_get_with_params(path,params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test19_kaquandaoru(self):
        path = getParams.get_url('financial_management', 'kaquandaoru')
        params = getParams.get_params('financial_management', 'kaquandaoru')
        resp_c = getParams.get_resp_params('financial_management', 'kaquandaoru', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'kaquandaoru', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test20_taocan(self):
        path = getParams.get_url('financial_management', 'taocan')
        params = getParams.get_params('financial_management', 'taocan')
        resp_c = getParams.get_resp_params('financial_management', 'taocan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'taocan', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test21_fuifuhuiyuan(self):
        path = getParams.get_url('financial_management', 'fuifuhuiyuan')
        params = getParams.get_params('financial_management', 'fuifuhuiyuan')
        resp_c = getParams.get_resp_params('financial_management', 'fuifuhuiyuan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'fuifuhuiyuan', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test22_fuifuhuiyuan1(self):
        path = getParams.get_url('financial_management', 'fuifuhuiyuan1')
        params = getParams.get_params('financial_management', 'fuifuhuiyuan1')
        resp_c = getParams.get_resp_params('financial_management', 'fuifuhuiyuan1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'fuifuhuiyuan1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test23_qudaoliebiao(self):
        path = getParams.get_url('financial_management', 'qudaoliebiao')
        params = getParams.get_params('financial_management', 'qudaoliebiao')
        resp_c = getParams.get_resp_params('financial_management', 'qudaoliebiao', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'qudaoliebiao', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test24_qudaoliebiao1(self):
        path = getParams.get_url('financial_management', 'qudaoliebiao1')
        params = getParams.get_params('financial_management', 'qudaoliebiao1')
        resp_c = getParams.get_resp_params('financial_management', 'qudaoliebiao1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'qudaoliebiao1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test25_zhangdanjiafeileibiao(self):
        path = getParams.get_url('financial_management', 'zhangdanjiafeileibiao')
        params = getParams.get_params('financial_management', 'zhangdanjiafeileibiao')
        resp_c = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test26_zhangdanjiafeileibiao1(self):
        path = getParams.get_url('financial_management', 'zhangdanjiafeileibiao1')
        params = getParams.get_params('financial_management', 'zhangdanjiafeileibiao1')
        resp_c = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test27_zhangdanjiafeileibiao2(self):
        path = getParams.get_url('financial_management', 'zhangdanjiafeileibiao2')
        params = getParams.get_params('financial_management', 'zhangdanjiafeileibiao2')
        resp_c = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao2', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhangdanjiafeileibiao2', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test28_lintingrijie(self):
        path = getParams.get_url('financial_management', 'lintingrijie')
        params = getParams.get_params('financial_management', 'lintingrijie')
        resp_c = getParams.get_resp_params('financial_management', 'lintingrijie', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'lintingrijie', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test29_kemugunli(self):
        path = getParams.get_url('financial_management', 'kemugunli')
        params = getParams.get_params('financial_management', 'kemugunli')
        resp_c = getParams.get_resp_params('financial_management', 'kemugunli', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'kemugunli', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test30_kemugunli1(self):
        path = getParams.get_url('financial_management', 'kemugunli1')
        params = getParams.get_params('financial_management', 'kemugunli1')
        resp_c = getParams.get_resp_params('financial_management', 'kemugunli1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'kemugunli1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test31_bianji(self):
        path = getParams.get_url('financial_management', 'bianji')
        params = getParams.get_params('financial_management', 'bianji')
        resp_c = getParams.get_resp_params('financial_management', 'bianji', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bianji', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test32_caieujiekou(self):
        path = getParams.get_url('financial_management', 'caieujiekou')
        params = getParams.get_params('financial_management', 'caieujiekou')
        resp_c = getParams.get_resp_params('financial_management', 'caieujiekou', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'caieujiekou', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test33_caieujiekou1(self):
        path = getParams.get_url('financial_management', 'caieujiekou1')
        params = getParams.get_params('financial_management', 'caieujiekou1')
        resp_c = getParams.get_resp_params('financial_management', 'caieujiekou1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'caieujiekou1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test34_baocun(self):
        path = getParams.get_url('financial_management', 'baocun')
        params = getParams.get_params('financial_management', 'baocun')
        resp_c = getParams.get_resp_params('financial_management', 'baocun', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'baocun', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test35_zhifu(self):
        path = getParams.get_url('financial_management', 'zhifu')
        params = getParams.get_params('financial_management', 'zhifu')
        resp_c = getParams.get_resp_params('financial_management', 'zhifu', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhifu', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test36_chakan(self):
        path = getParams.get_url('financial_management', 'chakan')
        params = getParams.get_params('financial_management', 'chakan')
        resp_c = getParams.get_resp_params('financial_management', 'chakan', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'chakan', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test37_chakan1(self):
        path = getParams.get_url('financial_management', 'chakan1')
        params = getParams.get_params('financial_management', 'chakan1')
        resp_c = getParams.get_resp_params('financial_management', 'chakan1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'chakan1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])


    def test38_bianji2(self):
        path = getParams.get_url('financial_management', 'bianji2')
        params = getParams.get_params('financial_management', 'bianji2')
        resp_c = getParams.get_resp_params('financial_management', 'bianji2', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bianji2', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test39_bianjibaocun(self):
        path = getParams.get_url('financial_management', 'bianjibaocun')
        params = getParams.get_params('financial_management', 'bianjibaocun')
        resp_c = getParams.get_resp_params('financial_management', 'bianjibaocun', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bianjibaocun', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test40_puweihao(self):
        path = getParams.get_url('financial_management', 'puweihao')
        params = getParams.get_params('financial_management', 'puweihao')
        resp_c = getParams.get_resp_params('financial_management', 'puweihao', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'puweihao', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test41_liebiaoshouxifei(self):
        path = getParams.get_url('financial_management', 'liebiaoshouxifei')
        params = getParams.get_params('financial_management', 'liebiaoshouxifei')
        resp_c = getParams.get_resp_params('financial_management', 'liebiaoshouxifei', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'liebiaoshouxifei', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test42_zhifufangshi12(self):
        path = getParams.get_url('financial_management', 'zhifufangshi12')
        params = getParams.get_params('financial_management', 'zhifufangshi12')
        resp_c = getParams.get_resp_params('financial_management', 'zhifufangshi12', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhifufangshi12', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test43_zhanghuguianli(self):
        path = getParams.get_url('financial_management', 'zhanghuguianli')
        params = getParams.get_params('financial_management', 'zhanghuguianli')
        resp_c = getParams.get_resp_params('financial_management', 'zhanghuguianli', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'zhanghuguianli', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])


    def test44_openBank(self):
        path = getParams.get_url('financial_management', 'openBank')
        params = getParams.get_params('financial_management', 'openBank')
        resp_c = getParams.get_resp_params('financial_management', 'openBank', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'openBank', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test45_viewk(self):
        path = getParams.get_url('financial_management', 'view')
        params = getParams.get_params('financial_management', 'view')
        resp_c = getParams.get_resp_params('financial_management', 'view', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'view', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test46_detaillog(self):
        path = getParams.get_url('financial_management', 'detaillog')
        params = getParams.get_params('financial_management', 'detaillog')
        resp_c = getParams.get_resp_params('financial_management', 'detaillog', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'detaillog', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test47_accountupdate(self):
        path = getParams.get_url('financial_management', 'accountupdate')
        params = getParams.get_params('financial_management', 'accountupdate')
        resp_c = getParams.get_resp_params('financial_management', 'accountupdate', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'accountupdate', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test48_queryByPage03(self):
        path = getParams.get_url('financial_management', 'queryByPage03')
        params = getParams.get_params('financial_management', 'queryByPage03')
        resp_c = getParams.get_resp_params('financial_management', 'queryByPage03', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'queryByPage03', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test49_orderdetail3(self):
        path = getParams.get_url('financial_management', 'orderdetail')
        params = getParams.get_params('financial_management', 'orderdetail')
        resp_c = getParams.get_resp_params('financial_management', 'orderdetail', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'orderdetail', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])



    def test50_createDownTask01(self):
        path = getParams.get_url('financial_management', 'createDownTask01')
        params = getParams.get_params('financial_management', 'createDownTask01')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask01', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask01', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test51_configview1(self):
        path = getParams.get_url('financial_management', 'configview1')
        params = getParams.get_params('financial_management', 'configview1')
        resp_c = getParams.get_resp_params('financial_management', 'configview1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'configview1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test52_config(self):
        path = getParams.get_url('financial_management', 'config')
        params = getParams.get_params('financial_management', 'config')
        resp_c = getParams.get_resp_params('financial_management', 'config', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'config', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test53_config02(self):
        path = getParams.get_url('financial_management', 'config02')
        params = getParams.get_params('financial_management', 'config02')
        resp_c = getParams.get_resp_params('financial_management', 'config02', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'config02', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test54_paymentlist(self):
        path = getParams.get_url('financial_management', 'paymentlist')
        params = getParams.get_params('financial_management', 'paymentlist')
        resp_c = getParams.get_resp_params('financial_management', 'paymentlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'paymentlist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test55_createDownTask02(self):
        path = getParams.get_url('financial_management', 'createDownTask02')
        params = getParams.get_params('financial_management', 'createDownTask02')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask02', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask02', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test56_bookinglist(self):
        path = getParams.get_url('financial_management', 'bookinglist')
        params = getParams.get_params('financial_management', 'bookinglist')
        resp_c = getParams.get_resp_params('financial_management', 'bookinglist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bookinglist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test57_paymentdetail(self):
        path = getParams.get_url('financial_management', 'paymentdetail')
        params = getParams.get_params('financial_management', 'paymentdetail')
        resp_c = getParams.get_resp_params('financial_management', 'paymentdetail', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'paymentdetail', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test58_detaillog1(self):
        path = getParams.get_url('financial_management', 'detaillog1')
        params = getParams.get_params('financial_management', 'detaillog1')
        resp_c = getParams.get_resp_params('financial_management', 'detaillog1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'detaillog1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test59_changebusinessSetStatus(self):
        path = getParams.get_url('financial_management', 'changebusinessSetStatus')
        params = getParams.get_params('financial_management', 'changebusinessSetStatus')
        resp_c = getParams.get_resp_params('financial_management', 'changebusinessSetStatus', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'changebusinessSetStatus', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test60_changebusinessSetStatus1(self):
        path = getParams.get_url('financial_management', 'changebusinessSetStatus1')
        params = getParams.get_params('financial_management', 'changebusinessSetStatus1')
        resp_c = getParams.get_resp_params('financial_management', 'changebusinessSetStatus1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'changebusinessSetStatus1', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test61_bookinglist1(self):
        path = getParams.get_url('financial_management', 'bookinglist1')
        params = getParams.get_params('financial_management', 'bookinglist1')
        resp_c = getParams.get_resp_params('financial_management', 'bookinglist1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bookinglist1', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test62_bookingdetail1(self):
        path = getParams.get_url('financial_management', 'bookingdetail1')
        params = getParams.get_params('financial_management', 'bookingdetail1')
        resp_c = getParams.get_resp_params('financial_management', 'bookingdetail1', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'bookingdetail1', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test63_createDownTask11(self):
        path = getParams.get_url('financial_management', 'createDownTask11')
        params = getParams.get_params('financial_management', 'createDownTask11')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask11', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask11', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test64_settlementlist(self):
        path = getParams.get_url('financial_management', 'settlementlist')
        params = getParams.get_params('financial_management', 'settlementlist')
        resp_c = getParams.get_resp_params('financial_management', 'settlementlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'settlementlist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test65_settlementBookinglist(self):
        path = getParams.get_url('financial_management', 'settlementBookinglist')
        params = getParams.get_params('financial_management', 'settlementBookinglist')
        resp_c = getParams.get_resp_params('financial_management', 'settlementBookinglist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'settlementBookinglist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test66_createDownTask03(self):
        path = getParams.get_url('financial_management', 'createDownTask03')
        params = getParams.get_params('financial_management', 'createDownTask03')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask03', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask03', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])


    def test67_withdrawalApplylist(self):
        path = getParams.get_url('financial_management', 'withdrawalApplylist')
        params = getParams.get_params('financial_management', 'withdrawalApplylist')
        resp_c = getParams.get_resp_params('financial_management', 'withdrawalApplylist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'withdrawalApplylist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])


    def test68_createDownTask04(self):
        path = getParams.get_url('financial_management', 'createDownTask04')
        params = getParams.get_params('financial_management', 'createDownTask04')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask04', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask04', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test69_oweInvoicelist(self):
        path = getParams.get_url('financial_management', 'oweInvoicelist')
        params = getParams.get_params('financial_management', 'oweInvoicelist')
        resp_c = getParams.get_resp_params('financial_management', 'oweInvoicelist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'oweInvoicelist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test70_oweInvoicedetail(self):
        path = getParams.get_url('financial_management', 'oweInvoicedetail')
        params = getParams.get_params('financial_management', 'oweInvoicedetail')
        resp_c = getParams.get_resp_params('financial_management', 'oweInvoicedetail', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'oweInvoicedetail', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])


    def test71_createDownTask05(self):
        path = getParams.get_url('financial_management', 'createDownTask05')
        params = getParams.get_params('financial_management', 'createDownTask05')
        resp_c = getParams.get_resp_params('financial_management', 'createDownTask05', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'createDownTask05', 'msg')
        response = HttpUtil().do_post(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test72_applicationlist(self):
        path = getParams.get_url('financial_management', 'applicationlist')
        params = getParams.get_params('financial_management', 'applicationlist')
        resp_c = getParams.get_resp_params('financial_management', 'applicationlist', 'code')
        resp_m = getParams.get_resp_params('financial_management', 'applicationlist', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])