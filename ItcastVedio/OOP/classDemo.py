class Parrent:
    parrentAttr =100
    def __init__(self):
        print ("父类的初始化")
    def parrentMethod(self):
        print("父类的方法")
    def setAttr(self,attr):
        Parrent.parrentAttr =attr
        print("父类的属性设置方法")
    def getAttr(self):
        print("父类的属性访问:%d"%Parrent.parrentAttr)

    def sayHello(self):
        print("hello itcast")

class Children(Parrent):
    def __init__(self):
        Parrent() #需要手动调用父类的初始化方法
        print("子类的初始化")

    def childMethod(self):
        print("子类方法 childMethod")

    # def  sayHello(self):
        # print("你好,深圳")