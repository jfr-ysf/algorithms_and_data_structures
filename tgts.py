def tgts(a:list, b:list):
	f=[[0]*(len(b)+1) for i in range(len(a)+1)]
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			if a[i-1]==b[j-1]:
				f[i][j] = f[i-1][j-1]+1
			else:
				f[i][j]=max(f[i-1][j], f[i][j-1])
	return f[-1][-1]
a=[1,4,6,87,45,33,94,2]
b=[4,87,33,6,76,31,22]
print(tgts(a,b))
input()