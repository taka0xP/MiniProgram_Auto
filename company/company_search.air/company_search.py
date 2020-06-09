# -*- encoding=utf8 -*-
__author__ = "XU SIRUI"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from poco.exceptions import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 唤醒设备
wake()

# 关闭微信进程
stop_app("com.tencent.mm")
sleep(2.0)

# 启动微信，搜索天眼查小程序
start_app("com.tencent.mm")
poco("com.tencent.mm:id/bp").offspring("android.support.v7.widget.LinearLayoutCompat").child(
    "android.widget.RelativeLayout").child("com.tencent.mm:id/jb").wait_for_appearance()
# 点击右上角搜索按钮
poco("com.tencent.mm:id/bp").offspring("android.support.v7.widget.LinearLayoutCompat").child("android.widget"
                                                                                             ".RelativeLayout").child(
    "com.tencent.mm:id/jb").click()
wait(Template(r"tyc_wx_search.png", record_pos=(0.0, -0.399), resolution=(1080, 1920)))
poco(text="小程序").click()

sleep(1.0)
text("天眼查", search=True)

try:
    poco(text="天眼查企业工商查询").wait_for_appearance(timeout=30)
except PocoTargetTimeout:
    raise
if poco(text="天眼查企业工商查询").exists():
    poco(text="天眼查企业工商查询").click()

# 进入小程序，查公司
wait(Template(r"tyc_hot_search.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)))
assert_exists(Template(r"tyc_hot_search.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)),
              "-----完成首页加载-----")
snapshot(msg="-----小程序首页-----")

# 登录，点击“首页-我的”按钮
if poco(text="我的").exists():
    poco(text="我的").click()
sleep(3)

# 判断是否登录，已登录则回到首页-查公司
if poco(text="立即登录").exists():
    poco(text="立即登录").click()
    if poco(text="微信账号快速登录").exists():
        poco(text="微信账号快速登录").click()
    sleep(2.0)
    # 元素----一键登录授权弹窗中“允许”按钮
    if poco("android.widget.LinearLayout").offspring("android:id/content").child(
            "android.widget.RelativeLayout").offspring("com.tencent.mm:id/st").exists():
        poco("android.widget.LinearLayout").offspring("android:id/content").child(
            "android.widget.RelativeLayout").offspring("com.tencent.mm:id/st").click()
    sleep(2.0)
    poco(text="查公司").click()
    wait(Template(r"tyc_hot_search.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)))
else:
    poco(text="查公司").click()
    wait(Template(r"tyc_hot_search.png", record_pos=(0.004, -0.127), resolution=(1080, 1920)))

# 进入公司列表页
if poco(text="请输入公司名、人名等关键词").exists():
    poco(text="请输入公司名、人名等关键词").click()
    text("金堤", search=True)
    try:
        poco(text="北京金堤科技有限公司").wait_for_appearance()
    except PocoTargetTimeout:
        raise
snapshot(msg="-----首页-搜索结果-----")

click(Template(r"tyc_clear.png", record_pos=(0.404, -0.609), resolution=(1080, 2340)))
# wait(Template(r"tyc_recently_search.png", record_pos=(-0.394, -0.475), resolution=(1080, 2340)))
sleep(2.0)
if exists(Template(r"tyc_default_desc.png", record_pos=(-0.08, -0.797), resolution=(1080, 2340))):
    click(Template(r"tyc_default_desc.png", record_pos=(-0.08, -0.797), resolution=(1080, 2340)))
    sleep(1.0)
    text("百度网讯", search=True)
    try:
        poco(text="北京百度网讯科技有限公司").wait_for_appearance(timeout=30)
    except PocoTargetTimeout:
        raise
snapshot(msg="-----搜索列表页-搜索结果-----")

if poco(text="全部区域").exists():
    poco(text="全部区域").click()
    wait(Template(r"tyc_bj.png", record_pos=(-0.398, -0.435), resolution=(1080, 2340)))
    while poco(text="北京市").exists():
        poco(text="北京市").click()
        break
    try:
        poco(text="北京市全市").wait_for_appearance(timeout=30)
    except PocoTargetTimeout:
        raise
    while poco(text="北京市全市").exists():
        poco(text="北京市全市").click()
        break
    poco(text="北京百度网讯科技有限公司").wait_for_appearance(timeout=30)

if poco(text="更多筛选").exists():
    poco(text="更多筛选").click()
    try:
        poco(text="企业名称").wait_for_appearance(timeout=30)
    except PocoTargetTimeout:
        raise
    if poco(text="企业名称").exists():
        poco(text="企业名称").click()
    wait(Template(r"tyc_company_name_selected.png", record_pos=(-0.355, -0.263), resolution=(1080, 2340)))
    poco(text="确认").wait(1.0).click()
    try:
        poco(text="北京百度网讯科技有限公司").wait_for_appearance(timeout=30)
    except PocoTargetTimeout:
        raise
    snapshot(msg="-----公司搜索列表页，筛选结果-----")
    click(Template(r"tyc_bj_baidu.png", record_pos=(-0.103, -0.356), resolution=(1080, 2340)))
wait(Template(r"tyc_bj_baidu_search.png", record_pos=(-0.061, -0.507), resolution=(1080, 2340)))
sleep(10.0)
snapshot(msg="-----公司详情页-----")

# 进入公司详情页,执行company_baseinfo.air
