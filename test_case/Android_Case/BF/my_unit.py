import unittest
from Approach.Common_step import Android_Common_Step
from Approach.Get_Driver.AppDriverBase import AndroidAppDriver
from Approach.Tool.Cliapp import cliapp
from Approach.Tool.FileComparator import FileComparator

#针对
result_dir="APP_Result/result/F405_AIO/Android_result"

class MyUnit(unittest.TestCase):
    setUp_count = 0       #每一次实现的步骤
    driver = None           #driver
    android_steps = None  # 用于保存 Android_Common_Step 实例
    close_driver = False  # 控制是否关闭 driver
    use_contains_assert = True  # 默认为 False，表示使用 compare_files 进行文件比较
    sequence_to_check = "*"  # 全局变量，存储待检查的字符串


    #用于只启动一次drive，只进入一次专家模式
    @classmethod
    def setUpClass(cls):
        """setUpClass开始"""
        if cls.driver is None:
            # 确保只有在第一次需要时才初始化 driver
            cls.driver = AndroidAppDriver.get_driver(version="14")
            # 实例化 Android_Common_Step，只需做一次初始化
            cls.android_steps = Android_Common_Step(cls.driver)
            #只进入一次专家模式
            cls.android_steps.Open_expert_mode()
        pass

    #用于标记位，断开飞控，关闭driver
    @classmethod
    def tearDownClass(cls):
        """tearDownClass结束"""
        if cls.close_driver and cls.driver is not None:
            print("正在关闭 driver...")
            cls.android_steps.end_break() # 关闭 driver
            cls.driver = None  # 清除 driver 引用
        else:
            print("未关闭 driver")
        pass


    #用于控制每一次用例的执行的标记
    def setUp(self):
        # 打印当前执行的子类名称和方法名称
        MyUnit.setUp_count += 1
        print(f"第 {MyUnit.setUp_count} 次测试用例已开始：—————————————— {self.__class__.__name__}.{self._testMethodName}——————————————————————")
        pass


    #用于控制部分用例——获取diff数据进行对比——并进行断言
    def tearDown(self):
        """
        测试结束后，根据布尔值选择文件比较方法：
        - use_contains_sequence 为 True 时，使用 contains_sequence 方法检查文件是否包含指定内容；
        - 否则，使用 compare_files 方法进行文件内容比较。
        """
        # 进入 CLI 模式
        self.android_steps.enter_CLI_mode()

        # 获取剪切板数据并生成文件路径
        cli_file_path, win_cli_file_path = cliapp(self.driver, self._testMethodName, result_dir)

        if self.use_contains_assert:
            # 使用 compare_files 比较文件内容
            are_equal, content1, content2 = FileComparator.compare_files(cli_file_path, win_cli_file_path)

            # 使用 unittest 的断言
            self.assertTrue(are_equal, f"文件内容不匹配！\n文件1内容：\n{content1}\n文件2内容：\n{content2}")

            # 打印比较结果
            if are_equal:
                print(f"文件内容匹配成功：{cli_file_path} 与 {win_cli_file_path}")

        else:
            # 使用 contains_sequence 判断文件内容是否包含特定字符串
            is_present = FileComparator.contains_sequence(cli_file_path, self.sequence_to_check)
            # 使用 unittest 的断言
            self.assertTrue(is_present, f"文件 {cli_file_path} 不包含指定字符串：{self.sequence_to_check}")
            print(f"文件 {cli_file_path} 包含指定字符串：{self.sequence_to_check}")

            self.use_contains_assert = True   #回到原始判断


"""
子类关闭方法：
    @classmethod
    def tearDownClass(cls):
        cls.close_driver=True
        super().tearDownClass()
        pass
"""