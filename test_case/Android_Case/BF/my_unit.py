import unittest


class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''setUpClass开始'''
        print("初始化driver\n")
        pass

    @classmethod
    def tearDownClass(cls):
        '''tearDownClass结束'''
        print("结束初始化driver\n")
        pass

    def setUp(self):
        print("\n——————————————开始一次新的测试用例——————————————————————")
        pass

    def tearDown(self):
        pass