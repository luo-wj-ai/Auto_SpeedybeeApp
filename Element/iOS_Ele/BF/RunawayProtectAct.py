from appium.webdriver.common.appiumby import AppiumBy as Aby

class RunawayProtectAct:
    actions1 = [
         # 点击专家模式
         ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
         # 点击进入失控保护页面
         ('tap', 0.0531, 0.4420),
    #有效脉冲范围设置
        #最小长度-2250
         ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="885"]', '2250'),
         ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #最大长度-2250
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="2115"]', '2250'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #频道回退设置
        #横滚Hold
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="Auto"])[1]'),
        ('click', 'xpath', 'el', Aby.XPATH,
         '//XCUIElementTypeOther[@name="drop_down"]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]'),
        #俯仰Hold
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="Auto"])[1]'),
        ('click', 'xpath', 'el', Aby.XPATH,
         '//XCUIElementTypeOther[@name="drop_down"]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]'),
        #方向Hold
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="Auto"])[1]'),
        ('click', 'xpath', 'el', Aby.XPATH,
         '//XCUIElementTypeOther[@name="drop_down"]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]'),
        #油门Hold
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="Auto"])[1]'),
        ('click', 'xpath', 'el', Aby.XPATH,
         '//XCUIElementTypeOther[@name="drop_down"]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]',),
# 滑动
        ('swipe', 0.5362, 0.6439, 0.5362, 0.3627),
    #二阶失控保护-设置
        #触发二阶-20
        ('clear', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="1.5"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="2"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="0"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #低油门
        ('clear', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="10"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="3"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="0"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #点击保存并重新启动
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="保存并重新启动"]'),
         # 等待时间
        ('time', 2)

    ]