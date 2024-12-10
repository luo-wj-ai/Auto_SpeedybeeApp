import os
import re


class FileComparator:

    # def extract_relevant_content(file_content):
    #     """
    #     提取文件中从 `# start the command batch` 到 `batch end` 的内容，并移除多余的换行符。
    #     :param file_content: str, 文件的完整内容
    #     :return: str, 提取的相关内容
    #     """
    #     # 使用正则表达式匹配文件内容中的相关部分
    #     match = re.search(r"#\s*feature(.*?)\s*batch\s*end", file_content, re.DOTALL)
    #     if match:
    #         # 打印匹配到的内容进行调试
    #         # print(f"匹配到的内容: {match.group(1)}")
    #         # 返回提取的内容，移除多余的空白字符
    #         return re.sub(r"\s+", "", match.group(1))  # 移除所有空白字符
    #     return ""  # 如果没有找到相关内容，返回空字符串
    @staticmethod
    def extract_relevant_content(file_content):
        """
        提取文件中从 `# start the command batch` 到 `batch end` 的内容，
        并移除所有以 `feature` 开头的行，然后移除多余的换行符。
        :param file_content: str, 文件的完整内容
        :return: str, 提取的相关内容
        """
        # 使用正则表达式匹配文件内容中的相关部分
        match = re.search(r"#\s*feature(.*?)\s*batch\s*end", file_content, re.DOTALL)
        if match:
            # 提取匹配的部分
            content = match.group(1)

            # 删除所有以 'feature' 开头的行
            content = re.sub(r"^feature.*\n", "", content, flags=re.MULTILINE)

            # 移除多余的空白字符
            return re.sub(r"\s+", "", content)

        return ""  # 如果没有找到相关内容，返回空字符串

    # 判断两个文件是否相等
    @staticmethod
    def compare_files(file1_path, file2_path):
        """
        比较两个文件中从 `# start the command batch` 到 `batch end` 的内容是否一致。
        :param file1_path: str, 第一个文件的路径
        :param file2_path: str, 第二个文件的路径
        :return: tuple, (是否一致, 文件1的相关内容, 文件2的相关内容)
        """
        # 检查文件是否存在
        if not os.path.exists(file1_path) or not os.path.exists(file2_path):
            raise FileNotFoundError("One or both files do not exist.")

        # 读取文件内容
        with open(file1_path, "r", encoding="utf-8") as f1:
            file1_content = f1.read()
        with open(file2_path, "r", encoding="utf-8") as f2:
            file2_content = f2.read()

        # 提取文件中的相关内容
        content1 = FileComparator.extract_relevant_content(file1_content)
        content2 = FileComparator.extract_relevant_content(file2_content)

        # 返回文件内容是否一致，并返回相关内容
        return content1 == content2, content1, content2

    # 判断文件是否包含字符
    @staticmethod
    def contains_sequence(file_path, sequence):
        """
        判断文件中从 `# start the command batch` 到 `batch end` 提取的内容是否包含指定的字符串。
        :param file_path: str, 文件路径
        :param sequence: str, 需要匹配的字符串
        :return: bool, 是否包含该字符串
        """
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        # 读取文件内容
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

        # 提取文件中相关的内容
        relevant_content = FileComparator.extract_relevant_content(file_content)

        # 清除 sequence 中的多余空白字符，确保匹配一致
        sequence = re.sub(r"\s+", "", sequence)

        # 使用 Boyer-Moore 算法进行字符串匹配
        return FileComparator.boyer_moore(relevant_content, sequence)

    @staticmethod
    def boyer_moore(text, pattern):
        """
        Boyer-Moore 字符串匹配算法实现。
        :param text: str, 主串
        :param pattern: str, 模式串
        :return: bool, 是否匹配
        """
        m = len(pattern)
        n = len(text)

        if m == 0:
            return True  # 空模式串视为匹配
        if m > n:
            return False  # 模式串长度大于文本长度，直接不匹配

        # 生成坏字符表
        bad_char = {c: m - i - 1 for i, c in enumerate(pattern[:-1])}
        bad_char_default = m

        # Boyer-Moore 主循环
        shift = 0
        while shift <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[shift + j]:
                j -= 1
            if j < 0:
                return True  # 匹配成功
            # 修正 shift 计算，避免越界错误
            shift += bad_char.get(text[shift + m - 1], bad_char_default) if shift + m - 1 < n else bad_char_default

        return False  # 未匹配成功



"""
relevant_content = FileComparator.extract_relevant_content(file_content)
print(relevant_content)
# 预期输出：This is some relevant content.There are multiple lines here.And some spaces too.

# 示例 2: compare_files 方法
file1_path = "file1.txt"
file2_path = "file2.txt"
are_equal, content1, content2 = FileComparator.compare_files(file1_path, file2_path)
print(f"文件内容是否一致: {are_equal}")
print(f"文件1内容: {content1}")
print(f"文件2内容: {content2}")
# 预期输出：文件内容是否一致: True/False（取决于文件内容）
# 文件1内容和文件2内容

# 示例 3: contains_sequence 方法
file_path = "file.txt"
sequence = "relevant content"
is_present = FileComparator.contains_sequence(file_path, sequence)
print(f"文件是否包含指定字符串: {is_present}")
# 预期输出：文件是否包含指定字符串: True/False（取决于文件内容）

# 示例 4: boyer_moore 方法
text = "This is a sample text"
pattern = "sample"
is_match = FileComparator.boyer_moore(text, pattern)
print(f"模式匹配成功: {is_match}")
# 预期输出：模式匹配成功: True
"""

