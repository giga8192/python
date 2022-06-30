

value = 100

class A:
    def m1(self,value1,value2):
        print(value1)
        print(value2)

    def m2(self):
        value1 = 1
        value2 = 2
        self.m1(value1 = str(value1)
                if value1 else None,
                value2 = str(value2)
                if value2 else None,)

obj1 = A()
obj1.m2()

def f1(value):
    return str(value) if value else None

res1 = f1(100)
res2 = f1(None)

