import unittest
import json
from utils import readExcel
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='CouponsBuild').get_log()
fp = readExcel.excel_path('test_datas.xlsx')


class CouponsBuild(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        HttpUtil.get_token()
        # pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_couponsBuild(self):
        path = readExcel.cell_value(fp, 'couponsBuild', 1, 1)
        params = json.loads(readExcel.cell_value(fp, 'couponsBuild', 1, 2))

        coupons_infos = readExcel.row_values2(fp, 'couponsBuild')
        for i in coupons_infos:
            coupons_type = i[0]

            # 判断卡券优惠类型(固定金额/满减/折扣)并赋值
            if '停车' in coupons_type and i[2] == '' and i[3] != '':
                params['couponsTypeRule']['discount'] = int(i[3])
            elif '满减' not in coupons_type and i[2] != '':
                params['couponsTypeRule']['amount'] = int(i[2] * 100)
            else:
                params['couponsTypeRule']['discount'] = ''
                params['couponsTypeRule']['amount'] = ''

            if type(i[2]) == str and i[2] != '':
                params['couponsTypeRule']['full'] = int(i[2].split('-')[0]) * 100
                params['couponsTypeRule']['minus'] = int(i[2].split('-')[1]) * 100
            else:
                params['couponsTypeRule']['full'] = ''
                params['couponsTypeRule']['minus'] = ''

            if '停车' in coupons_type and i[3] != '':
                params['deductionType'] = 2
            else:
                params['deductionType'] = 1

            # 判断卡券属性(付费会员专享券/普通券)
            if '付费' in i[4]:
                params['isMemberCoupons'] = 1
            elif '普通' in i[4]:
                params['isMemberCoupons'] = 0

            # 判断卡券类型
            if '停车' in coupons_type:
                params['type'] = 0
            elif '满减' in coupons_type:
                params['type'] = 7
            elif '活动' in coupons_type:
                params['type'] = 6
            elif '代金' in coupons_type:
                params['type'] = 3

            # 判断卡券发放类型
            if '直接发放' in i[5]:
                params['sendType'] = 1
            elif '渠道投放' in i[5]:
                params['sendType'] = 2
            else:
                params['sendType'] = 3

            # 如果为停车券,使用范围只能是停车场,否则默认服务台/会员中心
            if params['type'] == 0:
                params['useSpaces'] = list('2')
            else:
                params['useSpaces'] = list('1')

            params['name'] = i[1]
            params['onlineStartDt'] = i[6]
            params['onlineEndDt'] = i[7]
            params['explanation'] = i[8]
            params['img'] = i[9]
            params['description'] = i[10]
            params['reminder'] = i[11]
            # print(params)
            response = HttpUtil().do_post(path, params)

