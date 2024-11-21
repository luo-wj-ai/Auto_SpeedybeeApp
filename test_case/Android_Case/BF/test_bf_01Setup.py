from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_01Setup(MyUnit):


    def test_bf_01Setup_Setting01(self):
        """恢复默认设置"""
        super().execute_actions("SetupAct.json", self.driver, act_name="SetupAct", group="action1")
        pass

    def test_bf_02Presets_Setting01(self):
        """"""
        super().execute_actions("PresetsAct.json", self.driver, act_name="PresetsAct", group="action1")
        pass

    def test_bf_03Port_Setting01(self):
        """打开UART2-MSP<br/>UART3-串行接收机<br/>UART4-FrSky"""
        super().execute_actions("PortAct.json", self.driver, act_name="PortAct", group="action1")
        pass

    def test_bf_04Mode_Setting01(self):
        """添加前四个范围和前3个链接 """
        super().execute_actions("ModeAct.json", self.driver, act_name="ModeAct", group="action1")
        pass



    @classmethod
    def tearDownClass(cls):
        cls.close_driver=True
        super().tearDownClass()
        pass