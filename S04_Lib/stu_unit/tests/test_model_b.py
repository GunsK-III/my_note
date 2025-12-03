# python -m src.S04_Lib.stu_unit.tests.test_model_b
# python -m unittest -v src.S04_Lib.stu_unit.tests.test_model_b

import unittest
from ..proj.model_b import ClassB


class TestClassB1(unittest.TestCase):
    def setUp(self):
        self.cb = ClassB(2)
        # print(f"执行测试方法: {self._testMethodName}")

    def test_func_b1(self):
        assert self.cb.num_a == 1

    def test_func_b2(self):
        assert self.cb.num_b != 4

    def test_func_b3(self):
        assert self.cb.func_b1() == 6

    @unittest.skip("跳过这条用例")
    def test_func_b4(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
