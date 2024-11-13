import unittest
import os
from BeautifulReport import BeautifulReport

def generate_report(suite):
    # 打印测试用例集合的大小
    print(f"测试用例集合: {suite.countTestCases()}")

    # 打印每个测试用例的名称，确认加载的方法
    for case in suite:
        print(f"加载测试用例： {case}")

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

if __name__ == '__main__':
    # 获取当前脚本（Run_BF.py）的路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 使用相对路径，定位到 BF 文件夹
    test_dir = os.path.join(base_dir, "BF")

    # 检查路径是否正确
    print(f"测试目录路径: {test_dir}")

    # 加载指定目录下的所有测试用例
    suite = unittest.defaultTestLoader.discover(test_dir, pattern="test_*py")

    # 生成报告
    generate_report(suite)
