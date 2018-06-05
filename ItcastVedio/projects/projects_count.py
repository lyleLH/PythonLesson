import re
from collections import Counter

FILESOURCE = "/Users/MTT/Documents/Python/PythonLesson/ItcastVedio/projects/songs.txt"

def mostCommonWords(fileSource):
    '''输入一个文本文件，统计其中的英文单词出现次数'''
    pattern =r'''[A-Za-z]+|\$?\d+%?$'''
    with open(fileSource) as f:
        r = re.findall(pattern,f.read())
        print(r)
        print("*"*30)
    return Counter(r).most_common()

if __name__ == "__main__":
    # print()
    print(mostCommonWords(FILESOURCE))
