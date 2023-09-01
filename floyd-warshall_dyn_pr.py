v=int(input("V: "))
e=int(input("E: "))
w=[[None for i in range(v)] for i in range(v)] # weights of edges
c=0 # counter
for i in range(e):
	v1,v2 = map(int, input("Enter the edge: ").split())
	weight=int(input("Enter the weight of an edge: "))
	w[v1][v2]=weight
	w[v2][v1]=weight
for i in range(v):
        print(w[i], end='\n')
for k in range(v):
	for i in range(v):
		for j in range(v):
			if type(w[i][k])==int and type(w[k][j])==int:
				w[i][j]=min(w[i][j], w[i][k]+w[k][j])
