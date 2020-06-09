# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

while not poco(text="本企业的问答").exists():
    poco.swipe([0.5,0.7],[0.5,0.4])
sleep(1.0)
# 历史信息-工商信息
touch(Template(r"tpl1552027073742.png", record_pos=(-0.368, -0.451), resolution=(1080, 1920)))
wait(Template(r"tpl1552027096836.png", record_pos=(-0.336, -0.604), resolution=(1080, 1920)))
snapshot(msg="-----历史工商信息列表-----")
keyevent("BACK")
wait(Template(r"tpl1552027073742.png", record_pos=(-0.368, -0.451), resolution=(1080, 1920)))

# 历史信息-历史股东
poco(text="历史股东").click()
wait(Template(r"tpl1552027224881.png", record_pos=(-0.27, -0.526), resolution=(1080, 1920)))
snapshot(msg="-----历史股东列表-----")
keyevent("BACK")
wait(Template(r"tpl1552027216172.png", record_pos=(-0.128, -0.45), resolution=(1080, 1920)))

# 历史信息-对外股东
touch(Template(r"tpl1552027292364.png", record_pos=(0.12, -0.454), resolution=(1080, 1920)))
# poco(text="对外投资").click()
wait(Template(r"tpl1552027349148.png", record_pos=(-0.369, -0.546), resolution=(1080, 1920)))
snapshot(msg="-----历史对外投资列表-----")
keyevent("BACK")
wait(Template(r"tpl1552027292364.png", record_pos=(0.12, -0.454), resolution=(1080, 1920)))

# 历史信息-开庭公告
touch(Template(r"tpl1552027404618.png", record_pos=(0.368, -0.447), resolution=(1080, 1920)))
# poco(text="开庭公告").click()
wait(Template(r"tpl1552027425498.png", record_pos=(-0.412, -0.58), resolution=(1080, 1920)))
snapshot(msg="-----历史开庭公告列表页-----")
# touch(Template(r"tpl1552027425498.png", record_pos=(-0.412, -0.58), resolution=(1080, 1920)))
poco(text="案号：").click()
wait(Template(r"tpl1552029375389.png", record_pos=(0.108, -0.519), resolution=(1080, 1920)))
snapshot(msg="-----历史开庭公告详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552027404618.png", record_pos=(0.368, -0.447), resolution=(1080, 1920)))

# 历史信息-法律诉讼
touch(Template(r"tpl1552029515955.png", record_pos=(-0.375, -0.176), resolution=(1080, 1920)))
# poco(text="法律诉讼").click()
wait(Template(r"tpl1552029527730.png", record_pos=(-0.379, -0.541), resolution=(1080, 1920)))
snapshot(msg="-----历史法律诉讼列表页-----")
# touch(Template(r"tpl1552029527730.png", record_pos=(-0.379, -0.541), resolution=(1080, 1920)))
poco(text="案件类型：").click()
wait(Template(r"tpl1552029580555.png", record_pos=(-0.002, -0.222), resolution=(1080, 1920)))
snapshot(msg="-----历史法律诉讼详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552029515955.png", record_pos=(-0.375, -0.176), resolution=(1080, 1920)))

# 历史信息-法院公告
touch(Template(r"tpl1552029639403.png", record_pos=(-0.128, -0.181), resolution=(1080, 1920)))
# poco(text="法院公告").click()
wait(Template(r"tpl1552029651324.png", record_pos=(-0.381, -0.587), resolution=(1080, 1920)))
snapshot(msg="-----历史法院公告列表页-----")
# touch(Template(r"tpl1552029651324.png", record_pos=(-0.381, -0.587), resolution=(1080, 1920)))
poco(text="公告类型：").click()
wait(Template(r"tpl1552029751694.png", record_pos=(-0.386, -0.515), resolution=(1080, 1920)))
snapshot(msg="-----历史法院公告详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552029639403.png", record_pos=(-0.128, -0.181), resolution=(1080, 1920)))

