def foo(op,n1,n2):
	return eval("%d %s %d" %(n1,op,n2))
print foo(raw_input (),int(raw_input()),int(raw_input()))
