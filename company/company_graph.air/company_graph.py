# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 回到公司详情页，进入企业图谱
while not poco(text="企业背景").exists():
    poco.swipe([0.5,0.6],[0.5,0.4])

while poco(text="企业图谱").exists():
    poco(text="企业图谱").click()
    sleep(6.0)
    snapshot(msg="-----企业图谱详情页-----")
    poco.swipe([0.6,0.6],[0.4,0.4])
    keyevent("BACK")
    wait(Template(r"tpl1560149977071.png", record_pos=(-0.239, -0.081), resolution=(1080, 2340)))
    break

poco(text="股权结构").click()
wait(Template(r"tpl1560329934341.png", record_pos=(-0.181, -0.606), resolution=(1080, 1920)))
snapshot(msg="-----股权结构详情页-----")
keyevent("BACK")
wait(Template(r"tpl1560151650761.png", record_pos=(0.24, -0.076), resolution=(1080, 2340)))

# 回到公司详情页，执行company_context.air