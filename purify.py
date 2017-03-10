__author__ = 'lyle'
def purify(list):
    out_put_list = []
    for n in list:
        if n%2 == 0:
            out_put_list.append(n)
    return  out_put_list

print(purify([1,2,3]))