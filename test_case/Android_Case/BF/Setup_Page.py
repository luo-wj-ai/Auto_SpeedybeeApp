import unittest
import os
from BeautifulReport import BeautifulReport
from Approach.AppDriverBase import AndroidAppDriver
from Approach.Common_step import Android_Common_Step

def generate_report(testcasename):
    print(f"正在运行 {testcasename.__name__} 的测试用例")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(testcasename)

    # 打印 suite 确认它是否正确加载
    print(f"测试用例集合: {suite.countTestCases()}")
    # 打印每个测试用例的名称，确认加载的方法
    for case in suite:
        print(f"加载测试用例： {case.id()}")

    # 报告文件名和路径
    filename = "TestReport.html"  # 测试报告文件名
    report_path = os.path.dirname(os.path.abspath(__file__))  # 使用当前文件所在的路径作为报告存储路径
    print(f"报告文件名： {filename}")
    print(f"报告存储路径： {report_path}")

    # 生成 BeautifulReport 测试报告
    try:
        treport = BeautifulReport(suite)
        treport.report(description="测试报告", filename=filename, report_dir=report_path)
        print("测试报告生成成功")
    except Exception as e:
        print(f"生成测试报告时发生错误: {e}")

class Setup_Page(unittest.TestCase):
    def setUp(self):
        '''初始化操作'''
        self.driver = AndroidAppDriver(version="14").get_driver()
        self.c_android = Android_Common_Step(self.driver)
        pass

    def test_Setup_Setting1(self):
        '''基本设置页操作'''
        self.fail(f"Test failed due to error: ")  # 强制使测试失败
        self.c_android.Open_expert_mode()
        pass

    def test_Setup_Setting2(self):
        '''基本设置页操作'''
        self.c_android.Open_expert_mode()
        pass

    def tearDown(self):
        '''关闭操作'''
        self.driver.quit()
        print("_______________完成一次测试用例执行_______________\n")
        pass

if __name__ == '__main__':
    generate_report(Setup_Page)
