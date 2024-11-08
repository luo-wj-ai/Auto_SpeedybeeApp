# encoding = utf-8
import unittest
from BeautifulReport import BeautifulReport
from Approach.filename import Filepath
from Approach.filename import reportfile_name
from Approach.App_ele_detect import appdriver
from Approach.App_ele_detect import clipapp
from Approach.common_step import text_comparison

from Approach.ele_control import testmove
from Approach.common_step import get_diff_result
from Approach.common_step import android_common_starup
from Approach.common_step import android_common_teardown
from Element.Android_Ele.bf.receiver.receiver_ele import RECEIVERELE
from Element.Android_Ele.bf.receiver.receiver_act import RECEIVERACT


# report 测试套件-待解决问题，BeautifulReport引用testcase后，unittest再次引用，重复测试
def report(testcasename):

    print(f"正在运行 {testcasename.__name__} 的测试用例")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(testCaseClass=testcasename)
    print(f"测试套件中的测试数目： {suite.countTestCases()}")

    # 打印每个测试用例的名称，确认加载的方法
    for case in suite:
        print(f"加载测试用例： {case.id()}")

    filename = reportfile_name()
    print(f"报告文件名： {filename}")

    report_path = Filepath.reportresult_path
    print(f"报告存储路径： {report_path}")

    treport = BeautifulReport(suite)
    treport.report(description=filename, filename=filename, report_dir=report_path)


class Setup_Page(unittest.TestCase):

    def test_receiver_setting1(self):
        print('this is test_port_setting1')

        driver = appdriver(port='4723', version='14', devicename='Pixel_7')  # 驱动
        ele = RECEIVERELE.testcase1           # 元素集合
        actions = RECEIVERACT.actions1          # 用例步骤
        print("进入了app测试步骤\n")
        android_common_starup(driver)    # 打开app通用步骤
        print("app通用步骤已完成\n执行用例\n")
        testmove(actions=actions, driver=driver, ele=ele)   # 执行用例
        print("执行完成用例\n")
        get_diff_result(driver)    # 获取diff结果
        print("执行完成diff结果")
        apkdata = clipapp(packagename="SpeedyBee_2.1.4(7090927).apk", driver=driver)
        print("主方法已写入剪切板")
        # 重置并断开连接-关闭app
        android_common_teardown(driver)
        print("已重置并断开连接-关闭app")
        # win station cli:暂定保存固定的cli输出文件
        winportfile = Filepath.winresult_path + r'receiver\\setting1.txt'
        text_comparison(self, str(apkdata), winportfile)
        print("执行完成")




if __name__ == '__main__':
    report(RECEIVERPAGE)
