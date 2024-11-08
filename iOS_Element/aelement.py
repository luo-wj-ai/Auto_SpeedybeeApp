"""
IOS-App 专家模式修改非空指定参数测试用例
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




class COMMONSTEP_IOS:
    start_action = [
        #点击加号
        # ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2]')
        ('tap',0.502415459,0.831473214)
    ]
    get_cli_result_action = [
        #先滑动
        #开始20-577，结束20-325
        ('swipe', 0.0483,0.6439,0.0483,0.3627),
        #等一会
        ('time',1),
        #点击cli
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeOther[@name="水平滚动条, 1页"])[1]'),
        #输入dump
        ('sendkeys', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeTextView[2]','diff'),
        #点击发送
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Send"]'),
        # 等待数据返回
        ('time', 2)
    ]
    resetting =[
        # 先输入defaults
        ('sendkeys', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeTextView[2]', 'defaults'),
        # 点击发送
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Send"]'),
        # 等待重置ing
        ('time', 2),
        # 点击断开连接飞控
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="断开连接"]')
    ]
