import unittest

from Approach.Common_step import Android_Common_Step
from Approach.Get_Driver.AppDriverBase import AndroidAppDriver


class MyUnit(unittest.TestCase):

    setUp_count = 0
    # 使用类变量来存储 driver 实例
    driver = None

    @classmethod
    def setUpClass(cls):
        '''setUpClass开始'''
        # 在 setUpClass 中初始化 driver 只执行一次
        if cls.driver is None:
            # 假设你在这里传入版本号，也可以从外部配置传递
            cls.driver = AndroidAppDriver.get_driver(version="12")
            print(f"初始化 Android App Driver：{cls.driver}")
            #实例化通用步骤
            # 实例化 Android_Common_Step 类
            cls.android_steps = Android_Common_Step(cls.driver)

    @classmethod
    def tearDownClass(cls):
        '''tearDownClass结束'''
        # 在 tearDownClass 中关闭 driver 只执行一次
        if cls.driver:
            AndroidAppDriver.quit_driver()  # 调用 quit_driver 来关闭 driver
            cls.driver = None
            print("关闭 Android App Driver")

    def setUp(self):
        # 打印当前执行的子类名称和方法名称
        MyUnit.setUp_count += 1
        print(f"第 {MyUnit.setUp_count} 次测试用例已开始：—————————————— {self.__class__.__name__}.{self._testMethodName}——————————————————————")

    def tearDown(self):
        pass


    """以下是通用的方法"""

    # 打开通用步骤
    def A_Open_expert_mode(self):
        self.android_steps.Open_expert_mode()