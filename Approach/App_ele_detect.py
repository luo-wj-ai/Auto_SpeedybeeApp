import datetime
import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from Approach.ele_control import ControlerMove
from Approach.filename import Filepath, apkfilename
from appium.webdriver.common.appiumby import AppiumBy as Aby


#启动webdriver的函数。
def appdriver(platformName, version):
    options = AppiumOptions()
    if platformName=="Android":
        options.load_capabilities({
            "platformName": platformName,
            "appium:platformVersion": version,
            "appium:deviceName": "Android phone",
            "appium:appPackage": "com.runcam.android.runcambf",
            "appium:appActivity": "com.runcam.android.runcambf.SplashActivity",
            "appium:resetKeyboard": True,
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })
    elif platformName=="iOS":
        options.load_capabilities({
            "platformName": platformName,
            "appium:platformVersion": version,
            "appium:deviceName": "iOS Phone",
            "appium:app": "com.runcam.speedybee",
            "appium:udid": "00008030-001109960186802E",
            "appium:automationName": "XCUITest"
        })
    link = f"http://127.0.0.1:4723/wd/hub"
    # print(link)
    driver = webdriver.Remote(command_executor=link, options=options)
    return driver

# 获取剪切板数据
def clipapp(packagename, driver):
    print("开始获取剪切板数据")
    # 手机上获取剪切板数据
    driver = driver
    paste_data = driver.get_clipboard()
    paste_app = str(paste_data)
    # 剪切板数据处理
    filepath = Filepath.apkresult_path
    filename = apkfilename(packagename)    # 仅获取txt文件名称
    aresultfile = str(filepath)+str(filename)        # 文件绝对路径及命名
    print("开始写入剪贴板数据")
    try:
        with open(aresultfile, 'w', encoding='utf-8') as f:
            f.write(paste_app)
            print("剪贴板数据写入成功")

        # ... 省略格式化代码 ...

        print("剪贴板数据处理完成")


    except IOError as e:
        print(f"文件操作失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

    print("进入文档格式化")

    # 文档格式化
    with open(aresultfile, 'r') as file:
        text = file.read()
    text = text.replace(r"\r", '\n').replace(r"\n", '\n')
    with open(aresultfile, 'w') as file:
        file.write(text)

    print("已写入")
    return aresultfile


#新方法#///////////////////////////////////////////////////////#新方法


# 获取元素文本
#举例：tar=('etbc', Aby.XPATH, '//XCUIElementTypeStaticText[@name="发现luo"]')
def iOS_get_attribute(driver,name):
    # 获取当前日期并格式化为YYYY-MM-DD
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        testwait = ControlerMove(driver=driver, timeout=8)
        print("1\n")
        test = testwait.ec('el', Aby.XPATH, '//XCUIElementTypeTextView[@value="diff # version # Betaflight / SPEEDYBEEF405V3 (SBF4) 4.3.2 Apr 7 2023 / 03:15:27 (f156481e9) MSP API: 1.44 # start the command batch batch start board_name SPEEDYBEEF405V3 profile 0 rateprofile 0 # end the command batch batch end # "]')
        time.sleep(3)
        # content_tar = test.get_attribute('value')
        content_tar="这个是一个测试是否可以输入的文件"
        print(content_tar)
        filename=Filepath.iparesult_path + name + '\\'+ current_date + '-' + name+'.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content_tar)

    except Exception as e:
        # 这里可以添加日志记录或其他异常处理
        print(f"An error occurred: {e}")

def test_weile(name):
    # 获取当前日期并格式化为YYYY-MM-DD
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    content_tar = "这个是一个测试是否可以输入的文件"
    print(content_tar)
    filename = Filepath.iparesult_path + name + '\\' + current_date + '-' + name + '.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content_tar)

if __name__ == '__main__':
    test_weile("setting")