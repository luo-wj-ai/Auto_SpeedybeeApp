from appium.webdriver.common.appiumby import AppiumBy as Aby

class PresetsAct:
    actions1 = [
        # 点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        # 点击进入预设页面
        ('tap', 0.0531, 0.4978),
        #分类-FITERS
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="分类"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="FILTERS"]'),
        ('tap', 0.483, 0.2232),
        #作者-Beatflight
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="作者"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="Betaflight"]'),
        ('tap', 0.483, 0.2232),
        # 固件-4.4
         ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="固件"]'),
         ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="4.4"]'),
         ('tap', 0.483, 0.2232),
        # 状态-OFFICIAL
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="状态"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="OFFICIAL"]'),
        ('tap', 0.483, 0.2232),
        #点击第一个模式
        ('tap', 0.5749, 0.3415),
        #点击应用
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="应用"]'),
        #点击警告-同意
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="同意"]'),
        #点击关闭
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="关闭"]'),
         # 等待时间
        ('time', 2)
    ]