__author__ = 'lyle'
def remove_duplicates(list):
    output = []
    for m in list:
        if m not in output:
            output.append(m)
    return  output

print(remove_duplicates([1,1,2,2]) )