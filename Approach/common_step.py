import unittest
from datetime import datetime

# from SpeedybeeApp.AP.ele_control import app_ele_get
import time

from appium.webdriver.common.appiumby import AppiumBy as Aby
import subprocess
from Approach.ele_control import ControlerMove, app_ele_get, rolling, click_ele, sendkeys, testmove
from Element.Android_Ele.aelement import COMMONSTEP
from Element.iOS_Ele.aelement import COMMONSTEP_IOS

#测试报告
from Approach.filename import Filepath
from BeautifulReport import BeautifulReport




# 运行后直接返回None（跳转界面）
#处理蓝牙连接和密码输入。如果设备设置了密码，会提示用户输入密码
def bluetooth_passwd(driver):

    cwait = ControlerMove(driver, timeout=5)

    # IOS不设置密码”
    conditions = [
        ('etbc', Aby.XPATH, '//XCUIElementTypeStaticText[@name="设置密码"]')
    ]

    for condition in conditions:
        try:
            ecwait = cwait.ec(usage=condition[0], etype=condition[1], element=condition[2])

            if ecwait:
                time.sleep(3)
                content_desc = ecwait.get_attribute('name')

                if content_desc == "设置密码":
                    print("进入了请设置密码校验\n")
                    click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,element='//XCUIElementTypeButton[@name="跳过"]')#点击跳过密码
                    return True

        except Exception as e:
            print(f'异常状况：{e}')
            pass

    return None

#在应用界面上执行滑动操作，以滚动到CLI（命令行界面）或设置菜单。
def roll_to_cli(driver):
    ele = COMMONSTEP.roll_cli
    rolling(driver, 'xpath', 'xpath', 'el', etype=Aby.XPATH, startele=ele['1'], endele=ele['2'])

#在应用界面上执行滑动操作，以滚动到CLI（命令行界面）或设置菜单。
def roll_to_setting(driver):
    ele = COMMONSTEP.roll_cli
    rolling(driver, 'xpath', 'xpath', 'el', etype=Aby.XPATH, startele=ele['2'], endele=ele['1'])

#————————执行测试完成后的清理操作，如重置飞控设备、断开连接、关闭应用等————————
def android_common_teardown(driver):
    # 重置飞控设备，回复默认状态
    ele = COMMONSTEP.common_close
    # 滑动菜单至“设置” 可点
    roll_to_setting(driver)
    # 进入 设置 页面
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['1'])
    # 点击 “更多”
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['2'])
    # 点击“重置”
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['3'])
    # 点击“确认”`
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['4'])
    # 断开连接
    click_ele(driver, 'xpath', 'el', etype=Aby.XPATH, element=ele['5'])
    time.sleep(5)
    # 关闭app
    driver.quit()

#————————在CLI模式下执行diff命令，获取命令返回的结果————————
def get_diff_result(driver):
    ele = COMMONSTEP.common_get_cli_result
    # 滑动至cli菜单
    roll_to_cli(driver)
    # 点击进入cli页面
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['1'])
    # 输入diff命令
    sendkeys(driver, 'id', 'el', etype=Aby.ID, element=ele['2'], keys=r'diff')
    # 点击发送
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['3'])
    # 等待数据返回
    time.sleep(6)
    # 点击复制按键
    click_ele(driver, 'id', 'el', etype=Aby.ID, element=ele['4'])


# ————————断言：判断是否两个文件内容相同，并忽略注释行————————
#读取和过滤文本文件。
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

#读取和过滤文本文件。
def remove_comments_and_empty_lines(lines):
    filtered_lines = []
    for line in lines:
        line = line.strip()  # 去除首尾空白字符
        if line and not line.startswith('#'):  # 忽略空行和以 # 开头的注释行
            filtered_lines.append(line)
    return filtered_lines

