#! /usr/bin/python

def printName(str):
    "print your name by string"
    print("your name is %s"%str)
    return

#python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。
#这种方式相当于传值和传引用的一种综合。
#如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
#如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

def changeMe(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值:",mylist)
    return

def changeMeValue(num):
    "按值传递"
    num+=2
    print("函数内的值",num)
    return

#参数类型

#必备参数
def changeMeArg(a,b):
    print(a) 
    return

# changeMeArg(1) #报错

# 命名参数
changeMeArg(a=1,b=2)

#缺省参数

def changeMeArg2(a,b=5): #缺省的值放在后面
    print('a=%d'%(a))
    print('b=%d'%(b))
    return

#changeMeArg2(1,2)
#changeMeArg2(1)

#不定长参数
def argList1(a,b,c,*d):
    print(a)
    print(b)
    print(c)
    print(d)
    return
#INPUT
# test_import.argList1(1,2,3,4,5,6,7,8,9,10)

#OUTPUT
#1
#2
#3
#(4, 5, 6, 7, 8, 9, 10)

def argList2(a,b,c,**d):
    print(a)
    print(b)
    print(c)
    print(d)
    return
#INPUT 
#test_import.argList2("aa",b = 12,c =34, d="44")

#OUTPUT
#aa
#12
#34
#{'d': '44'}

def argList3(**a):
    print(a)
    for key in a:
        print(key+'='+str(a[key]))