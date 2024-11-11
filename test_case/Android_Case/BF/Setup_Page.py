# encoding = utf-8
import unittest
from BeautifulReport import BeautifulReport
from Approach.filename import Filepath
from Approach.filename import reportfile_name
from Approach.App_ele_detect import appdriver
from Approach.App_ele_detect import clipapp
from Approach.Common_Step import text_comparison

from Approach.Control_Ele import testmove
from Approach.Common_Step import get_diff_result
from Approach.Common_Step import android_common_starup
from Approach.Common_Step import android_common_teardown
from Element.Android_Ele.BF.receiver.receiver_ele import RECEIVERELE
from Element.Android_Ele.BF.receiver.receiver_act import RECEIVERACT


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

    def test_Setup_Setting1(self):

        driver = appdriver(platformName="Android",version='14')  # 驱动
        ele = RECEIVERELE.testcase1           # 元素集合
        actions = RECEIVERACT.actions1          # 用例步骤
        android_common_starup(driver)    # 打开app通用步骤
        testmove(actions=actions, driver=driver, ele=ele)   # 执行用例
        get_diff_result(driver)    # 获取diff结果
        apkdata = clipapp(packagename="SpeedyBee_2.1.4(7090927).apk", driver=driver)
        # 重置并断开连接-关闭app
        android_common_teardown(driver)
        # win station cli:暂定保存固定的cli输出文件
        winportfile = Filepath.winresult_path + r'receiver\\setting1.txt'
        text_comparison(self, str(apkdata), winportfile)
        print("执行完成")




if __name__ == '__main__':
    report(Setup_Page)
