import unittest
from Approach.Tool.Generate_Report import generate_report
from Approach.Get_Driver.AppDriverBase import AndroidAppDriver
from Approach.Common_step import Android_Common_Step



class Setup_Page(unittest.TestCase):
    def setUp(self):
        '''初始化操作'''
        self.driver = AndroidAppDriver(version="14").get_driver()
        self.c_android = Android_Common_Step(self.driver)
        pass

    def test_Setup_Setting1(self):
        '''Setup基本设置页操作01'''
        self.fail(f"Test failed due to error: ")  # 强制使测试失败
        self.c_android.Open_expert_mode()
        pass

    def test_Setup_Setting2(self):
        '''Setup基本设置页操作02'''
        self.c_android.Open_expert_mode()
        pass

    def tearDown(self):
        '''关闭操作'''
        self.driver.quit()

        pass

if __name__ == '__main__':
    generate_report(Setup_Page)
