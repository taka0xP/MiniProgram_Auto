# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

while not poco(text="经营信息").exists():
    poco.swipe([0.5, 0.7], [0.5, 0.4])
# 企业发展-融资历史
poco(text="融资历史").click()
wait(Template(r"tpl1559817197435.png", record_pos=(-0.067, -0.797), resolution=(1080, 2340)))
snapshot(msg="-----融资历史详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552010263937.png", record_pos=(-0.378, -0.344), resolution=(1080, 1920)))

# 企业发展-投资事件
poco(text="投资事件").click()
wait(Template(r"tpl1552010547333.png", record_pos=(-0.255, -0.558), resolution=(1080, 1920)))
snapshot(msg="-----投资事件详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552010521661.png", record_pos=(-0.128, -0.337), resolution=(1080, 1920)))

# 企业发展-核心团队
poco(text="核心团队").click()
wait(Template(r"tpl1552011091338.png", record_pos=(-0.154, -0.616), resolution=(1080, 1920)))
snapshot(msg="-----核心团队详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552011057217.png", record_pos=(0.121, -0.337), resolution=(1080, 1920)))

# 企业发展-企业业务
poco(text="企业业务").click()
wait(Template(r"tpl1552011264601.png", record_pos=(-0.211, -0.516), resolution=(1080, 1920)))
snapshot(msg="-----企业业务详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552011245341.png", record_pos=(0.369, -0.334), resolution=(1080, 1920)))

# 企业发展-竞品信息
poco(text="竞品信息").click()
wait(Template(r"tpl1552011383966.png", record_pos=(-0.201, -0.581), resolution=(1080, 1920)))
snapshot(msg="-----竞品信息详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552011357004.png", record_pos=(-0.377, -0.066), resolution=(1080, 1920)))

# 回到公司详情页，执行company_manage.air
