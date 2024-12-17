import os
import re
import time
import json
import logging
from datetime import datetime
import coloredlogs
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as Ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 配置彩色日志
coloredlogs.install(level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def parse_json(json_file, act_name=None, group=None):
    """解析 JSON 文件，按动作名和组返回数据"""
    try:
        with open(json_file, "r", encoding="utf-8") as file:  # 强制使用 UTF-8 编码
            data = json.load(file)
        if act_name:
            data = data.get(act_name, {})
        return data.get(group, []) if group else data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error reading JSON file: {json_file} - {e}")
        return {}



class AppiumHelper:
    """封装 Appium 常用操作"""

    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.locators = {
            'ID': AppiumBy.ID,
            'XPATH': AppiumBy.XPATH,
            'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
            'ANDROID_UIAUTOMATOR': AppiumBy.ANDROID_UIAUTOMATOR,
            'NAME': AppiumBy.NAME
        }
        self.conditions = {
            'el': Ec.presence_of_element_located,
            'etbc': Ec.element_to_be_clickable,
            'ioe': Ec.invisibility_of_element_located,
            'eltbs': Ec.element_located_to_be_selected,
            'voel': Ec.visibility_of_element_located
        }

    def _log_error(self, msg, exception=None):
        """统一错误日志"""
        logging.error(msg)
        if exception:
            logging.exception(exception)

    def _get_condition_and_locator(self, appby, cond, ele):
        """校验并返回条件和定位器"""
        condition = self.conditions.get(cond)
        locator = self.locators.get(appby)
        if not condition or not locator:
            raise ValueError(f"Invalid locator or condition: {appby}, {cond}")
        return condition, locator, ele

    def perform_action(self, action, **kwargs):
        """
        执行单一动作
        """
        actions = {
            'click': self._click,
            'sendkeys': self._send_keys,
            'clear': self._clear,
            'time': self._sleep,
            'tap': self._tap,
            'swipe': self._swipe,
            'rolling': self._rolling,
        }
        try:
            method = actions.get(action)
            if not method:
                logging.warning(f"Unsupported action: {action}. Skipping.")
                return False
            return method(**kwargs)
        except Exception as e:
            self._log_error(f"Error executing action {action}", e)
            return False

    def _click(self, appby, cond, ele, comment=""):
        """点击操作"""
        element = self._wait_and_get_element(appby, cond, ele)
        if element:
            element.click()
            logging.info(f"Clicked element: {ele} - {comment}")
            return True
        return False

    def _send_keys(self, appby, cond, ele, keys, comment=""):
        """发送键值操作"""
        element = self._wait_and_get_element(appby, cond, ele)
        if element:
            element.send_keys(str(keys))
            logging.info(f"Sent keys to element: {ele} - {comment}")
            return True
        return False

    def _clear(self, appby, cond, ele, comment=""):
        """清除元素内容"""
        element = self._wait_and_get_element(appby, cond, ele)
        if element:
            element.clear()
            logging.info(f"Cleared element: {ele} - {comment}")
            return True
        return False

    def _sleep(self, duration, comment=""):
        """休眠操作"""
        logging.info(f"Sleeping for {duration} seconds - {comment}")
        time.sleep(duration)
        return True

    def _tap(self, x_proportion, y_proportion, comment=""):
        """屏幕点击操作，支持打印屏幕比例和实际坐标"""
        # 获取屏幕尺寸
        size = self.driver.get_window_size()
        width, height = size['width'], size['height']

        # 计算点击的实际坐标
        x, y = int(width * x_proportion), int(height * y_proportion)

        # 执行点击操作
        self.driver.tap([(x, y)])
        # 打印屏幕尺寸、点击比例和实际坐标
        logging.info(f"Screen size: width={width}, height={height}")
        logging.info(f"Tapped at position: (x={x}, y={y}) - {comment}")
        return True

    def _swipe(self, start_x_proportion, start_y_proportion, end_x_proportion, end_y_proportion, duration=100,
               comment=""):
        """屏幕滑动操作，支持按屏幕比例计算坐标"""
        # 获取屏幕尺寸
        size = self.driver.get_window_size()
        width, height = size['width'], size['height']

        # 计算滑动的实际坐标
        start_x = int(width * start_x_proportion)
        start_y = int(height * start_y_proportion)
        end_x = int(width * end_x_proportion)
        end_y = int(height * end_y_proportion)

        # 执行滑动操作
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

        # 打印屏幕尺寸、滑动比例和实际坐标
        logging.info(f"Screen size: width={width}, height={height}")
        logging.info(f"Swiped from ({start_x}, {start_y}) to ({end_x}, {end_y}) - {comment}")
        return True

    def _rolling(self, start_locator_type, start_locator, end_locator_type, end_locator, cond, comment=""):
        """
        滚动操作，从起始元素滚动到终止元素。

        参数：
            start_locator_type (str)：起始元素的定位器类型，例如 "XPATH"。
            start_locator (str)：起始元素的定位表达式。
            end_locator_type (str)：终止元素的定位器类型。
            end_locator (str)：终止元素的定位表达式。
            cond (str)：等待条件，例如 "el"。
            comment (str)：动作备注信息。
        """
        try:
            # 获取起点和终点元素
            start_element = self._wait_and_get_element(start_locator_type, cond, start_locator)
            end_element = self._wait_and_get_element(end_locator_type, cond, end_locator)

            if start_element and end_element:
                # 使用滚动方法
                self.driver.scroll(start_element, end_element)
                logging.info(f"Rolled from {start_locator} to {end_locator} - {comment}")
                return True
            else:
                logging.error(f"Rolling failed: Could not find start or end element - {comment}")
                return False
        except Exception as e:
            self._log_error(f"Error during rolling - {comment}", e)
            return False



    def save_element_screenshot(self, ele, folder="screenshots"):
        """
        保存未捕获元素的截图

        参数:
        - ele: 未捕获的元素名称，用于命名截图
        - folder: 保存截图的文件夹路径，相对于当前文件目录的上一层目录

        返回:
        - 截图保存的完整路径
        """
        # 获取当前文件目录的上一层目录
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # 拼接截图保存的文件夹路径
        screenshot_dir = os.path.join(parent_dir, folder)
        os.makedirs(screenshot_dir, exist_ok=True)  # 如果文件夹不存在则创建

        # 构造时间戳和安全的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sanitized_ele = re.sub(r'[\\/:*?"<>|]', '_', ele)[:50]  # 替换非法字符并限制长度
        file_name = f"{timestamp}_{sanitized_ele}_未捕获.png"

        # 拼接完整路径
        screenshot_path = os.path.join(screenshot_dir, file_name)

        # 保存截图
        try:
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            logging.error(f"Failed to save screenshot: {e}")

        return screenshot_path

    def _wait_and_get_element(self, appby, cond, ele):
        """通用元素获取方法，支持失败时截图"""
        try:
            # 获取条件和定位器
            condition, locator, ele = self._get_condition_and_locator(appby, cond, ele)
            self.wait.until(condition((locator, ele)))
            return self.driver.find_element(locator, ele)
        except (NoSuchElementException, TimeoutException) as e:
            # 记录错误日志
            self._log_error(f"Element not found: {ele}", e)

            # 调用独立的截图方法
            self.save_element_screenshot(ele)

            return None


def execute_actions(json_data_or_file, driver, act_name, group="default", testcase=None):
    """
    从 JSON 数据或 JSON 文件中解析并执行指定的动作序列。

    参数：
        json_data_or_file (str 或 dict)：可以是 JSON 文件路径，也可以是已经解析的 JSON 数据。
        driver (WebDriver)：Appium 的 WebDriver 实例，用于执行动作。
        act_name (str)：指定的动作组名称。
        group (str)：指定子组名称，默认为 "default"。
        testcase (unittest.TestCase)：unittest 测试实例，用于在失败时调用 fail()（可选）。

    返回：
        None
    """
    # 判断传入的是 JSON 文件路径还是已经解析的 JSON 数据
    if isinstance(json_data_or_file, str):  # 如果是文件路径
        logging.info(f"Loading JSON file: {json_data_or_file}")
        # 解析 JSON 文件，根据指定的动作组和组名提取数据
        json_data = parse_json(json_data_or_file, act_name=act_name, group=group)
    else:  # 如果是已经解析的 JSON 数据
        logging.info("Using provided JSON data")
        # 从 JSON 数据中获取指定动作组和子组的动作列表
        json_data = json_data_or_file.get(act_name, {}).get(group, [])

    if not json_data:
        error_msg = f"No actions found for group {group} in {act_name}"
        logging.error(error_msg)
        if testcase:  # 如果传递了 testcase，则调用 fail()
            testcase.fail(error_msg)
        return

    # 初始化 AppiumHelper 工具类，用于封装常用的 Appium 操作
    helper = AppiumHelper(driver)

    valid_keys = {
        "action",  # 动作类型
        "appby",  # 定位器类型
        "cond",  # 等待条件
        "ele",  # 定位器值
        "keys",  # 输入框中的文本
        "duration",  # 持续时间
        "x_proportion", "y_proportion",  # 点击位置的比例
        "start_x_proportion", "start_y_proportion",  # 滑动起点比例
        "end_x_proportion", "end_y_proportion",  # 滑动终点比例
        "start_locator_type",  # 滚动起点的定位器类型
        "start_locator",  # 滚动起点的定位器值
        "end_locator_type",  # 滚动终点的定位器类型
        "end_locator",  # 滚动终点的定位器值
        "comment"  # 动作备注
    }

    # 遍历 JSON 数据中的每个动作
    for action in json_data:
        # 过滤掉动作中无效的字段，只保留有效的键值对
        filtered_action = {k: v for k, v in action.items() if k in valid_keys}

        try:
            # 调用 AppiumHelper 的方法执行动作
            if not helper.perform_action(**filtered_action):
                error_msg = f"Action {action.get('action')} failed: {action.get('comment', '')}"
                logging.error(error_msg)
                if testcase:  # 如果传递了 testcase，则调用 fail()
                    testcase.fail(error_msg)
                break
        except Exception as e:
            # 捕获异常，记录日志并标记测试失败
            error_msg = f"Exception during action execution: {e}"
            logging.error(error_msg)
            if testcase:  # 如果传递了 testcase，则调用 fail()
                testcase.fail(error_msg)
            break



