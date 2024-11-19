import os
import inspect

def assert_method(driver, test_method_name=None, result_dir="APP_Result/result/F405_AIO/Android_result"):
    """
    从设备剪切板中获取数据并写入指定目录的文件。文件名为调用的测试方法名。

    :param driver: Appium driver 对象
    :param result_dir: 结果存储目录，默认值为 'APP_Result/result/F405_AIO/Android_result'
    :param test_method_name: 调用此方法的测试方法名，若未提供则自动获取
    """
    # 获取剪切板数据
    paste_data = driver.get_clipboard()
    paste_app = str(paste_data)

    # 获取调用此方法的测试方法名（如果未提供）
    if test_method_name is None:
        test_method_name = inspect.stack()[1].function  # 调用的测试方法名

    # 获取项目根目录并构造结果文件路径
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    result_path = os.path.join(project_root, result_dir)
    os.makedirs(result_path, exist_ok=True)  # 若目录不存在则创建

    # 构造文件路径，文件名为测试方法名
    cli_file_path = os.path.join(result_path, f"{test_method_name}.txt")

    # 文本格式化处理
    paste_app = paste_app.replace(r"\r", '\n').replace(r"\n", '\n')

    # 写入剪切板数据到文件（覆盖模式）
    with open(cli_file_path, 'w', encoding='utf-8') as f:
        f.write(paste_app)

    print(f"剪切板数据已写入文件：{cli_file_path}")

    #获取win保存该文件的目录
    win_cli_file_path = cli_file_path.replace("Android_result", "Win_result").replace("iOS_result","Win_result").replace("test_", "WIN_test_")


    return cli_file_path,win_cli_file_path
