import os


def get_json_path(json_name,js_result_dir="Element/F405_AIO/Android_Ele/BF"):


    # 获取项目根目录并构造结果文件路径
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    result_path = os.path.join(project_root, js_result_dir)
    os.makedirs(result_path, exist_ok=True)  # 若目录不存在则创建


    # 构造文件路径，文件名为测试方法名
    cli_file_path = os.path.join(result_path, json_name)


    return cli_file_path



