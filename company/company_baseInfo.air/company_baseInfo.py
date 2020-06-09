# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 基本信息-更多号码
poco(text="更多号码").click()
wait(Template(r"tyc_more_num.png", record_pos=(-0.006, -0.18), resolution=(1080, 1920)))
poco(text="关闭").click()
wait(Template(r"tyc_bj_baidu.png", record_pos=(-0.053, -0.504), resolution=(1080, 1920)))

# 基本信息-企业名片
poco(text="企业名片").click()
wait(Template(r"tyc_card.png", record_pos=(-0.004, -0.082), resolution=(1080, 2340)))
snapshot(msg="-----企业名片-----")
keyevent("BACK")

# 股东
poco(text="持股比例 99.50%").click()
wait(Template(r"tyc_lyh_logo.png", record_pos=(-0.397, -0.59), resolution=(1080, 1920)))
snapshot(msg="-----股东-人员详情页-----")
keyevent("BACK")
wait(Template(r"tyc_bj_baidu.png", record_pos=(-0.053, -0.504), resolution=(1080, 1920)))

# 董监高
poco(text="共有24家公司").click()
wait(Template(r"tyc_lzx_logo.png", record_pos=(-0.321, -0.589), resolution=(1080, 1920)))
snapshot(msg="-----董监高-人员详情页-----")
keyevent("BACK")
wait(Template(r"tyc_bj_baidu.png", record_pos=(-0.053, -0.504), resolution=(1080, 1920)))

# 回到公司详情页，执行company_risk.air
