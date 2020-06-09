# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

while not poco(text="历史信息").exists():
    poco.swipe([0.5,0.7],[0.5,0.4])
    
# 商标信息
poco(text="商标信息").click()
wait(Template(r"tpl1552271807027.png", record_pos=(-0.151, -0.494), resolution=(1080, 1920)))
snapshot(msg="-----商标信息列表页-----")
poco(text="注册号：").click()
wait(Template(r"tpl1552271911820.png", record_pos=(-0.383, -0.281), resolution=(1080, 1920)))
snapshot(msg="-----商标信息详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552271788406.png", record_pos=(-0.375, 0.186), resolution=(1080, 1920)))


# 专利信息
poco(text="专利信息").click()
wait(Template(r"tpl1552272087034.png", record_pos=(-0.404, -0.588), resolution=(1080, 1920)))
snapshot(msg="-----专利信息列表页-----")
poco(text="申请号：").click()
wait(Template(r"tpl1552272915254.png", record_pos=(-0.412, -0.476), resolution=(1080, 1920)))
snapshot(msg="-----专利信息详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552272077641.png", record_pos=(-0.13, 0.185), resolution=(1080, 1920)))

# 著作权
poco(text="著作权").click()
wait(Template(r"tpl1552272984028.png", record_pos=(-0.39, -0.459), resolution=(1080, 1920)))
snapshot(msg="-----著作权-软件著作权列表页-----")
poco(text="软件简称：").click()
wait(Template(r"tpl1552273036591.png", record_pos=(-0.406, -0.582), resolution=(1080, 1920)))
snapshot(msg="-----著作权-软件著作权详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552272984028.png", record_pos=(-0.39, -0.459), resolution=(1080, 1920)))
poco(text="作品著作权(5000)").click()
wait(Template(r"tpl1552273105882.png", record_pos=(-0.403, -0.45), resolution=(1080, 1920)))
snapshot(msg="-----著作权-作品著作权列表页-----")
poco(text="登记号：").click()
wait(Template(r"tpl1552273036591.png", record_pos=(-0.406, -0.582), resolution=(1080, 1920)))
snapshot(msg="-----著作权-作品著作权详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552272972021.png", record_pos=(0.121, 0.189), resolution=(1080, 1920)))

# 网站备案
poco(text="网站备案").click()
wait(Template(r"tpl1552274138190.png", record_pos=(-0.395, -0.543), resolution=(1080, 1920)))
snapshot(msg="-----网站备案列表-----")
keyevent("BACK")
wait(Template(r"tpl1552274123410.png", record_pos=(0.369, 0.189), resolution=(1080, 1920)))

# 回到公司详情页，执行company_history.air
