import unittest
from Approach.Common_step import Android_Common_Step
from Approach.Get_Driver.AppDriverBase import AndroidAppDriver


class MyUnit(unittest.TestCase):
    setUp_count = 0
    driver = None
    android_steps = None  # 用于保存 Android_Common_Step 实例

    @classmethod
    def setUpClass(cls):
        """setUpClass开始"""
        if cls.driver is None:
            # 确保只有在第一次需要时才初始化 driver
            cls.driver = AndroidAppDriver.get_driver(version="14")
            # 实例化 Android_Common_Step，只需做一次初始化
            cls.android_steps = Android_Common_Step(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """tearDownClass结束"""
        pass

    def setUp(self):
        # 打印当前执行的子类名称和方法名称
        MyUnit.setUp_count += 1
        print(f"第 {MyUnit.setUp_count} 次测试用例已开始：—————————————— {self.__class__.__name__}.{self._testMethodName}——————————————————————")

    def tearDown(self):
        # 你可以在这里做一些清理工作，比如重置状态等
        pass
