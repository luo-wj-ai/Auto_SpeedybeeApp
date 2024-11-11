from abc import ABC, abstractmethod

from Approach.Control_Ele import testmove


# 抽象基类定义通用操作
class Common_Step(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def Open_expert_mode(self,actions):
        """打开专家模式"""
        pass

    @abstractmethod
    def Exit_expert_mode(self,actions):
        """退出专家模式"""
        pass

    @abstractmethod
    def bluetooth_passwd(self,actions):
        """校验蓝牙密码"""
        pass

    @abstractmethod
    def get_diff_result(self,actions):
        """CLI模式下执行diff命令，获取命令返回的结果"""
        pass


class Android_Common_Step(Common_Step):

    def Open_expert_mode(self):
        actions1 = [
            # 点击专家模式
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
        pass