# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 品牌
while not poco(text="品牌").exists():
    poco.swipe([0.5, 0.6], [0.5, 0.4])
poco(text="品牌").click()
wait(Template(r"tpl1559803724369.png", record_pos=(0.013, -0.738), resolution=(1080, 2340)))
snapshot(msg="-----项目品牌详情页-----")
keyevent("BACK")

# 机构
while not poco(text="机构").exists():
    poco.swipe([0.5, 0.6], [0.5, 0.4])
poco(text="机构").click()
wait(Template(r"tpl1559803396347.png", record_pos=(-0.07, -0.733), resolution=(1080, 2340)))
snapshot(msg="-----投资机构详情页-----")
keyevent("BACK")

wait(Template(r"tpl1559803376513.png", record_pos=(-0.011, -0.603), resolution=(1080, 2340)))

# 回到公司详情页，执行company_grahp.air
