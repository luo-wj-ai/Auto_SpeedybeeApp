import unittest
from AP.App_ele_detect import ios_appdriver
from AP.common_step import iOS_common_starup, iOS_get_diff_result, report
from AP.ele_control import testmove
from iOS_Element.BF.PortAct import PortAct




class PortPage(unittest.TestCase):
    #开始打开驱动
    def setUp(self) -> None:
        self.driver = ios_appdriver(platformName='iOS')  # 驱动
        iOS_common_starup(self.driver)  # 打开IOS_app通用步骤
    #接触关闭驱动并关闭控件
    def tearDown(self) -> None:
        iOS_get_diff_result(self.driver,name='setting')    # 获取diff结果并重置关闭飞控
        # #对比两个文件有没有差异
        # # text_comparison(self, str(apkdata), Filepath.winresult_path + r'setting\\setting1.txt')
        # print("执行完成")
    def test_port1(self):
        testmove(actions=PortAct.actions1,driver=self.driver)   ####执行用例###
if __name__ == '__main__':
    report(PortPage)