import os
from Approach.Tool.TestReportGenerator import TestReportGenerator

# 使用示例
if __name__ == '__main__':
    # 获取当前脚本（Run_BF.py）的路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 指定需要运行的测试文件列表
    # test_files = ["test_bf_01Setup.py"]
    test_files = ["test_Bee25.py"]
    # 创建 TestReportGenerator 实例，并传入测试目录和测试文件列表
    report_generator = TestReportGenerator(test_case_dir=os.path.join(base_dir, "./Flight_settings"), test_files=test_files)
    # 生成测试报告
    report_generator.generate_report()
