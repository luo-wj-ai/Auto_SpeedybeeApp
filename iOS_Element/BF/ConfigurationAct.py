from appium.webdriver.common.appiumby import AppiumBy as Aby

class ConfigurationAct:
    actions1 = [
        #点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        #点击进入配置页面
        ('tap', 0.0531, 0.3304),
    #系统配置
        #PID循环更新频率-0.4Hz
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="3.2 kHz"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="0.4 kHz"]'),

    #飞控板和传感器对齐设置
        # 横滚偏移度数	360
        # 俯仰偏移度	360
        # 航向偏移指数	360
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]','360'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]', '360'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]', '360'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),

        #第一陀螺-自定义
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="CW 0°"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="自定义"]'),
        #磁力计角度偏移-自定义
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="默认"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="自定义"][2]'),

    #加速度计微调
        # 横滚微调-300
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@va1lue="0"])[1]', '300'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        # 俯仰微调-300
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]', '300'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #摄像头
        #FPV摄像头角度-90
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="0"]','90'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #Dshot信标配置
        #信标音调
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="1"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #RX_LOST
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="RX_LOST, 当TX关闭或信号丢失时发出蜂鸣声（重复直到TX正常为止）。" and @value="0"]',),
#滑动
        ('swipe',0.5362,0.6439,0.5362,0.3627),
    #其他功能
        #6个按钮
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="INFLIGHT_ACC_CAL, 飞行中加速计校准"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeSwitch[@name="SOFTSERIAL, 软串口"])[1]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="GPS, 用于导航和遥测的GPS"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="SONAR, 声纳"]'),
        ('swipe', 0.5362, 0.6439, 0.5362, 0.3627),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="TRANSPONDER, 比赛计圈器"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeSwitch[@name="BLACKBOX, 黑盒日志记录器"]'),
        # 等待时间
        ('time', 2)
    ]