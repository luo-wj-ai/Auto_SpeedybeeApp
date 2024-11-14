import time
import logging
import coloredlogs
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as Ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 配置彩色日志
coloredlogs.install(level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 捕获元素的方法
class AppiumHelper:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=timeout)

    # 等待元素出现或满足条件,并进行定位
    def ec_get(self, appby, cond, ele):
        locators = {
            'ID': AppiumBy.ID,
            'XPATH': AppiumBy.XPATH,
            'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
            'NAME': AppiumBy.NAME
        }
        conditions = {
            'el': Ec.presence_of_element_located,
            'etbc': Ec.element_to_be_clickable,
            'ioe': Ec.invisibility_of_element_located,
            'eltbs': Ec.element_located_to_be_selected,
            'voel': Ec.visibility_of_element_located
        }

        try:
            condition = conditions.get(cond)
            if condition:
                # 等待直到条件满足
                self.wait.until(condition((locators.get(appby), ele)))
                # 条件满足后，获取并返回元素
                return self.driver.find_element(by=locators.get(appby), value=ele)
            else:
                raise ValueError(f"Unknown condition type: {cond}")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Element not found or timed out while waiting for {ele}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
        except Exception as e:
            logging.error(f"Error waiting for element {ele}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败

    # 点击元素
    def click_ele(self, appby, cond, ele):
        try:
            element = self.ec_get(appby, cond, ele)
            if element:
                element.click()
                logging.info(f"Clicked on element {ele}")
                return True
            return False
        except Exception as e:
            logging.error(f"Error clicking element {ele}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    # 页面滚动，根据元素
    def rolling(self, susage, eusage, cond, startele, endele):
        try:
            start_element = self.ec_get(susage, cond, startele)
            end_element = self.ec_get(eusage, cond, endele)
            if start_element and end_element:
                self.driver.scroll(start_element, end_element)
                logging.info(f"Scrolled from {startele} to {endele}")
                return True
            else:
                logging.warning(f"Failed to find elements to scroll: {startele} or {endele}")
                return False
        except Exception as e:
            logging.error(f"Error during scroll from {startele} to {endele}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    # 输入内容
    def sendkeys(self, appby, cond, element, keys):
        try:
            element = self.ec_get(appby, cond, element)
            if element:
                element.send_keys(str(keys))
                logging.info(f"Sent keys '{keys}' to element {element}")
                return True
            return False
        except Exception as e:
            logging.error(f"Cannot send keys to {element}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    # 点击指定屏幕位置
    def tap(self, x_proportion, y_proportion):
        try:
            size = self.driver.get_window_size()  # 获取屏幕尺寸
            x = int(size['width'] * x_proportion)
            y = int(size['height'] * y_proportion)
            self.driver.tap([(x, y)])  # 执行点击操作
            logging.info(f"Tapped at position ({x}, {y})")
            return True
        except Exception as e:
            logging.error(f"Tap error: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    # 滑动屏幕,根据屏幕坐标比例
    def swipe(self, start_x_proportion, start_y_proportion, end_x_proportion, end_y_proportion):
        try:
            size = self.driver.get_window_size()  # 获取屏幕尺寸
            start_x = int(size['width'] * start_x_proportion)
            start_y = int(size['height'] * start_y_proportion)
            end_x = int(size['width'] * end_x_proportion)
            end_y = int(size['height'] * end_y_proportion)
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=100)
            logging.info(f"Swiped from ({start_x}, {start_y}) to ({end_x}, {end_y})")
            return True
        except Exception as e:
            logging.error(f"Swipe error: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    # 清除输入框内容
    def clear(self, appby, cond, element):
        try:
            element = self.ec_get(appby, cond, element)
            if element:
                element.clear()
                logging.info(f"Cleared content of element {element}")
                return True
            return False
        except Exception as e:
            logging.error(f"Error clearing element {element}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False

    #等待时间
    def time_sleep(self, num):
        try:
            logging.info(f"Sleeping for {num} seconds")
            time.sleep(num)
            return True
        except Exception as e:
            logging.error(f"Error during sleep for {num} seconds: {e}")
            self.fail(f"Test failed due to sleep error: {e}")  # 强制失败
            return False

    # 执行操作
    def execute_action(self, action, *args):
        action_methods = {
            'click': self.click_ele,
            'rolling': self.rolling,
            'sendkeys': self.sendkeys,
            'tap': self.tap,
            'swipe': self.swipe,
            'clear': self.clear,
            'time': self.time_sleep
        }

        try:
            method = action_methods.get(action)
            if method:
                return method(*args)
            else:
                logging.error(f"Unknown action: {action}")
                self.fail(f"Test failed due to unknown action: {action}")  # 强制使测试失败
                return False
        except Exception as e:
            logging.error(f"Error executing action {action}: {e}")
            self.fail(f"Test failed due to error: {e}")  # 强制使测试失败
            return False


# 用例执行器
def testmove(actions, driver):
    appium_helper = AppiumHelper(driver)
    for action in actions:
        try:
            action_name = action[0]
            args = action[1:]
            result = appium_helper.execute_action(action_name, *args)
            if not result:
                logging.error(f"Action {action_name} failed")
                break
        except Exception as e:
            logging.error(f"Error executing action {action}: {e}")
            driver.quit()
            break
