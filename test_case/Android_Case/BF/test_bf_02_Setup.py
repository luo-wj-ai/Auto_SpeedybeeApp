import unittest
from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_02_Setup(MyUnit):


    def test_bf_Setup_Setting3(self):
        '''Setup基本设置页操作01'''
        print(333333333)

        # self.c_android.Open_expert_mode()
        pass

    def test_bf_Setup_Setting4(self):
        '''Setup基本设置页操作02'''
        print(444444444444444)
        self.fail(f"Test failed due to error: ")  # 强制使测试失败
        # self.c_android.Open_expert_mode()
        pass
