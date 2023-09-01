"""stack=[]
def push(x):
    stack.append(x)
def pop():
    x=stack.pop()
    return x
def clear():
    stack.clear()
def is_empty():
    return len(stack)==0
def los():
    return len(stack)
def test():
    import doctest
    doctest.testmod()
if __name__=='__main__':
    test()
    input()
"""
f=0
for i in range(1,2020):
    f+=i
print(f)
