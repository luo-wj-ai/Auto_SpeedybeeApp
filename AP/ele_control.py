"""
presence_of_element_located: 判断元素是否出现在DOM中。
visibility_of_element_located: 判断元素是否可见。
element_to_be_clickable: 判断元素是否可点击。
title_contains: 判断页面标题是否包含特定文本。
alert_is_present: 判断页面是否存在警告框（alert）。
"""
import time
import selenium.webdriver.support.expected_conditions as Ec
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


#捕获元素的方法
#传driver，捕获的元素，参数
def app_ele_get(driver, usage, elem):

    try:
        if usage == 'id':
            return driver.find_element(by=AppiumBy.ID, value=elem)
        elif usage == 'xpath':
            return driver.find_element(by=AppiumBy.XPATH, value=elem)
        elif usage == 'aid':
            return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=elem)
        elif usage == 'name':
            return driver.find_element(by=AppiumBy.NAME, value=elem)
        elif usage == 'iosclasschain':
            return driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value=elem)
        elif usage == 'iospredicate':
            return driver.find_element(by=AppiumBy.IOS_PREDICATE, value=elem)
        elif usage == 'iosui':
            return driver.find_element(by=AppiumBy.IOS_UIAUTOMATION, value=elem)
        elif usage == 'androidui':
            return driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=elem)

    except Exception as e:
        print("error:", f"cannot find the elements{e}")
        # raise e

class ControlerMove:

    def __init__(self, driver, timeout=5):
        self.wait = WebDriverWait(driver=driver, timeout=timeout)

    def ec(self, usage, etype, element):
        try:
            locator = (etype, element)
            if usage == 'el':       # 等待至少一个元素出现在 DOM 中
                return self.wait.until(Ec.presence_of_element_located(locator))

            elif usage == 'etbc':   # 等待元素可点击

                return self.wait.until(Ec.element_to_be_clickable(locator))

            elif usage == 'ioe':    # 等待元素在页面上不可见
                return self.wait.until(Ec.invisibility_of_element_located(locator))

            elif usage == 'eltbs':  # 等待元素被选中
                return self.wait.until(Ec.element_located_to_be_selected(locator))

            elif usage == 'voel':   # 等待元素出现在 DOM 中，并且可见（visible）
                return self.wait.until(Ec.visibility_of_element_located(locator))

        except Exception as e:
            print("error:", f"cannot find the elements{e}")
            # raise e  # 抛出异常，中断测试

# 操作控制

# 点击
def click_ele(driver, usage, wusage, etype, element):
    try:
        controller = ControlerMove(driver)
        test = controller.ec(wusage, etype=etype, element=element)
        print(test)
        if test:
            app_ele_get(driver=driver, usage=usage, elem=element).click()
            return True
        else:
            print(f"{element},is not clickable.")
            return False
    except Exception as e:
        print(f'please check the ele was gived,{e}')
        driver.quit()
        return False


# 页面滚动   ---等待修改，修改页面滚动至指定位置
def rolling(driver, susage, eusage, wusage, etype, startele, endele):
    try:
        controller = ControlerMove(driver)
        test = controller.ec(wusage, etype=etype, element=startele)
        if test:
            sdriver = app_ele_get(driver=driver, usage=susage, elem=startele)
            edriver = app_ele_get(driver=driver, usage=eusage, elem=endele)
            driver.scroll(sdriver, edriver)
            return True
        else:
            print(f'fail to rolling,{startele} is not show')
            return False
    except Exception as e:
        print(f"can not scroll,{e},check your element")
        driver.quit()
        raise e

# 输入器
def sendkeys(driver, usage, wusage, etype, element, keys):
    try:
        controller = ControlerMove(driver, timeout=8)
        test = controller.ec(wusage, etype=etype, element=element)
        if test:
            sdriver = app_ele_get(driver=driver, usage=usage, elem=element)
            sdriver.send_keys(str(keys))
            return True
        else:
            print(f'fail to rolling,{element} is not show')
            return False
    except Exception as e:
        print(f"can not send,{e},check your element")
        driver.quit()
        raise e



#通过坐标进行点击,需要传入x，y按钮的比例
def tap(driver,x_proportion,y_proportion):#比如iPhone11的比例是：414*896
    try:
        size = driver.get_window_size()#获取屏幕比例
        x = int(size['width'] * x_proportion)
        y = int(size['height'] * y_proportion)
        driver.tap([(x, y)])#执行点击操作
    except:
        print("tap错误")
        driver.quit()

#通过元素坐标进行滑动
def swipe(driver,start_x_proportion, start_y_proportion, end_x_proportion, end_y_proportion):
    try:
        size = driver.get_window_size()  # 获取屏幕比例
        start_x=int(size['width']*start_x_proportion)
        start_y=int(size['height']*start_y_proportion)
        end_x=int(size['width']*end_x_proportion)
        end_y=int(size['height']*end_y_proportion)
        driver.swipe(start_x, start_y, end_x, end_y, duration=100)
        # print(start_x, '\n', start_y,'\n',end_x,'\n',end_y,'\n')
        # print("滑动成功家人们\n")
    except:
        print("swipe错误")
        driver.quit()

#清除输入框
def clear(driver, usage, wusage, etype, element):
    try:
        controller = ControlerMove(driver)
        test = controller.ec(wusage, etype=etype, element=element)
        print(test)
        if test:
            app_ele_get(driver=driver, usage=usage, elem=element).clear()
            return True
        else:
            print(f"{element},is not clearable.")
            return False
    except Exception as e:
        print(f'please check the ele was gived,{e}')
        driver.quit()
        return False


# 用例执行器
def testmove(actions, driver):
    for action in actions:
        if action[0] == 'click':
            click_ele(driver, action[1], action[2], etype=action[3], element=action[4])
        elif action[0] == 'rolling':
            rolling(driver, action[1], action[2], action[3], etype=action[4], startele=action[5],endele=action[6])
        elif action[0] == 'time':
            time.sleep(action[1])
        elif action[0] == 'sendkeys':
            sendkeys(driver, usage=action[1], wusage=action[2], etype=action[3], element=action[4], keys=action[5])
        elif action[0] == 'clear':
            clear(driver, usage=action[1], wusage=action[2], etype=action[3], element=action[4])
        elif action[0] =='tap':
            tap(driver,x_proportion=action[1],y_proportion=action[2])
        elif action[0] =='swipe':
            swipe(driver,start_x_proportion=action[1],start_y_proportion=action[2],end_x_proportion=action[3],end_y_proportion=action[4])
        else:
            print("没有这个操作方法")
            driver.quit()
            break


