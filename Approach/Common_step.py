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
    def enter_CLI_mode(self):
        """进入cli模式"""
        pass

    @abstractmethod
    def enter_CLI_mode(self):
        """进入cli模式"""
        pass

#小米手机的运行
class Android_Common_Step(Common_Step):

    def Open_expert_mode(self):
        """进入专家模式"""
        actions = [
        #隐私政策
            # 同意隐私政策
            ('click', 'ID', 'el', 'com.runcam.android.runcambf:id/mCheckBox'),
            # 点击同意
            ('click', 'ID', 'el', 'com.runcam.android.runcambf:id/AgreeBtn'),
        #首页
            # 点击开始使用
            ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="开始使用"]'),
             #  点击＋号搜索设备   1077*2396
            ('click', 'XPATH', 'el', '//android.widget.FrameLayout[@resource-id="com.runcam.android.runcambf:id/start_layout"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]'),
             #同意定位
            ('click', 'XPATH', 'el', '//android.widget.Button[@text="本次使用允许"]'),
             #同意
            ('click', 'XPATH', 'el', '//android.widget.Button[@text="始终允许"]'),
             #点击立即连接
            ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="立即连接"]'),
             #跳过密码
            ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="跳过"]'),
            ('time', 2),
         #速览页
             #点击专家模式
            ('click', 'XPATH', 'el', '//android.widget.Button[@content-desc="专家模式"]'),
            # 等待时间
            ('time', 2)
        ]
        testmove(actions, self.driver)
        pass

#
    def Exit_expert_mode(self):
        pass  # 暂时不实现或添加你的逻辑

    def bluetooth_passwd(self):
        pass  # 暂时不实现或添加你的逻辑

    #获取diff文件
    def enter_CLI_mode(self):
        actions = [
        #滑动到cli输入diff
            #滑动到页面最底部
            (),
            #点击CLI页面
            ('click', 'XPATH', 'el', '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/cli_icon"]'),
            #因为CLI页面还有BUG。需要进入两次
            ('click', 'XPATH', 'el', '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/cli_icon"]'),
            #输入diff命令
            ('sendkeys', 'XPATH', 'el',
             '//android.widget.AutoCompleteTextView[@resource-id="com.runcam.android.runcambf:id/send_content"]',
             "diff"),
            #点击发送
            ('click', 'XPATH', 'el', '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/send_btn"]'),
            #点击复制按钮——复制到剪切板存放着
            ('click', 'XPATH', 'el', '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/copy_btn"]'),
        #defaults恢复默认设置
            # defaults输入命令
            ('sendkeys', 'XPATH', 'el',
             '//android.widget.AutoCompleteTextView[@resource-id="com.runcam.android.runcambf:id/send_content"]',
             "defaults"),
            # 点击发送
            ('click', 'XPATH', 'el',
             '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/send_btn"]'),
            #滑动到页面最顶部
            (),
            #点击设置页面——主要是为了退出飞控的CLI页面
            ('click', 'XPATH', 'el',
             '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/setup_icon"]'),
            # 等待时间
            ('time', 2)
        ]
        pass  # 暂时不实现或添加你的逻辑


"""
# 示例：实例化并调用方法
if __name__ == "__main__":
    # 假设 driver 已经初始化好，这里使用一个假的 driver
    driver = None  # 这里应当替换为实际的 driver 实例

    # 实例化 Android_Common_Step 类
    android_steps = Android_Common_Step(driver)

    # 调用 Open_expert_mode 方法
    android_steps.Open_expert_mode()
    
    """