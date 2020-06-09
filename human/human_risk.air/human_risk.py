# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 人员天眼风险-周边风险
touch(Template(r"tpl1552038311335.png", record_pos=(-0.382, -0.194), resolution=(1080, 1920)))
wait(Template(r"tpl1552038334039.png", record_pos=(-0.342, -0.635), resolution=(1080, 1920)))
snapshot(msg="-----天眼风险详情页-----")
touch(Template(r"tpl1560478443887.png", record_pos=(0.405, -0.381), resolution=(1080, 2340)))
touch(wait(Template(r"tpl1560478523070.png", record_pos=(0.446, -0.531), resolution=(1080, 2340))))
wait(Template(r"tpl1552038520551.png", record_pos=(0.001, -0.15), resolution=(1080, 1920)))
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552038334039.png", record_pos=(-0.342, -0.635), resolution=(1080, 1920)))

# 人员天眼风险-预警信息
touch(Template(r"tpl1552038641053.png", record_pos=(0.218, -0.522), resolution=(1080, 1920)))
wait(Template(r"tpl1552038711032.png", record_pos=(-0.312, -0.327), resolution=(1080, 1920)))
touch(Template(r"tpl1560478754263.png", record_pos=(0.397, -0.381), resolution=(1080, 2340)))
wait(Template(r"tpl1552038733659.png", record_pos=(-0.406, -0.414), resolution=(1080, 1920)))
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552034130662.png", record_pos=(-0.392, -0.587), resolution=(1080, 1920)))

# 完成人员天眼风险验证，执行human_controller.air