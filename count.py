__author__ = 'lyle'
def count(sequence,item):
    count = 0
    for n in sequence:
        if n== item:
            count = count+1
    return  count

print(count([1,2,1,1],1))