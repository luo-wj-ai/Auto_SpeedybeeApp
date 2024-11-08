from appium.webdriver.common.appiumby import AppiumBy as Aby

class PortAct:

    actions1 =[
        #点击专家模式
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeButton[@name="专家模式"]'),
        #点击进入端口页面
        ('tap',0.0531,0.2746),
        #UART1-遥测输出-FrSky
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="已禁用"])[4]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="FrSky"]'),
        #UART1-遥测输出-AUTO-默认
        #滑动
        ('rolling', 'xpath', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="串行接收机"])[4]',
         '(//XCUIElementTypeStaticText[@name="串行接收机"])[1]'),
        #UART3-遥控输出-iBUS
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="已禁用"])[9]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="iBUS"]'),
        #UART3-遥控输出-19200
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="AUTO"])[10]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="19200"]'),
        # UART5-传感器-AUTO
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="57600"]'),
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="AUTO"])[20]'),
        # 滑动 0
        ('rolling', 'xpath', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="串行接收机"])[5]',
         '(//XCUIElementTypeStaticText[@name="串行接收机"])[4]'),
        # UART6-遥控输出-LTM
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="已禁用"])[16]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="LTM"]'),
        # UART6-遥控输出-38400
        ('click', 'xpath', 'el', Aby.XPATH, '(//XCUIElementTypeStaticText[@name="AUTO"])[18]'),
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="38400"]'),
        #点击保存并重新启动
        ('click', 'xpath', 'el', Aby.XPATH, '//XCUIElementTypeStaticText[@name="保存并重新启动"]'),
        #等待时间
        ('time', 2)
    ]