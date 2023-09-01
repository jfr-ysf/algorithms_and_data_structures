import stack
def rpn(a:list):
	'''
	RPN - reverse polish notation
	'''
	for x in a:
		if type(x)==int:
			stack.push(x)
		elif x not in '+-*/%':
			continue
		else:
			if stack.los()<2:
				print("First enter the operands and then enter the operation into list")
				return
			a=stack.pop()
			b=stack.pop()
			if x=='+':
				z=b+a
			elif x=='-':
				z=b-a
			elif x=='*':
				z=b*a
			elif x=='/':
				z=b/a
			elif x=='//':
				z=b//a
			else:
				z=b%a
			stack.push(z)
	assert stack.los()==1, 'Error.The amount of operations is greater than amount of operands'
	return stack.pop()
a=[2,'as',7,'%',5,'+']
print(rpn(a))
input()
