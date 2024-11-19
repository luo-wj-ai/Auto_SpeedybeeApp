from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_01_Setup(MyUnit):


    def tearDown(self):
        pass

    def test_bf_01Setup_Setting01(self):
        """恢复默认设置"""

        pass

    def test_bf_01Setup_Setting02(self):
        """恢复默认设置"""

        pass

    @classmethod
    def tearDownClass(cls):
        cls.close_driver=True
        super().tearDownClass()
        pass