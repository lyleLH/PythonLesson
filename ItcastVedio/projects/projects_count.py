import re
from collections import Counter

FILESOURCE = "/Users/MTT/Documents/Python/PythonLesson/ItcastVedio/projects/songs.txt"

def mostCommonWords(fileSource):
    '''输入一个文本文件，统计其中的英文单词出现次数'''
    pattern =r'''[A-Za-z]+|\$?\d+%?$'''
    with open(fileSource) as f:
        r = re.findall(pattern,f.read())
        list = Counter(r).most_common()

        for dic in list:
            print("单词:%s"%dic[0]+"\n"+"出现次数:%s"%dic[1]+"\n")
            # for key in dic:
                # print(key ,dic[key])
            # print(dic)
        #     for key in dic:
        #         print(key,str(dic[key]))
    return list

if __name__ == "__main__":
    # print()
    mostCommonWords(FILESOURCE)
