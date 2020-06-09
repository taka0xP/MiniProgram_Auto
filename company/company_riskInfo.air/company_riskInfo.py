# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 开庭公告
while not poco(text="企业发展").exists():
    poco.swipe([0.5,0.7],[0.5,0.4])
poco(text="开庭公告").click()
wait(Template(r"tpl1551951133614.png", record_pos=(-0.417, -0.586), resolution=(1080, 1920)))
snapshot(msg="-----开庭公告列表页-----")
poco(text="案号：").click()
wait(Template(r"tpl1551951269273.png", record_pos=(0.113, -0.518), resolution=(1080, 1920)))
snapshot(msg="-----开庭公告详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551950935509.png", record_pos=(-0.38, -0.016), resolution=(1080, 1920)))

# 法律诉讼
poco(text="法律诉讼").click()
wait(Template(r"tpl1551951133614.png", record_pos=(-0.417, -0.586), resolution=(1080, 1920)))
snapshot(msg="-----法律诉讼列表页-----")
poco(text="案号：").click()
wait(Template(r"tpl1551951551486.png", record_pos=(0.0, -0.15), resolution=(1080, 1920)))
snapshot(msg="-----法律诉讼详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551951376066.png", record_pos=(-0.123, -0.017), resolution=(1080, 1920)))

# 法院公告
poco(text="法院公告").click()
wait(Template(r"tpl1551952917626.png", record_pos=(-0.379, -0.586), resolution=(1080, 1920)))
snapshot(msg="-----法院公告列表页-----")
poco(text="公告类型：").click()
wait(Template(r"tpl1551952985707.png", record_pos=(-0.404, -0.498), resolution=(1080, 1920)))
snapshot(msg="-----法院公告详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551952899201.png", record_pos=(0.123, -0.019), resolution=(1080, 1920)))

# 被执行人
poco(text="被执行人").click()
wait(Template(r"tpl1551954303473.png", record_pos=(-0.383, -0.555), resolution=(1080, 1920)))
snapshot(msg="-----被执行人列表页-----")
poco(text="执行标的：").click()
wait(Template(r"tpl1551954386013.png", record_pos=(-0.384, -0.601), resolution=(1080, 1920)))
snapshot(msg="-----被执行人详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551954286954.png", record_pos=(-0.375, 0.254), resolution=(1080, 1920)))

# 行政处罚
poco(text="行政处罚").click()
wait(Template(r"tpl1551954489020.png", record_pos=(-0.346, -0.445), resolution=(1080, 1920)))
snapshot(msg="-----行政处罚-工商局列表页-----")
poco(text="违法行为类型：").click()
wait(Template(r"tpl1551954544805.png", record_pos=(-0.374, -0.625), resolution=(1080, 1920)))
snapshot(msg="-----行政处罚-工商局详情页-----")
keyevent("BACK")
wait(Template(r"tpl1551954489020.png", record_pos=(-0.346, -0.445), resolution=(1080, 1920)))
poco(text="信用中国(8)").click()
snapshot(msg="-----行政处罚-信用中国列表页-----")
poco(text="处罚名称：").click()
wait(Template(r"tpl1551954694611.png", record_pos=(-0.386, -0.618), resolution=(1080, 1920)))
snapshot(msg="-----行政处罚-信用中国详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551954466291.png", record_pos=(0.122, 0.256), resolution=(1080, 1920)))

# 股权出质
poco(text="股权出质").click()
wait(Template(r"tpl1551954861794.png", record_pos=(-0.379, -0.632), resolution=(1080, 1920)))
snapshot(msg="-----股权出质列表页-----")
poco(text="登记编号：").click()
wait(Template(r"tpl1551954922453.png", record_pos=(-0.389, -0.48), resolution=(1080, 1920)))
snapshot(msg="-----股权出质详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1551954843939.png", record_pos=(-0.378, 0.529), resolution=(1080, 1920)))

# 回到公司详情页，执行company_develop.air
