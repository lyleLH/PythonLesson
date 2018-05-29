#字符串格式化 
print("my name is %s,Im %d years old"%("tom",26))

#字符串的各种函数 vi
#s.find() len()
#s.index()
#s.count
#s.replace

mystr = "hello world itcast and itcastcpp and itcast"
mystr.find("itcast"[0:1])
mystr.find("itcast",start=0,end =len(mystr))
mystr.index("itcast")
mystr.count("itcast")
mystr.decode(encoding="UTF-8")
mystr.replace("itcast","chuanzhiboke",2)
 

#字符串操作
#s.split()
mystr.split(" ")
words = mystr.split(" ",2)
for word in words:
    print(word)
words.sort()

#字符串验证

mystr.capitalize()
mystr.endswith("itcast")
mystr.startswith("hello")
#不能含有空格
mystr.isalnum()#至少一个数字，所有字符都是字母或者数字
mystr.isalpha()#至少一个字符，所有字符都为字母

#只包含十进制数字
mystr.isdecimal()

#字符全为大、小写
mystr.isupper()
mystr.islower()

#字符全是空格
mystr.isspace()

#字符串插入
mystr.join("XXX")


#字符串输出排列方式
mystr.ljust(60)
mystr.rjust(60)
mystr.center(80)

#过滤字符串中的空格
mystr.lstrip()
mystr.rstrip()

#字符串分割
mystr.partition('world')
mystr.partition('hello') #Out[186]: ('', 'hello', ' world itcast and itcastcpp and itcast')