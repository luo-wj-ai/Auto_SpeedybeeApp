from abc import ABC, abstractmethod
from appium import webdriver
from appium.options.common import AppiumOptions


class AppDriverBase(ABC):
    def __init__(self, version):
        self.version = version
        self.options = AppiumOptions()
        self.link = "http://127.0.0.1:4723/wd/hub"
        self.setup_options()
        self.driver = webdriver.Remote(command_executor=self.link, options=self.options)

    @abstractmethod
    def setup_options(self):
        pass

    def get_driver(self):
        return self.driver


class AndroidAppDriver(AppDriverBase):
    def setup_options(self):
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
        self.options.load_capabilities({
            "platformName": "iOS",
            "appium:platformVersion": self.version,
            "appium:deviceName": "iOS Phone",
            "appium:app": "com.runcam.speedybee",
            "appium:udid": "00008030-001109960186802E",
            "appium:automationName": "XCUITest"
        })


"""
# 实例化 Android 驱动
android_version = "11.0"
android_driver_instance = AndroidAppDriver(version=android_version)
driver = android_driver_instance.get_driver()
"""
