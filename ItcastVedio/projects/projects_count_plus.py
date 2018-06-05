import re,os
from collections import Counter

#目标文件所在的目录
FILESOURCE = "/Users/MTT/Documents/Python/PythonLesson/ItcastVedio/projects"

def getCounter(fileSource):
    fileSource =FILESOURCE+'/'+fileSource
    '''输入一个英文文本文件，统计其中单词出现的频次'''
    pattern =r'''[A-Za-z]+|\$?\d+%?$'''
    with open(fileSource) as f:
        f = re.findall(pattern,f.read())
        return Counter(f)

#过滤词
filterWords =['the','in','of','and','to','has','s','is','are','a','with','as','an','a']

def findFile(fileDir):
    os.chdir(fileDir)
    total_counter= Counter()
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1]=='.txt':
            total_counter += getCounter(i)

    for i in filterWords:
        total_counter[i]=0
    print(total_counter.most_common())

if __name__ =='__main__':
    findFile(FILESOURCE)