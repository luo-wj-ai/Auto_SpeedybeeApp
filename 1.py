import time
import logging
import selenium.webdriver.support.expected_conditions as Ec
from adodbapi.examples.xls_read import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


# 等待元素出现或满足条件,并进行定位
def ec_get(self, usage, wusage, ele):
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
        condition = conditions.get(wusage)
        if condition:
            self.wait.until(condition((locators.get(usage), ele)))
            return self.driver.find_element(by=locators.get(usage), value=ele)
        else:
            raise ValueError(f"Unknown usage type: {wusage}")
    except Exception as e:
        logging.error(f"Error waiting for element {ele}: {e}")
        raise
