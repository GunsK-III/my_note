class ClassB:
    def __init__(self, num_1):
        self.num_a = 1
        self.num_b = self.num_a + num_1

    def func_b1(self):
        return self.num_b * 2


if __name__ == '__main__':
    cb = ClassB(2)
    print(cb.num_b)
    print(cb.func_b1())