#用于比较两个文件的内容，忽略注释行和空行
def text_comparison(self, apprfile, winrfile):
    expected_lines = read_file(apprfile)
    actual_lines = read_file(winrfile)
    # 打印文件内容进行调试
    print("apk文件Expected lines:", expected_lines)
    print("\n")
    print("win文件Actual lines:", actual_lines)
    expected_lines = remove_comments_and_empty_lines(expected_lines)
    actual_lines = remove_comments_and_empty_lines(actual_lines)

    self.assertEqual(expected_lines, actual_lines, "Text files are not equal")
    print("已完成文件对比测试")


#新方法#///////////////////////////////////////////////////////#新方法
#Android重写方法，需要修改
def android_common_starup(driver):
    # 通用
    testmove(COMMONSTEP_IOS.start_action, driver)
    # 加入判断是否是测试设备（测试设备固定命名'luo'）
    #发现了才进行立即连接
    for _ in range(3):
        try:
            testwait = ControlerMove(driver=driver, timeout=5)
            test = testwait.ec('etbc', Aby.XPATH, '//XCUIElementTypeStaticText[@name="发现luo"]')
            content_tar = test.get_attribute('name')
            if content_tar == "发现luo":
                click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                          element='//XCUIElementTypeButton[@name="立即连接"]')  # 直接连接
                # bluetooth_passwd(driver)# 输入密码&跳过密码
                return    # 结束函数执行

        except Exception as ee:
            click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                      element='//XCUIElementTypeButton[@name="可识别的设备"]')  # 点击可识别的设备
            click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                      element='//XCUIElementTypeButton[@name="重新搜索"]')  # 点击重新搜索
    print("找了三次都没有找到飞控，请手动判断是否被其他设备影响\n")

#iOS基础进入方法
def iOS_common_starup(driver):
    # 通用
    testmove(COMMONSTEP_IOS.start_action, driver)
    # 加入判断是否是测试设备（测试设备固定命名'luo'）
    #发现了才进行立即连接
    for _ in range(3):
        try:
            testwait = ControlerMove(driver=driver, timeout=5)
            test = testwait.ec('etbc', Aby.XPATH, '//XCUIElementTypeStaticText[@name="发现luo"]')
            content_tar = test.get_attribute('name')
            if content_tar == "发现luo":
                click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                          element='//XCUIElementTypeButton[@name="立即连接"]')  # 直接连接
                # bluetooth_passwd(driver)# 输入密码&跳过密码
                return    # 结束函数执行

        except Exception as ee:
            click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                      element='//XCUIElementTypeButton[@name="可识别的设备"]')  # 点击可识别的设备
            click_ele(driver, 'xpath', 'el', etype=Aby.XPATH,
                      element='//XCUIElementTypeButton[@name="重新搜索"]')  # 点击重新搜索
    print("找了三次都没有找到飞控，请手动判断是否被其他设备影响\n")


#获取完并重置退出步骤
def iOS_get_diff_result(driver,name):
    #已封装好的步骤
    #先进入cli，输入diff
    testmove(COMMONSTEP_IOS.get_cli_result_action,driver)
    #下面获取剪切版的数据还没有做完
    # iOS_get_attribute(driver,name)
    #用完要处理干净，把飞控重置
    testmove(COMMONSTEP_IOS.resetting,driver)
    #结束程序
    driver.quit()

# report 测试套件-待解决问题，BeautifulReport引用testcase后，unittest再次引用，重复测试
def report(testCaseName):

    print(f"正在运行 {testCaseName.__name__} 的测试用例")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(testCaseName)
    print(f"测试套件中的测试数目： {suite.countTestCases()}")

    # 打印每个测试用例的名称，确认加载的方法
    for case in suite:
        print(f"加载测试用例： {case.id()}")

    # 获取原始报告文件名，并添加当前日期
    current_date = datetime.now().strftime("%Y%m%d")  # 获取当前日期并格式化为 YYYYMMDD
    filename = f"{testCaseName.__name__}_{current_date}"

    print(f"报告文件名： {filename}")

    report_path = Filepath.reportresult_path
    print(f"报告存储路径： {report_path}")

    treport = BeautifulReport(suite)
    treport.report(description=filename, filename=filename, report_dir=report_path)






