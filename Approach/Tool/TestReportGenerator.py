import time
import unittest
import os
from BeautifulReport import BeautifulReport
import pyfiglet


class TestReportGenerator:
    def __init__(self, test_case_dir, test_files):
        """
        :param test_case_dir: 测试用例的目录
        :param test_files: 需要加载的测试用例文件列表
        """
        self.test_case_dir = test_case_dir
        self.test_files = test_files
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.report_dir = os.path.join(self.project_root, "APP_Result/report")

    def print_test_cases(self, suite):
        """递归打印测试用例名称"""
        for case in suite:
            if isinstance(case, unittest.TestCase):
                print(f"加载测试用例： {case.__class__.__name__}.{case._testMethodName}")
            elif isinstance(case, unittest.TestSuite):
                self.print_test_cases(case)  # 递归调用

    def print_test_report(self):
        """打印测试报告艺术字"""
        # 生成ASCII Art 字符
        ascii_art = pyfiglet.figlet_format("Test Report", font="slant")
        print(ascii_art)
        msg = r"""
                           _ooOoo_
                          o8888888o
                          88" . "88
                          (| -_- |)
                           O\ = /O
                       ____/`---'\____
                     .   ' \\| |// `.
                      / \\||| : |||// \
                    / _||||| -:- |||||- \
                      | | \\\ - /// | |
                    | \_| ''\---/'' | |
                     \ .-\__ `-` ___/-. /
                  ___`. .' /--.--\ `. . __
               ."" '< `.___\_<|>_/___.' >'"".
              | | : `- \`.;`\ _ /`;.`/ - ` : | |
                \ \ `-. \_ __\ /__ _/ .-` / /
        ======`-.____`-.___\_____/___.-`____.-'======
                           `=---='

        .............................................
               佛祖保佑             永无BUG
        .............................................
            佛曰:
            写字楼里写字间          写字间里程序员；
            程序人员写程序          又拿程序换酒钱。
            酒醒只在网上坐          酒醉还来网下眠； 
            酒醉酒醒日复日          网上网下年复年。
            但愿老死电脑间          不愿鞠躬老板前；
            奔驰宝马贵者趣          公交自行程序员。
            别人笑我忒疯癫          我笑自己命太贱；
            不见满街漂亮妹          哪个归得程序员？
        """

        print(msg)
        pass

    def generate_report(self):
        """加载测试用例并生成测试报告"""
        # 初始化测试套件
        suite = unittest.TestSuite()

        # 遍历指定的测试文件并逐一加载
        for test_file in self.test_files:
            # 只加载指定的文件
            file_suite = unittest.defaultTestLoader.discover(self.test_case_dir, pattern=test_file)
            suite.addTests(file_suite)

        # 打印测试用例集合的大小
        print(f"测试用例集合: {suite.countTestCases()}")

        # 打印每个测试用例的名称
        self.print_test_cases(suite)

        # 获取当前时间并格式化为字符串
        now_time = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
        filename = now_time + "TestReport.html"  # 测试报告文件名

        # 创建报告目录（如果不存在）
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        print(f"报告文件名： {filename}")
        print(f"报告存储路径： {self.report_dir}")
        #打印艺术字
        # self.print_test_report()

        # 生成 BeautifulReport 测试报告
        try:
            treport = BeautifulReport(suite)
            treport.report(description="测试报告", filename=filename, report_dir=self.report_dir)
            print("测试报告生成成功")
        except Exception as e:
            print(f"生成测试报告时发生错误: {e}")


"""
# 使用示例
if __name__ == '__main__':
    # 获取当前脚本（Run_BF.py）的路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 指定需要运行的测试文件列表
    test_files = ["test_bf_01_Setup.py", "test_INAV_01_Setup.py"]
    # 创建 TestReportGenerator 实例，并传入测试目录和测试文件列表
    report_generator = TestReportGenerator(test_case_dir=os.path.join(base_dir, "BF"), test_files=test_files)
    # 生成测试报告
    report_generator.generate_report()
"""

