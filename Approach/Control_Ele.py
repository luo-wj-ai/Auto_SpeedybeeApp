import time
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as Ec

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        except Exception as e:
            logging.error(f"Error waiting for element {ele}: {e}")
            raise

    # 点击元素
    def click_ele(self, appby, cond, element):
        try:
            if self.ec_get(appby, cond, element):
                self.driver.find_element(by=AppiumBy.ID, value=element).click()
                return True
            else:
                logging.warning(f"{element} is not clickable.")
                return False
        except Exception as e:
            logging.error(f"Error clicking element {element}: {e}")
            return False

    # 页面滚动，根据元素
    def rolling(self, susage, eusage, cond, startele, endele):
        try:
            if self.ec_get(susage, cond, startele):
                sdriver = self.ec_get(susage, cond, startele)
                edriver = self.ec_get(eusage, cond, endele)
                self.driver.scroll(sdriver, edriver)
                return True
            else:
                logging.warning(f"Failed to scroll, {startele} is not visible.")
                return False
        except Exception as e:
            logging.error(f"Cannot scroll: {e}")
            return False

    # 输入内容
    def sendkeys(self, appby, cond, element, keys):
        try:
            if self.ec_get(appby, cond, element):
                self.driver.find_element(by=AppiumBy.ID, value=element).send_keys(str(keys))
                return True
            else:
                logging.warning(f"Failed to send keys to {element}.")
                return False
        except Exception as e:
            logging.error(f"Cannot send keys to {element}: {e}")
            return False

    # 点击指定屏幕位置
    def tap(self, x_proportion, y_proportion):
        try:
            size = self.driver.get_window_size()  # 获取屏幕尺寸
            x = int(size['width'] * x_proportion)
            y = int(size['height'] * y_proportion)
            self.driver.tap([(x, y)])  # 执行点击操作
            return True
        except Exception as e:
            logging.error(f"Tap error: {e}")
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
            return True
        except Exception as e:
            logging.error(f"Swipe error: {e}")
            return False

    # 清除输入框内容
    def clear(self, appby, cond, element):
        try:
            if self.ec_get(appby, cond, element):
                self.driver.find_element(by=AppiumBy.ID, value=element).clear()
                return True
            else:
                logging.warning(f"{element} is not clearable.")
                return False
        except Exception as e:
            logging.error(f"Error clearing element {element}: {e}")
            return False

    # 等待时间
    def time_sleep(self, num):
        time.sleep(num)

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
                return False
        except Exception as e:
            logging.error(f"Error executing action {action}: {e}")
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
        except Exception as e:
            logging.error(f"Error executing action {action}: {e}")
            driver.quit()
            break

# # 用法示例
# actions = [
#     ('click', 'XPATH', 'el', 'some_button'),
#     ('sendkeys', 'XPATH', 'el', 'some_input_field', 'Hello, World!'),
#     ('swipe', 0.2, 0.4, 0.8, 0.4)
# ]
#
# testmove(actions, driver)
