from abc import ABC, abstractmethod

from Approach.Control_Ele import testmove

#这是dev分支
# 抽象基类定义通用操作
class Common_Step(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def Open_expert_mode(self):
        """打开专家模式"""
        pass

    @abstractmethod
    def Exit_expert_mode(self):
        """退出专家模式"""
        pass

    @abstractmethod
    def bluetooth_passwd(self):
        """校验蓝牙密码，暂时不实现"""
        pass

    @abstractmethod
    def get_diff_result(self):
        """CLI模式下执行diff命令，获取命令返回的结果"""
        pass


class Android_Common_Step(Common_Step):

    def Open_expert_mode(self):
        actions = [
        #隐私政策
            # 同意隐私政策
            ('click', 'ID', 'el', 'com.runcam.android.runcambf:id/mCheckBox'),
            # 点击同意
            ('click', 'ID', 'el', 'com.runcam.android.runcambf:id/AgreeBtn'),
        #首页
            # 点击开始使用
         #    ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="开始使用"]'),
         #     #  点击＋号搜索设备   1077*2396
         #     ('tap', 0.50417,0.84808),
         #     ('time', 1),
         #     #同意定位
         #     ('click', 'ID', 'el', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'),
         #     #同意
         #   ('click', 'ID', 'el', 'com.android.permissioncontroller:id/permission_allow_button'),
         #     ('time', 1),
         #     #点击立即连接
         #   ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="立即连接"]'),
         #     #跳过密码
         #   ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="跳过"]'),
         #     ('time', 1),
         # #速览页
         #     #点击专家模式
         #    ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="专家模式"]'),
            # 等待时间
            ('time', 1),
            ('time', 2)
        ]
        testmove(actions, self.driver)
        pass

    def Exit_expert_mode(self):
        pass  # 暂时不实现或添加你的逻辑

    def bluetooth_passwd(self):
        pass  # 暂时不实现或添加你的逻辑

    def get_diff_result(self):
        pass  # 暂时不实现或添加你的逻辑