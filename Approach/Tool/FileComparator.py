import re
import os

import os
import re

class FileComparator:
    @staticmethod
    def extract_relevant_content(file_content):
        """
        提取文件中从 `# start the command batch` 到 `batch end` 的内容，并移除多余换行符。

        :param file_content: str, 文件的完整内容
        :return: str, 提取的相关内容（去除了多余的换行符和空格）
        """
        # 使用正则表达式，匹配从 `# start the command batch` 到 `batch end` 之间的内容
        # re.DOTALL 表示可以跨行匹配
        match = re.search(r"# start the command batch(.*?)batch end", file_content, re.DOTALL)
        if match:
            # 如果匹配成功，提取括号内的内容（即 relevant_content）
            relevant_content = match.group(1)
            # 使用正则表达式去掉多余的换行符和空格，将所有内容拼接在一起
            return re.sub(r"\s+", "", relevant_content)
        # 如果未匹配到相关内容，则返回空字符串
        return ""

    @staticmethod
    def compare_files(file1_path, file2_path):
        """
        比较两个文件中从 `# start the command batch` 到 `batch end` 的内容是否一致。

        :param file1_path: str, 第一个文件的路径
        :param file2_path: str, 第二个文件的路径
        :return: tuple, (是否一致, 第一个文件的相关内容, 第二个文件的相关内容)
        """
        # 检查两个文件路径是否存在，如果任何一个不存在则抛出 FileNotFoundError 异常
        if not os.path.exists(file1_path) or not os.path.exists(file2_path):
            raise FileNotFoundError("One or both files do not exist.")

        # 打开第一个文件并读取其内容
        with open(file1_path, "r", encoding="utf-8") as f1:
            file1_content = f1.read()
        # 打开第二个文件并读取其内容
        with open(file2_path, "r", encoding="utf-8") as f2:
            file2_content = f2.read()

        # 提取两个文件中从 `# start the command batch` 到 `batch end` 的相关内容
        content1 = FileComparator.extract_relevant_content(file1_content)
        content2 = FileComparator.extract_relevant_content(file2_content)

        # 返回比较结果，以及两个文件的相关内容
        # 如果内容一致，返回 True；否则返回 False
        return content1 == content2, content1, content2


"""
from FileComparator import FileComparator

# 定义两个文件的路径
file1_path = "APP_Result/result/F405_AIO/Android_result/test_bf_Setup_Setting01.txt"
file2_path = "APP_Result/result/F405_AIO/Win_result/WIN_test_bf_Setup_Setting01.txt"

# 调用 compare_files 方法进行比较
are_equal= FileComparator.compare_files(file1_path, file2_path)

# 打印比较结果
if are_equal:
    print("两个文件的相关内容一致！")
else:
    print("两个文件的相关内容不一致！")
    print(f"文件 1 的内容：\n{content1}")
    print(f"文件 2 的内容：\n{content2}")
"""
