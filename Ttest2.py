class A:

    def __init__(self):
        # self.a = 10
        # self.b = 20
        self.c = 30

    def a(self):
        return 1000

    @staticmethod
    def a(cls):
        return 100000

    @property
    def b(self):
        return 2000

    # a = 100001
    c = 300001


print("比较类属性和类方法：")
print(A.a)
print(A.c)
print("比较类属性，类方法，实例属性")
a = A()
print(a.a)
print(a.b)
print(a.c)