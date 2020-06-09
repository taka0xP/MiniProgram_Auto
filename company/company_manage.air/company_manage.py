# -*- encoding=utf8 -*-
__author__ = "XU "

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

while not poco(text="知识产权").exists():
    poco.swipe([0.5,0.7],[0.5,0.4])

# 招聘信息
poco(text="招聘信息").click()
wait(Template(r"tpl1559817511835.png", record_pos=(-0.38, -0.767), resolution=(1080, 2340)))
snapshot(msg="-----招聘信息列表页-----")
poco(text="发布日期：").click()
wait(Template(r"tpl1559817540617.png", record_pos=(-0.362, -0.362), resolution=(1080, 2340)))
snapshot(msg="-----招聘信息详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552011950034.png", record_pos=(-0.374, 0.319), resolution=(1080, 1920)))

# 行政许可
poco(text="行政许可").click()
wait(Template(r"tpl1552012154894.png", record_pos=(-0.349, -0.523), resolution=(1080, 1920)))
snapshot(msg="-----行政许可-工商局列表页-----")
poco(text="许可文件名称：").click()
wait(Template(r"tpl1552012217799.png", record_pos=(-0.342, -0.634), resolution=(1080, 1920)))
snapshot(msg="-----行政许可-工商局详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552012154894.png", record_pos=(-0.349, -0.523), resolution=(1080, 1920)))
poco(text="信用中国(4)").click()
wait(Template(r"tpl1552012296399.png", record_pos=(-0.368, -0.526), resolution=(1080, 1920)))
snapshot(msg="-----行政许可-信用中国列表页-----")
poco(text="决定文书号：").click()
wait(Template(r"tpl1552012366761.png", record_pos=(-0.369, -0.629), resolution=(1080, 1920)))
snapshot(msg="-----行政许可-信用中国详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552012136684.png", record_pos=(-0.127, 0.319), resolution=(1080, 1920)))

# 税务评级
poco(text="税务评级").click()
wait(Template(r"tpl1552012525237.png", record_pos=(-0.345, -0.55), resolution=(1080, 1920)))
snapshot(msg="-----税务评级列表-----")
keyevent("BACK")
wait(Template(r"tpl1552012512063.png", record_pos=(0.12, 0.316), resolution=(1080, 1920)))

# 抽查检查
poco(text="抽查检查").click()
wait(Template(r"tpl1552012612588.png", record_pos=(-0.343, -0.595), resolution=(1080, 1920)))
snapshot(msg="-----抽查检查列表-----")
keyevent("BACK")
wait(Template(r"tpl1552012593710.png", record_pos=(0.368, 0.313), resolution=(1080, 1920)))

# 资质证书
poco(text="资质证书").click()
wait(Template(r"tpl1552013317691.png", record_pos=(-0.367, -0.586), resolution=(1080, 1920)))
snapshot(msg="-----资质证书列表页-----")
poco(text="许可证编号：").click()
wait(Template(r"tpl1560763816784.png", record_pos=(-0.337, -0.776), resolution=(1080, 2340)))
snapshot(msg="-----资质证书详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552013269603.png", record_pos=(-0.375, -0.444), resolution=(1080, 1920)))

# 招投标
poco(text="招投标").click()
wait(Template(r"tpl1552013536027.png", record_pos=(-0.396, -0.544), resolution=(1080, 1920)))
snapshot(msg="-----招投标列表页-----")
poco(text="采购人：").click()
wait(Template(r"tpl1552013616479.png", record_pos=(0.302, -0.193), resolution=(1080, 1920)))
snapshot(msg="-----招投标详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552013523535.png", record_pos=(-0.128, -0.447), resolution=(1080, 1920)))

# 产品信息
poco(text="产品信息").click()
wait(Template(r"tpl1552013724110.png", record_pos=(-0.211, -0.529), resolution=(1080, 1920)))
snapshot(msg="-----产品信息列表-----")
keyevent("BACK")
wait(Template(r"tpl1552013714094.png", record_pos=(0.12, -0.443), resolution=(1080, 1920)))

# 微信公众号
poco(text="微信公众号").click()
wait(Template(r"tpl1552013821732.png", record_pos=(-0.194, -0.553), resolution=(1080, 1920)))
snapshot(msg="-----微信公众号列表-----")
keyevent("BACK")
wait(Template(r"tpl1552013803531.png", record_pos=(0.369, -0.445), resolution=(1080, 1920)))

# 进出口信用
poco(text="进出口信用").click()
wait(Template(r"tpl1559818818272.png", record_pos=(-0.369, -0.805), resolution=(1080, 2340)))
snapshot(msg="-----进出口信用详情页-----")
keyevent("BACK")
wait(Template(r"tpl1559818788679.png", record_pos=(-0.381, 0.802), resolution=(1080, 2340)))

# 回到公司详情页，执行company_property.air
