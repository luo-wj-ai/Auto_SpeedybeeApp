from abc import ABC, abstractmethod

from Approach.Control_Ele import execute_actions



#这是dev分支
# 抽象基类定义通用操作
class Common_Step(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def Open_expert_mode(self):
        """连接打开专家模式"""
        pass


    @abstractmethod
    def enter_CLI_mode(self):
        """进入cli模式，并且获取diff"""
        pass

    @abstractmethod
    def end_break(self):
        """断开飞控连接，并且结束driver"""
        pass


class Android_Common_Step(Common_Step):
    """小米手机的通用步骤"""

    def Open_expert_mode(self):
        """进入专家模式"""
        actions = {
            "Open_expert_mode": {
                "default": [
                    {"action": "click", "appby": "ID", "ele": "com.runcam.android.runcambf:id/mCheckBox", "cond": "el",
                     "comment": "同意隐私政策"},
                    {"action": "click", "appby": "ID", "ele": "com.runcam.android.runcambf:id/AgreeBtn", "cond": "el",
                     "comment": "点击同意"},
                    {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@content-desc='开始使用']",
                     "cond": "el", "comment": "点击开始使用"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.FrameLayout[@resource-id='com.runcam.android.runcambf:id/start_layout']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]",
                     "cond": "el", "comment": "点击＋号搜索设备"},
                    # {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@text='本次使用允许']",
                    #  "cond": "el", "comment": "同意定位"},
                    {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@text='始终允许']",
                     "cond": "el", "comment": "同意"},
                    {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@content-desc='立即连接']",
                     "cond": "el", "comment": "点击立即连接"},
                    {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@content-desc='跳过']",
                     "cond": "el", "comment": "跳过密码"},
                    {"action": "time", "duration": 5, "comment": "因为了解缓慢，所以等待5秒"},
                    # {
                    #     "action": "tap",
                    #     "x_proportion": 0.8754098,
                    #     "y_proportion": 0.9188134,
                    #     "comment": "点击屏幕中间小蒙层提示LED"
                    # },
                    {"action": "click", "appby": "XPATH", "ele": "//android.widget.Button[@content-desc='专家模式']",
                     "cond": "el", "comment": "点击专家模式"},
                    {"action": "time", "duration": 2, "comment": "等待2秒"}
                ]
            }
        }
        # 调用 execute_actions_from_json 方法，并传入动作数据和其它参数
        execute_actions(actions, self.driver, act_name="Open_expert_mode", group="default")

    def  end_break(self):
        """断开飞控连接，并且结束driver"""
        actions = {
            "end_break": {
                "default": [
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/disconnect_btn']",
                     "cond": "el", "comment": "点击断开连接"},
                    {"action": "time", "duration": 5,"comment": "等待5秒"}
                ]
            }
        }
        execute_actions(actions, self.driver, act_name="end_break", group="default")
        self.driver.quit()

    def enter_CLI_mode(self):
        """获取diff文件"""
        actions = {
            "enter_CLI_mode": {
                "default": [
                    {"action": "rolling", "start_locator_type": "XPATH",
                     "start_locator": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/battery_icon']",
                     "end_locator_type": "XPATH",
                     "end_locator": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/configuration_icon']",
                     "cond": "el", "comment": "滑动到页面最底部"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/cli_icon']",
                     "cond": "el", "comment": "点击CLI页面"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/cli_icon']",
                     "cond": "el", "comment": "因为CLI页面还有BUG，需要进入两次"},
                    {"action": "sendkeys", "appby": "XPATH",
                     "ele": "//android.widget.AutoCompleteTextView[@resource-id='com.runcam.android.runcambf:id/send_content']",
                     "keys": "diff", "cond": "el", "comment": "输入diff命令"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.TextView[@resource-id='com.runcam.android.runcambf:id/send_btn']",
                     "cond": "el", "comment": "点击发送"},
                    {"action": "time", "duration": 1, "comment": "等待1秒"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/copy_btn']",
                     "cond": "el", "comment": "点击复制按钮——复制到剪切板存放"},
                    {"action": "sendkeys", "appby": "XPATH",
                     "ele": "//android.widget.AutoCompleteTextView[@resource-id='com.runcam.android.runcambf:id/send_content']",
                     "keys": "defaults", "cond": "el", "comment": "输入defaults命令"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.TextView[@resource-id='com.runcam.android.runcambf:id/send_btn']",
                     "cond": "el", "comment": "点击发送"},
                    {"action": "rolling", "start_locator_type": "XPATH",
                     "start_locator": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/configuration_icon']",
                     "end_locator_type": "XPATH",
                     "end_locator": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/battery_icon']",
                     "cond": "el", "comment": "滑动到页面最顶部"},
                    {"action": "click", "appby": "XPATH",
                     "ele": "//android.widget.ImageView[@resource-id='com.runcam.android.runcambf:id/setup_icon']",
                     "cond": "el", "comment": "点击设置页面——主要是为了退出飞控的CLI页面"},
                    {"action": "time", "duration": 2, "comment": "等待2秒"}
                ]
            }
        }
        execute_actions(actions, self.driver, act_name="enter_CLI_mode", group="default")
