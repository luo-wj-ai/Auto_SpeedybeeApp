import os

def get_json_path(json_name, js_result_dir="Element/F405_AIO/Android_Ele/BF"):
    """
    获取 JSON 文件的完整路径
    - json_name: JSON 文件名
    - js_result_dir: JSON 文件所在的相对目录
    """

    # 获取项目根目录
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    # print(f"项目根目录: {project_root}")  # 打印项目根目录

    # 构造 JSON 结果文件路径
    result_path = os.path.join(project_root, js_result_dir)
    # print(f"目标目录路径: {result_path}")  # 打印 JSON 文件所在目录路径

    # 若目录不存在则创建
    os.makedirs(result_path, exist_ok=True)

    # 构造 JSON 文件的完整路径
    cli_file_path = os.path.join(result_path, json_name)
    print(f"JSON 文件路径: {cli_file_path}")  # 打印 JSON 文件路径

    return cli_file_path
