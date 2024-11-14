from abc import ABC, abstractmethod
from appium import webdriver
from appium.options.common import AppiumOptions
import threading


class AppDriverBase(ABC):
    _driver = None  # 类变量，用来存储共享的 driver 实例
    _lock = threading.Lock()  # 用于线程安全的锁

    def __init__(self, version):
        self.version = version
        self.options = AppiumOptions()
        self.link = "http://127.0.0.1:4723/wd/hub"
        self.setup_options()

    @abstractmethod
    def setup_options(self):
        """子类实现具体的配置"""
        pass

    @classmethod
    def get_driver(cls, version="12"):
        """获取 driver 实例，确保只初始化一次"""
        if cls._driver is None:
            with cls._lock:  # 使用锁确保线程安全
                if cls._driver is None:  # 再次检查 driver 是否为 None
                    print("Initializing Appium Driver")
                    # 如果没有实例，创建并初始化 driver
                    cls._driver = webdriver.Remote(command_executor=cls.link, options=cls.options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """关闭 driver 实例"""
        if cls._driver:
            print("Quitting Appium Driver")
            cls._driver.quit()
            cls._driver = None


class AndroidAppDriver(AppDriverBase):
    def setup_options(self):
        """为 Android 配置 Appium 驱动"""
        self.options.load_capabilities({
            "platformName": "Android",
            "appium:platformVersion": self.version,
            "appium:deviceName": "Android phone",
            "appium:appPackage": "com.runcam.android.runcambf",
            "appium:appActivity": "com.runcam.android.runcambf.SplashActivity",
            "appium:resetKeyboard": True,
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
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
