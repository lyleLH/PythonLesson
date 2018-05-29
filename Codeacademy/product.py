__author__ = 'lyle'
def product(list):
    output = 1
    for n in list:
        output = output * n
    return  output

print(product([4, 5, 5]))