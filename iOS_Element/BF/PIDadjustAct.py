from appium.webdriver.common.appiumby import AppiumBy as Aby

class PIDadjustAct:
    actions1 = [
        # 点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        # 点击进入PID调整页面
        ('tap', 0.0531, 0.5536),
#PID设置——————————————————————————

        #自定义配置文件名称-名称01
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="自定义配置文件名称"])[1]', 'mingcheng01'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        # 自定义配置文件名称-名称02
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="自定义配置文件名称"])[1]','mingcheng02'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
# 滑动
        ('swipe', 0.5362, 0.6439, 0.5362, 0.3627),
    #Feed-forward
        #  抖动抑制-20
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="7"]','20'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #  平滑度-75
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="25"]', '75'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #   增压-50
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="15"])[1]', '50'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #  最大速率-150
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="90"]', '150'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
        #  转换阈值-1
        ('send', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeTextField[@value="0"])[1]', '1'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="Done"]'),
# 滑动
        ('swipe', 0.5362, 0.6439, 0.5362, 0.3627),
    # l值释放
        #截止频率-50
        ('send', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeTextField[@value="15"]', '50'),



        # 等待时间
        ('time', 2)
    ]