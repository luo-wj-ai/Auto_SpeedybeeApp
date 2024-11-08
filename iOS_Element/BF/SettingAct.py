from appium.webdriver.common.appiumby import AppiumBy as Aby


class SettingAct:
    actions1 = [
        #点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        # 刚刚进入设置页面
        # 点击校准加速度计
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="校准加速度计"]'),
        # 右下角三个点
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="3point"]'),
        #  ①点击校准校准加速度计
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="校准加速度计"]'),
        #  ②点击重置设置
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="重置设置"]'),
        # ③再次点击重置
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="重置"]'),
        # 等待时间
        ('time', 2)
    ]


