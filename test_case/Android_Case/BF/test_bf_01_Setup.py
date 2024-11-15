from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_01_Setup(MyUnit):

    def test_aaa_Open_expert_mode(self):
        """进入专家模式"""

        self.android_steps.Open_expert_mode()
        pass

    def test_bf_Setup_Setting1(self):
        """测试"""
        self.android_steps.enter_CLI_mode()
        pass

    def test_zzz_end_break(self):
        """断开连接"""
        self.android_steps.end_break()
        pass

