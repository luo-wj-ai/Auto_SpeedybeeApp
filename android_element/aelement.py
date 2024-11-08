"""
Android-App 专家模式修改非空指定参数测试用例
"""
from appium.webdriver.common.appiumby import AppiumBy as Aby

# # 飞控型号，固件版本判断
# 飞控型号
class VERMATCH:
    flight_ts = [
        'SPEEDYBEEF405V4',
        'SPEEDYBEEF405V3',
        'SPEEDYBEEF7V2',
        'SPEEDYBEEF7V3',
        'SPEEDYBEE405MINI',
        'SPEEDYBEE405WING'
    ]

    bf_fmversion = [
        'BTFL 4.5.0',
        'BTFL 4.4.3',
        'BTFL 4.4.2',
        'BTFL 4.4.0',
        'BTFL 4.3.2',
        'BTFL 4.3.1',
        'BTFL 4.3.0',
        'BTFL 4.2.11'
    ]

    inav_fmversion = [
        'INAV 7.1.2',
        'INAV 7.1.1',
        'INAV 7.1.0',
        'INAV 7.0.0',
        'INAV 6.1.1',
        'INAV 6.1.0'
    ]




class COMMONSTEP:
    # 添加设备xpath
    addxpath1 = '//android.widget.FrameLayout[@resource-id="com.runcam.android.runcambf:id/start_layout"]'
    addxpath2 = '/android.widget.FrameLayout/android.view.View/android.view.View'
    addxpath3 = '/android.view.View/android.view.View/android.widget.ImageView[4]'
    addxpath = addxpath1 + addxpath2 + addxpath3
    common_open = {
        # 勾选隐私协议ID
        "1": "com.runcam.android.runcambf:id/mCheckBox",
        # 同意隐私协议ID
        "2": "com.runcam.android.runcambf:id/AgreeBtn",
        # click start-xpath
        "3": "//android.widget.Button[@content-desc='开始使用']",
        # 添加设备xpath
        "4": addxpath,
        # # 小米平板定位permission
        "99": '//android.widget.Button[@text="仅在使用中允许"]',
        # # 小米平板连接设备permission
        "100": '//android.widget.Button[@text="始终允许"]',
        # permission1id
        "5": "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
        # permission2id
        "6": "com.android.permissioncontroller:id/permission_allow_button",
        '7': '//android.view.View[@content-desc="发现apptest"]',  # xpath
        '8': '//android.widget.Button[@content-desc="可识别的设备"]',  # xpath
        '9': r'//android.view.View[@content-desc="app F405 V4 24:58:7C:9C:0C:22"]',
        # 立即链接xpath
        "10": '//android.widget.Button[@content-desc="立即连接"]',
        "11": '//android.view.View[@content-desc="蓝牙连接失败"]',
        # 进入专家模式xpath
        "12": '//android.widget.Button[@content-desc="专家模式"]'  # 检测时间过长，待替换
    }

    start_action = [
        ('click', 'id', 'el', Aby.ID, '1'),
        ('click', 'id', 'el', Aby.ID, '2'),
        ('click', 'xpath', 'el', Aby.XPATH, '3'),
        ('click', 'xpath', 'el', Aby.XPATH, '4'),
        ('click', 'xpath', 'el', Aby.XPATH, '99'),
        ('click', 'xpath', 'el', Aby.XPATH, '100')
        # ('click', 'xpath', 'el', Aby.XPATH, '10')
        # ('click', 'id', 'el', Aby.ID, '5'),
        # ('click', 'id', 'el', Aby.ID, '6'),
    ]

    common_close = {
        # 设置页面id
        "1": "com.runcam.android.runcambf:id/setup_icon",
        # “更多” 功能按键id
        "2": "com.runcam.android.runcambf:id/expend_img",
        # “重置" 按键id
        "3": "com.runcam.android.runcambf:id/reset_settings_btn",
        # 弹窗确认id
        "4": "com.runcam.android.runcambf:id/submmit_btn",
        # 断开链接xpath
        "5": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/disconnect_btn"]'
    }

    close_action = [
        ('click', 'id', 'el', Aby.ID, '1'),
        ('click', 'id', 'el', Aby.ID, '2'),
        ('click', 'id', 'el', Aby.ID, '3'),
        ('click', 'id', 'el', Aby.ID, '4'),
        ('click', 'xpath', 'el', Aby.XPATH, '5')
    ]

    common_get_cli_result = {
        # 进入cli界面id
        "1": "com.runcam.android.runcambf:id/cli_icon",
        # diffsendid
        "2": "com.runcam.android.runcambf:id/send_content",
        # sendid
        "3": "com.runcam.android.runcambf:id/send_btn",
        # clipboard id
        "4": "com.runcam.android.runcambf:id/copy_btn"
    }

    get_cli_result_action = [
        ('click', 'id', 'el', Aby.ID, '1'),
        ('click', 'id', 'el', Aby.ID, '2'),
        ('click', 'id', 'el', Aby.ID, '3'),
        ('click', 'id', 'el', Aby.ID, '4')
    ]

    roll_cli = {
        # 电池菜单
        "1": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/battery_icon']",
        # 配置菜单
        "2": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/configuration_icon']"
    }
