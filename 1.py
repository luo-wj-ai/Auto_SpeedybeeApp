import unittest
import time
import os
from BeautifulReport import BeautifulReport


class SimpleTest(unittest.TestCase):

    def test_success(self):
        """简单的成功测试用例"""
        self.assertEqual(1 + 1, 2)

    def test_failure(self):
        """简单的失败测试用例"""
        self.assertEqual(1 + 1, 3)  # 这个会故意失败


if __name__ == "__main__":
    # 获取当前脚本目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_files = ["test_simple.py"]

    # 创建一个测试报告生成器
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)

    # 设置报告文件的路径为当前路径
    report_dir = base_dir
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 生成报告文件
    report_generator = BeautifulReport(suite)
    report_generator.report(description="Simple Test Report", filename="simple_test_report.html", report_dir=report_dir)
    print("报告生成成功！")
