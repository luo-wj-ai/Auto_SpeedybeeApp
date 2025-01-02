import os

if __name__ == "__main__":
    # 获取当前工作目录
    print(f"当前工作目录: {os.getcwd()}")

    # 获取当前文件的绝对路径
    print(f"当前文件绝对路径: {os.path.abspath(__file__)}")

    # 获取当前文件的目录路径
    print(f"当前文件目录路径: {os.path.dirname(os.path.abspath(__file__))}")

    # 获取父目录
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    print(f"父目录: {parent_dir}")

    # 拼接路径
    screenshot_dir = os.path.join(parent_dir, "screenshots")
    print(f"截图保存路径: {screenshot_dir}")

    # 创建目录
    os.makedirs(screenshot_dir, exist_ok=True)

    #删除目录
    os.rmdir(screenshot_dir)

    # 检查路径是否存在
    print(f"路径是否存在: {os.path.exists(screenshot_dir)}")

    # 标准化路径
    normalized_path = os.path.normpath("../screenshots/./example.png")
    print(f"标准化路径: {normalized_path}")

    # 分离文件名和扩展名
    file_name, file_ext = os.path.splitext("example.png")
    print(f"文件名: {file_name}, 扩展名: {file_ext}")

    # 获取相对路径
    relative_path = os.path.relpath(screenshot_dir, parent_dir)
    print(f"相对路径: {relative_path}")