# 历史信息-行政处罚
touch(Template(r"tpl1552029806652.png", record_pos=(-0.377, 0.093), resolution=(1080, 1920)))
# poco(text="行政处罚").click()
wait(Template(r"tpl1552029814340.png", record_pos=(-0.35, -0.446), resolution=(1080, 1920)))
snapshot(msg="-----历史行政处罚-工商局列表页-----")
# touch(Template(r"tpl1552029814340.png", record_pos=(-0.35, -0.446), resolution=(1080, 1920)))
poco(text="违法行为类型：").click()
wait(Template(r"tpl1552029878515.png", record_pos=(-0.378, -0.625), resolution=(1080, 1920)))
snapshot(msg="-----历史行政处罚-工商局详情页-----")
keyevent("BACK")
wait(Template(r"tpl1552029814340.png", record_pos=(-0.35, -0.446), resolution=(1080, 1920)))
# touch(Template(r"tpl1552029933288.png", record_pos=(0.228, -0.643), resolution=(1080, 1920)))
poco(text="信用中国(4)").click()
wait(Template(r"tpl1552029961585.png", record_pos=(-0.384, -0.529), resolution=(1080, 1920)))
snapshot(msg="-----历史行政处罚-信用中国列表页-----")
# touch(Template(r"tpl1552029961585.png", record_pos=(-0.384, -0.529), resolution=(1080, 1920)))
poco(text="处罚名称：").click()
wait(Template(r"tpl1552030016371.png", record_pos=(-0.386, -0.616), resolution=(1080, 1920)))
snapshot(msg="-----历史行政处罚-信用中国详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552029806652.png", record_pos=(-0.377, 0.093), resolution=(1080, 1920)))

# 历史信息-股权出质
touch(Template(r"tpl1552031042142.png", record_pos=(-0.13, 0.09), resolution=(1080, 1920)))
# poco(text="股权出质").click()
wait(Template(r"tpl1552031056714.png", record_pos=(-0.4, -0.578), resolution=(1080, 1920)))
snapshot(msg="-----历史股权出质列表页-----")
# touch(Template(r"tpl1552031056714.png", record_pos=(-0.4, -0.578), resolution=(1080, 1920)))
poco(text="出质人：").click()
wait(Template(r"tpl1552031260847.png", record_pos=(-0.393, -0.442), resolution=(1080, 1920)))
snapshot(msg="-----历史股权出质详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552031042142.png", record_pos=(-0.13, 0.09), resolution=(1080, 1920)))

# 历史信息-行政许可
touch(Template(r"tpl1552031378520.png", record_pos=(0.368, 0.09), resolution=(1080, 1920)))
# poco(text="行政许可").click()
wait(Template(r"tpl1552031399247.png", record_pos=(0.006, 0.033), resolution=(1080, 1920)))
snapshot(msg="-----历史行政许可-工商局：（百度）-----")
# touch(Template(r"tpl1552031456964.png", record_pos=(0.227, -0.638), resolution=(1080, 1920)))
poco(text="信用中国(1)").click()
wait(Template(r"tpl1552031466966.png", record_pos=(-0.367, -0.531), resolution=(1080, 1920)))
snapshot(msg="-----历史行政许可-信用中国列表页-----")
# touch(Template(r"tpl1552031466966.png", record_pos=(-0.367, -0.531), resolution=(1080, 1920)))
poco(text="决定文书号：").click()
wait(Template(r"tpl1552031522835.png", record_pos=(-0.371, -0.627), resolution=(1080, 1920)))
snapshot(msg="-----历史行政许可-信用中国详情页-----")
keyevent("BACK")
sleep(1.0)
keyevent("BACK")
wait(Template(r"tpl1552031378520.png", record_pos=(0.368, 0.09), resolution=(1080, 1920)))

# 回到公司详情页，执行company_discuss.air

