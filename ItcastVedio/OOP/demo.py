#实例方法、类方法和对象方法

# hasstr

class Employee:
    '''
    一个员工信息的类
    '''
    classInfo = "its a test class"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.salary = salary

    def selfIntroduction(self):
        print("hello, my name is %s,and im %d years old"%(self.name,self.age))
        print("good morning everybody!")