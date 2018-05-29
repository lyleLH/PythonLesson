import test_import

test_import.printName("tom")

mylist = [100,200,300]
test_import.changeMe(mylist)


#匿名函数
sum =lambda a,b:a+b
#In [5]: sum(10,20)
#Out[5]: 30

def arglist():
    print("call arglist")
    return 1,2,3,4,5,6