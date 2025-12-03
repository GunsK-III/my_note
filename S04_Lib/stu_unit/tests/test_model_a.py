# python -m src.S04_Lib.stu_unit.tests.test_model_a
# python -m unittest -v src.S04_Lib.stu_unit.tests.test_model_a
# 也可以直接执行该脚本

import unittest
from ..proj.model_a import *

class TestModelA1(unittest.TestCase):
    def test_func_a1(self):
        self.assertEqual(func_a1(), 1)

    def test_func_a2(self):
        self.assertFalse(func_a2())
        # 实际中尽量使用assertEqual，避免使用assertTrue或assertFalse

    def test_func_a3(self):
        self.assertNotEqual(func_a3(), "ABC")


class TestModelA2(unittest.TestCase):
    def test_func_a4(self):
        with self.assertRaises(ZeroDivisionError):
            func_a4()


if __name__ == '__main__':
    unittest.main(verbosity=2)
