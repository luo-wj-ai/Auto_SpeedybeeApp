from appium.webdriver.common.appiumby import AppiumBy as Aby

class BatteryAct:
    actions1 = [
        # 点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        # 点击进入电池页面
        ('tap', 0.0531, 0.3862),
    #电池
        #最低单芯电压-5
        ('clear', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="3.30"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="5"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #最高单芯电压-5
        ('clear', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="4.30"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="5"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        # 警告单芯电压-5
        ('clear', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="3.50"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeKey[@name="5"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        # 容量-20000
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]','20000'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #电压计
        #比例-255
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="110"]', '255'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #电阻分压器数值-255
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="10"]', '255'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #倍数-255
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="1"]', '255'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #电流计
        #比例-16000
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="386"]', '16000'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #偏移量-32000
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="0"]', '32000'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
    #点击保存
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="保存"]'),
        #等待时间
        ('time',2)
    ]


