# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

poco.swipe([0.5, 0.8], [0.5, 0.2])

# 公司详情-问答模块
wait(Template(r"tpl1560152626079.png", record_pos=(-0.364, 0.085), resolution=(1080, 2340)))
touch(Template(r"tpl1560152626079.png", record_pos=(-0.364, 0.085), resolution=(1080, 2340)))
wait(Template(r"tpl1560152716340.png", record_pos=(-0.178, -0.74), resolution=(1080, 2340)))
snapshot(msg="-----问答详情-----")
keyevent("BACK")
wait(Template(r"tpl1560152626079.png", record_pos=(-0.364, 0.085), resolution=(1080, 2340)))

# 返回首页，准备执行“查老板”流程
wait(Template(r"tpl1560152955304.png", record_pos=(-0.372, 1.016), resolution=(1080, 2340)))
touch(Template(r"tpl1560152955304.png", record_pos=(-0.372, 1.016), resolution=(1080, 2340)))
wait(Template(r"tpl1559270045736.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)))

