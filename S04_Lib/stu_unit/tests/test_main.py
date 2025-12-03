# python -m src.S04_Lib.stu_unit.tests.test_main

from .test_model_a import *
from .test_model_b import *

if __name__ == '__main__':
    suite = unittest.TestSuite()        # 创建测试集

    # 添加测试用例
    # suite.addTest(TestModelA1("test_func_a1"))
    # suite.addTest(TestModelA2("test_func_a4"))
    # suite.addTest(TestClassB1("test_func_b1"))

    # 添加整个测试类（老方法）
    # suite.addTest(unittest.makeSuite(TestModelA1))
    # suite.addTest(unittest.makeSuite(TestModelA2))
    # suite.addTest(unittest.makeSuite(TestClassB1))

    # 添加整个测试类（新方法）
    loader = unittest.TestLoader()       # 测试加载器
    suite.addTests(loader.loadTestsFromTestCase(TestModelA1))
    suite.addTests(loader.loadTestsFromTestCase(TestModelA2))
    suite.addTests(loader.loadTestsFromTestCase(TestClassB1))

    # 自动查找
    # suite = unittest.defaultTestLoader.discover('tests')

    # 运行
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
