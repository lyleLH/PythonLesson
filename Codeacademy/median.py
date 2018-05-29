__author__ = 'lyle'
def median(alist):
    alist = sorted(alist)
    count_of_list  = len(alist)
    midIndex= 0
    if count_of_list ==1:
        return alist[0]
    if count_of_list %2==0:
        midIndex = (int)(count_of_list/2)
        return (alist[midIndex]+alist[midIndex-1])/(2.0)
    else:
        midIndex = (int)((count_of_list-1)/2)
        return (alist[midIndex])


print(median([4,5,5,4]))