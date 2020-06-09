# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 进入天眼风险
poco(text="查看风险").click()
wait(Template(r"tpl1559729260673.png", record_pos=(-0.168, -0.63), resolution=(1080, 1920)))
snapshot(msg="-----天眼风险详情页-----")

# 自身风险
poco(text="该公司 曾因未按时履行法律义务而被法院强制执行").click()
wait(Template(r"tpl1559536271734.png", record_pos=(-0.393, -0.399), resolution=(1080, 1920)))
snapshot(msg="-----风险信息-被执行人-列表页-----")
poco(text="执行法院：").click()
wait(Template(r"tpl1559732083395.png", record_pos=(-0.244, -0.581), resolution=(1080, 1920)))
snapshot(msg="-----风险信息-被执行人-详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1559729260673.png", record_pos=(-0.168, -0.63), resolution=(1080, 2340)))

# 周边风险
poco(text="周边风险(962)").click()
wait(Template(r"tpl1560322263311.png", record_pos=(-0.048, -0.708), resolution=(1080, 2340)))
poco(text="该公司 投资的沈阳分分钟企业管理有限公司曾因未按时履行法律义务而被法院强制执行").click()
wait(Template(r"tpl1560324686512.png", record_pos=(0.447, -0.424), resolution=(1080, 1920)))
snapshot(msg="-----天眼风险详情页-周边风险tab-被执行信息列表页-----")
poco(text="执行法院：").click()
sleep(1.0)
snapshot(msg="-----风险信息-被执行人-详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1559729260673.png", record_pos=(-0.168, -0.63), resolution=(1080, 2340)))

# 预警提醒
poco(text="预警提醒(887)").click()
wait(Template(r"tpl1559732375913.png", record_pos=(0.285, -0.531), resolution=(1080, 1920)))
poco(text="该公司 发生了注册资本变更").click()
wait(Template(r"tpl1559732454971.png", record_pos=(-0.17, -0.645), resolution=(1080, 1920)))
snapshot(msg="-----周边风险-变更记录-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tyc_bj_baidu.png", record_pos=(-0.053, -0.504), resolution=(1080, 1920)))

# 回到公司详情页，执行company_brand.air
