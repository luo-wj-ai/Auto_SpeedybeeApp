from abc import ABC, abstractmethod
from appium import webdriver
from appium.options.common import AppiumOptions
import threading


# 基础类：AppDriverBase
class AppDriverBase(ABC):
    _driver = None  # 类变量，用来存储共享的 driver 实例
    _lock = threading.Lock()  # 用于线程安全的锁
    link = "http://127.0.0.1:4723"  # 在父类中定义 link 属性

    def __init__(self, version):
        self.version = version
        self.options = AppiumOptions()  # 实例化 AppiumOptions，这样 options 是实例级的
        self.setup_options()

    @abstractmethod
    def setup_options(self):
        """子类实现具体的配置"""
        pass

    @classmethod
    def get_driver(cls, version="14"):
        """获取 driver 实例，确保只初始化一次"""
        if cls._driver is None:
            with cls._lock:  # 使用锁确保线程安全
                if cls._driver is None:  # 再次检查 driver 是否为 None
                    # 创建 AndroidAppDriver 实例并调用实例的 options
                    driver_instance = AndroidAppDriver(version)
                    cls._driver = webdriver.Remote(command_executor=cls.link, options=driver_instance.options)
        return cls._driver


class AndroidAppDriver(AppDriverBase):
    def setup_options(self):
        """为 Android 配置 Appium 驱动"""
        self.options.load_capabilities({
            "platformName": "Android",  # 目标平台为 Android
            "appium:platformVersion": self.version,  # 动态指定设备的 Android 系统版本
            "appium:deviceName": "Android phone",  # 设备名称，可以是任意值（例如"Android phone"）
            "appium:appPackage": "com.runcam.android.runcambf",  # 应用包名（需要测试的应用包名）
            "appium:appActivity": "com.runcam.android.runcambf.SplashActivity",  # 应用启动的 Activity
            "appium:automationName": "UiAutomator2",  # 指定自动化引擎为 UiAutomator2
            "appium:resetKeyboard": True,  # 重置输入法为默认的 Appium 输入法
            "appium:ignoreHiddenApiPolicyError": True,  # 忽略 Android 9+ 的隐藏 API 限制警告
            "appium:ensureWebviewsHavePages": True,  # 确保 Webview 页面加载时不会报空错误
            "appium:nativeWebScreenshot": True,  # 截屏时启用原生方式
            "appium:newCommandTimeout": 3600,  # 会话超时时间（秒）
            "appium:noReset": True,  # 不清除应用数据和缓存，保留应用状态
            "appium:skipInstall": True  # 跳过应用安装步骤（假设应用已经安装在设备上）
        })


class iOSAppDriver(AppDriverBase):
    def setup_options(self):
        """为 iOS 配置 Appium 驱动"""
        self.options.load_capabilities({
            "platformName": "iOS",
            "appium:platformVersion": self.version,
            "appium:deviceName": "iOS Phone",
            "appium:app": "com.runcam.speedybee",
            "appium:udid": "00008030-001109960186802E",
            "appium:automationName": "XCUITest"
        })


"""
# 示例：实例化 Android 驱动
android_version = "11.0"
android_driver_instance = AndroidAppDriver(version=android_version)
driver = android_driver_instance.get_driver()
"""
