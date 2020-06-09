# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 回到首页，查老板

poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/d88").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.RelativeLayout").child("android.widget.FrameLayout").offspring("com.tencent.mm:id/x").child("android.widget.FrameLayout").child("android.widget.FrameLayout")[0].offspring("android.view.ViewGroup").child("android.widget.FrameLayout").offspring("android.webkit.WebView")[0].child("android.view.View")[2].click() # 元素--首页查老板tab
wait(Template(r"tpl1552032932959.png", record_pos=(-0.086, -0.301), resolution=(1080, 1920)))
snapshot(msg="-----首页查老板-----")

poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/d88").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.tencent.mm:id/w").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[1].click() # 元素--首页底部查老板tab
wait(Template(r"tpl1552033448196.png", record_pos=(-0.315, -0.01), resolution=(1080, 1920)))
snapshot(msg="-----查老板热门搜索页-----")
if exists(Template(r"tpl1560504563311.png", record_pos=(0.406, -0.798), resolution=(1080, 2340))):
    touch(Template(r"tpl1560504563311.png", record_pos=(0.406, -0.798), resolution=(1080, 2340)))
    touch(wait(Template(r"tpl1560504692249.png", record_pos=(-0.115, -0.791), resolution=(1080, 2340))))
else:
    touch(wait(Template(r"tpl1560504692249.png", record_pos=(-0.115, -0.791), resolution=(1080, 2340))))
    
text("柳超", search=True)
wait(Template(r"tpl1552034107158.png", record_pos=(-0.335, -0.116), resolution=(1080, 1920)))
touch(Template(r"tpl1552034130662.png", record_pos=(-0.359, -0.436), resolution=(1080, 1920)))
wait(Template(r"tpl1552034130662.png", record_pos=(-0.392, -0.587), resolution=(1080, 1920)))
snapshot(msg="-----人员详情页-----")
touch(Template(r"tpl1560477537745.png", record_pos=(0.002, -0.54), resolution=(1080, 2340)))
snapshot(msg="-----人员详情蒙层-----")
touch(wait(Template(r"tpl1560477563520.png", record_pos=(0.0, -0.502), resolution=(1080, 2340))))
wait(Template(r"tpl1552034130662.png", record_pos=(-0.392, -0.587), resolution=(1080, 1920)))

# 进入人员详情后，执行human_risk.air

