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
        self.wait = WebDriverWait(driver, timeout)

        # 提前定义好定位器和条件的映射字典
        self.locators = {
            'ID': AppiumBy.ID,
            'XPATH': AppiumBy.XPATH,
            'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
            'NAME': AppiumBy.NAME
        }
        self.conditions = {
            'el': Ec.presence_of_element_located,
            'etbc': Ec.element_to_be_clickable,
            'ioe': Ec.invisibility_of_element_located,
            'eltbs': Ec.element_located_to_be_selected,
            'voel': Ec.visibility_of_element_located
        }

    def handle_error(self, msg, exception=None):
        """统一的错误处理"""
        logging.error(msg)
        if exception:
            logging.exception(exception)

    def ec_get(self, appby, cond, ele):
        """通用元素定位获取"""
        try:
            condition = self.conditions.get(cond)
            locator = self.locators.get(appby)
            if not condition or not locator:
                raise ValueError(f"Invalid locator or condition: {appby}, {cond}")
            # 等待直到条件满足
            self.wait.until(condition((locator, ele)))
            return self.driver.find_element(by=locator, value=ele)
        except (NoSuchElementException, TimeoutException) as e:
            self.handle_error(f"Element not found or timed out while waiting for {ele}", e)
        except Exception as e:
            self.handle_error(f"Error waiting for element {ele}", e)

    def click_ele(self, appby, cond, ele):
        """点击元素"""
        try:
            element = self.ec_get(appby, cond, ele)
            if element:
                element.click()
                logging.info(f"Clicked on element {ele}")
                return True
            return False
        except Exception as e:
            self.handle_error(f"Error clicking element {ele}", e)
            return False

    def rolling(self, susage, eusage, cond, startele, endele):
        """滚动操作"""
        try:
            start_element = self.ec_get(susage, cond, startele)
            end_element = self.ec_get(eusage, cond, endele)
            if start_element and end_element:
                self.driver.scroll(start_element, end_element)
                logging.info(f"Scrolled from {startele} to {endele}")
                return True
            logging.warning(f"Failed to find elements to scroll: {startele} or {endele}")
            return False
        except Exception as e:
            self.handle_error(f"Error during scroll from {startele} to {endele}", e)
            return False

    def sendkeys(self, appby, cond, element, keys):
        """发送键值"""
        try:
            element = self.ec_get(appby, cond, element)
            if element:
                element.send_keys(str(keys))
                logging.info(f"Sent keys '{keys}' to element {element}")
                return True
            return False
        except Exception as e:
            self.handle_error(f"Cannot send keys to {element}", e)
            return False

    def tap(self, x_proportion, y_proportion):
        """点击屏幕指定位置"""
        try:
            size = self.driver.get_window_size()
            x = int(size['width'] * x_proportion)
            y = int(size['height'] * y_proportion)
            self.driver.tap([(x, y)])
            logging.info(f"Tapped at position ({x}, {y})")
            return True
        except Exception as e:
            self.handle_error(f"Tap error", e)
            return False

    def swipe(self, start_x_proportion, start_y_proportion, end_x_proportion, end_y_proportion):
        """滑动操作"""
        try:
            size = self.driver.get_window_size()
            start_x = int(size['width'] * start_x_proportion)
            start_y = int(size['height'] * start_y_proportion)
            end_x = int(size['width'] * end_x_proportion)
            end_y = int(size['height'] * end_y_proportion)
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=100)
            logging.info(f"Swiped from ({start_x}, {start_y}) to ({end_x}, {end_y})")
            return True
        except Exception as e:
            self.handle_error(f"Swipe error", e)
            return False

    def clear(self, appby, cond, element):
        """清除元素内容"""
        try:
            element = self.ec_get(appby, cond, element)
            if element:
                element.clear()
                logging.info(f"Cleared content of element {element}")
                return True
            return False
        except Exception as e:
            self.handle_error(f"Error clearing element {element}", e)
            return False

    def time_sleep(self, num):
        """睡眠操作"""
        try:
            logging.info(f"Sleeping for {num} seconds")
            time.sleep(num)
            return True
        except Exception as e:
            self.handle_error(f"Error during sleep for {num} seconds", e)
            return False

    def execute_action(self, action, *args):
        """执行指定动作"""
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
                self.handle_error(f"Unknown action: {action}")
                return False
        except Exception as e:
            self.handle_error(f"Error executing action {action}", e)
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
