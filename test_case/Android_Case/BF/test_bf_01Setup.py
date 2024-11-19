from test_case.Android_Case.BF.my_unit import MyUnit


class Test_bf_01Setup(MyUnit):


    def test_bf_01Setup_Setting01(self):
        """恢复默认设置"""
        self.use_contains_assert = False
        self.sequence_to_check="SPEEDYBEEF405AIO"
        pass

    def test_bf_01Setup_Setting02(self):
        """恢复默认设置"""

        pass

    @classmethod
    def tearDownClass(cls):
        cls.close_driver=True
        super().tearDownClass()
        pass