# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 人员详情-作为法人
touch(Template(r"tpl1560479261655.png", record_pos=(-0.252, 0.156), resolution=(1080, 2340)))
wait(Template(r"tpl1560479315799.png", record_pos=(-0.251, -0.812), resolution=(1080, 2340)))
keyevent("BACK")
wait(Template(r"tpl1560481053959.png", record_pos=(-0.145, -0.57), resolution=(1080, 2340)))

# 人员详情-作为股东
touch(Template(r"tpl1560481053959.png", record_pos=(-0.145, -0.57), resolution=(1080, 2340)))
wait(Template(r"tpl1552039895307.png", record_pos=(-0.359, 0.075), resolution=(1080, 1920)))
touch(Template(r"tpl1560479261655.png", record_pos=(-0.252, 0.156), resolution=(1080, 2340)))
wait(Template(r"tpl1560479315799.png", record_pos=(-0.251, -0.812), resolution=(1080, 2340)))
keyevent("BACK")
wait(Template(r"tpl1560481073709.png", record_pos=(0.078, -0.572), resolution=(1080, 2340)))

# 人员详情-作为高管
touch(Template(r"tpl1560481073709.png", record_pos=(0.078, -0.572), resolution=(1080, 2340)))
wait(Template(r"tpl1552039917873.png", record_pos=(-0.356, 0.08), resolution=(1080, 1920)))
touch(Template(r"tpl1560479261655.png", record_pos=(-0.252, 0.156), resolution=(1080, 2340)))
wait(Template(r"tpl1560479315799.png", record_pos=(-0.251, -0.812), resolution=(1080, 2340)))
keyevent("BACK")

# 人员详情-曾经任职
touch(wait(Template(r"tpl1552040014933.png", record_pos=(0.366, 0.069), resolution=(1080, 1920))))
wait(Template(r"tpl1552040035910.png", record_pos=(-0.333, -0.55), resolution=(1080, 1920)))
touch(wait(Template(r"tpl1552040182098.png", record_pos=(-0.042, -0.639), resolution=(1080, 1920))))
touch(Template(r"tpl1552040226434.png", record_pos=(0.313, -0.643), resolution=(1080, 1920)))
wait(Template(r"tpl1552040239829.png", record_pos=(-0.329, -0.549), resolution=(1080, 1920)))
keyevent("BACK")
wait(Template(r"tpl1552040014933.png", record_pos=(0.366, 0.069), resolution=(1080, 1920)))

# 人员详情-实际控制权
for i in range(1000):
    if exists(Template(r"tpl1560491663418.png", record_pos=(0.355, -0.066), resolution=(1080, 2340))):
        touch(Template(r"tpl1560491663418.png", record_pos=(0.355, -0.066), resolution=(1080, 2340)))
        wait(Template(r"tpl1560494049959.png", record_pos=(-0.337, -0.609), resolution=(1080, 2340)))
        keyevent("BACK")
        break
    else:
        poco.swipe([0.5, 0.8], [0.5, 0.2])
        i = i + 1

for j in range(1000):
    if exists(Template(r"tpl1560500468373.png", record_pos=(0.342, -0.021), resolution=(1080, 2340))):
        touch(Template(r"tpl1560495050309.png", record_pos=(0.007, -0.249), resolution=(1080, 2340)))
        wait(Template(r"tpl1560479261655.png", record_pos=(-0.252, 0.156), resolution=(1080, 2340)))
        keyevent("BACK")
        break
    else:
        poco.swipe([0.5, 0.8], [0.5, 0.2])
        j = j + 1

# 人员详情-合作伙伴
if exists(Template(r"tpl1560500468373.png", record_pos=(0.342, -0.021), resolution=(1080, 2340))):
    touch(Template(r"tpl1560500468373.png", record_pos=(0.342, -0.021), resolution=(1080, 2340)))
    wait(Template(r"tpl1552038311335.png", record_pos=(-0.382, -0.194), resolution=(1080, 1920)))

# 返回首页-人员详情完成
touch(Template(r"tpl1552041222742.png", record_pos=(-0.237, 0.812), resolution=(1080, 1920)))
wait(Template(r"tpl1559270045736.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)))


