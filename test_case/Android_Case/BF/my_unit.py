import time
from Approach.Control_Ele import execute_actions
from Approach.Tool.Get_Json_Path import get_json_path
import unittest
from Approach.Common_step import Android_Common_Step
from Approach.Get_Driver.AppDriverBase import AndroidAppDriver
from Approach.Tool.Cliapp import cliapp
from Approach.Tool.FileComparator import FileComparator

# 测试报告路径
result_dir = "APP_Result/result/F405_AIO/Android_result"
# 测试数据路径
JSON_dir = "Element/F405_AIO/Android_Ele/BF"

class MyUnit(unittest.TestCase):
    setUp_count = 0       # 每次执行用例的计数器
    driver = None         # 用于保存 Android 驱动实例
    android_steps = None  # 用于保存 Android_Common_Step 实例
    close_driver = False  # 控制是否关闭 driver
    use_contains_assert = True  # 默认为 True，表示使用 compare_files 方法进行文件比较
    sequence_to_check = "*"  # 全局变量，存储待检查的字符串

    @staticmethod
    def execute_actions(json_path, driver, act_name, group):
        """
        执行动作：根据 JSON 配置文件执行操作
        - json_path: JSON 文件路径
        - driver: Android 驱动实例
        - act_name: 动作名称
        - group: 动作组
        """
        my_json_path = get_json_path(json_path, JSON_dir)
        execute_actions(my_json_path, driver, act_name, group)

    @staticmethod
    def assert_compare_files_logic(cli_file_path, win_cli_file_path, use_contains_assert, sequence_to_check):
        """
        文件比较逻辑：
        - 根据 `use_contains_assert` 决定使用哪种方法进行文件比较
        - 当为 True 时，使用 compare_files 比较文件内容
        - 否则，使用 contains_sequence 检查文件是否包含特定内容
        """
        if use_contains_assert:
            # 使用 compare_files 比较文件内容
            are_equal, content1, content2 = FileComparator.compare_files(cli_file_path, win_cli_file_path)

            # 使用断言判断文件内容是否一致
            assert are_equal, f"文件内容不匹配！\n文件1内容：\n{content1}\n文件2内容：\n{content2}"
            print(f"文件内容匹配成功：{cli_file_path} 与 {win_cli_file_path}")
        else:
            # 使用 contains_sequence 检查文件内容
            is_present = FileComparator.contains_sequence(cli_file_path, sequence_to_check)

            # 使用断言判断文件是否包含指定字符串
            assert is_present, f"文件 {cli_file_path} 不包含指定字符串：{sequence_to_check}"
            print(f"文件 {cli_file_path} 包含指定字符串：{sequence_to_check}")


    @classmethod
    def setUpClass(cls):
        """
        setUpClass：用于在所有测试用例执行之前的初始化操作
        - 初始化 Android 驱动实例（只执行一次）
        - 打开专家模式（只执行一次）
        """
        if cls.driver is None:
            # 初始化 Android 驱动
            cls.driver = AndroidAppDriver.get_driver(version="14")

            # 实例化 Android_Common_Step，只需执行一次
            cls.android_steps = Android_Common_Step(cls.driver)

            # 打开专家模式
            cls.android_steps.Open_expert_mode()

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass：用于在所有测试用例执行之后的清理操作
        - 关闭 driver 并清除资源（可选，受 close_driver 控制）
        """
        if cls.close_driver and cls.driver is not None:
            print("正在关闭 driver...")
            cls.android_steps.end_break()  # 执行关闭操作
            cls.driver = None  # 清除 driver 引用
        else:
            print("未关闭 driver")

    def setUp(self):
        """
        setUp：每次测试用例执行之前的初始化操作
        - 打印当前用例的执行信息
        - 增加执行计数器
        """
        MyUnit.setUp_count += 1
        print(f"第 {MyUnit.setUp_count} 次测试用例已开始：—————————————— {self.__class__.__name__}.{self._testMethodName}——————————————————————")

    def tearDown(self):
        """
        tearDown：每次测试用例执行之后的清理操作
        - 进入 CLI 模式
        - 执行文件比较逻辑（封装的 assert_compare_files_logic 方法）
        """
        time.sleep(4)  # 强制等待，确保上一个保存操作完成

        # 进入 CLI 模式
        self.android_steps.enter_CLI_mode()

        # 获取剪切板数据并生成文件路径
        cli_file_path, win_cli_file_path = cliapp(self.driver, self._testMethodName, result_dir)

        # 调用文件比较逻辑进行断言
        self.assert_compare_files_logic(cli_file_path, win_cli_file_path, self.use_contains_assert, self.sequence_to_check)
        self.use_contains_assert=True #如果use_contains_assert为False，就重新赋值


"""
子类关闭方法示例：
    @classmethod
    def tearDownClass(cls):
        cls.close_driver = True  # 设置标记位以关闭 driver
        super().tearDownClass()  # 调用父类的 tearDownClass
"""
