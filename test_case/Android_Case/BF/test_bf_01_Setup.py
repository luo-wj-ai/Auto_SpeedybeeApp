import unittest
from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_01_Setup(MyUnit):

    def test_AAA_Open_expert_mode(self):
        self.android_steps.Open_expert_mode()
        pass

    def test_bf_Setup_Setting1(self):
        '''Setup基本设置页操作01'''

        pass

    def test_bf_Setup_Setting2(self):
        '''Setup基本设置页操作01'''
        print(33333)
        pass


    def test_ZZZ_Exit_expert_mode(self):
        self.driver.quit()