def foo(op,n1,n2):
	return eval("%d %s %d" %(n1,op,n2))
print  'result is : %s \n' % foo(raw_input('input an operater:\n'),int(raw_input('input an int:\n')),int(raw_input('input another int:\n')))
