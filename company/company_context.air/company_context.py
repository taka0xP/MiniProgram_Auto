# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 企业背景
# 企业背景-工商信息
while not poco(text="风险信息").exists():
    poco.swipe([0.5,0.6],[0.6,0.4])
poco(text="工商信息").click()
wait(Template(r"tpl1559811453646.png", record_pos=(0.215, -0.461), resolution=(1080, 2340)))
snapshot(msg="-----工商信息详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551946957541.png", record_pos=(-0.373, 0.025), resolution=(1080, 1920)))

# 企业背景-主要人员
poco(text="主要人员").click()
wait(Template(r"tpl1560330927656.png", record_pos=(0.335, -0.606), resolution=(1080, 1920)))
snapshot(msg="-----主要人员详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551947746652.png", record_pos=(-0.129, -0.088), resolution=(1080, 1920)))

# 企业背景-股东信息
poco(text="股东信息").click()
wait(Template(r"tpl1551948610508.png", record_pos=(-0.267, -0.536), resolution=(1080, 1920)))
snapshot(msg="-----股东信息详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551947997013.png", record_pos=(0.123, 0.309), resolution=(1080, 1920)))

# 企业背景-对外投资
poco(text="对外投资").click()
wait(Template(r"tpl1551948578345.png", record_pos=(-0.367, -0.55), resolution=(1080, 1920)))
snapshot(msg="-----对外投资详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551948085206.png", record_pos=(0.368, -0.076), resolution=(1080, 1920)))

# 企业背景-股权结构
touch(Template(r"tpl1551948274862.png", record_pos=(-0.369, 0.194), resolution=(1080, 1920)))
wait(Template(r"tpl1551948300734.png", record_pos=(-0.182, -0.609), resolution=(1080, 1920)))
snapshot(msg="-----股权结构详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551948274862.png", record_pos=(-0.369, 0.194), resolution=(1080, 1920)))

# 企业背景-最终受益人
poco(text="最终受益人").click()
wait(Template(r"tpl1551948440031.png", record_pos=(-0.368, -0.625), resolution=(1080, 1920)))
snapshot(msg="-----最终受益人详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551948423261.png", record_pos=(-0.129, 0.194), resolution=(1080, 1920)))

# 企业背景-实际控制权
poco(text="实际控制权").click()
wait(Template(r"tpl1551948531830.png", record_pos=(-0.352, -0.628), resolution=(1080, 1920)))
snapshot(msg="-----实际控制权详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551948516978.png", record_pos=(0.12, 0.202), resolution=(1080, 1920)))

# 企业背景-变更记录
poco(text="变更记录").click()
wait(Template(r"tpl1551949067252.png", record_pos=(-0.406, -0.519), resolution=(1080, 1920)))
snapshot(msg="-----变更记录详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551949045065.png", record_pos=(0.368, 0.202), resolution=(1080, 1920)))

# 企业背景-企业年报
poco(text="企业年报").click()
wait(Template(r"tpl1551949163738.png", record_pos=(-0.383, -0.622), resolution=(1080, 1920)))
snapshot(msg="-----企业年报列表页-----")
if poco(text="2017年度").exists():
    poco(text="2017年度").click()
    wait(Template(r"tpl1551949215450.png", record_pos=(-0.38, -0.624), resolution=(1080, 1920)))
    snapshot(msg="-----企业年报详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551949136131.png", record_pos=(-0.377, 0.473), resolution=(1080, 1920)))

# 企业背景-附近同行
poco(text="附近同行").click()
wait(Template(r"tpl1559812345120.png", record_pos=(-0.299, -0.621), resolution=(1080, 2340)))
snapshot(msg="-----附件同行详情页-----")
keyevent("BACK")
wait(Template(r"tpl1559812310517.png", record_pos=(-0.128, 0.727), resolution=(1080, 2340)))

# 回到公司详情页，执行company_riskInfo.air
