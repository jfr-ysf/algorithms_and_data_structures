from collections import deque
n=int(input("Enter amount of vertexes: "))
m=int(input("Enter amount of edges: "))
g={i:set() for i in range(n)}
e_weighs=[[ None for i in range(n)] for i in range(n)]
for i in range(n):
        print(e_weighs[i], end='\n')
'''
for i in range(m):
	v1,v2=map(int, input("Enter edge: ").split())
	weigh=int(input("Enter weigh of edge: "))
	assert weigh>=0
	e_weighs[v1][v2]=weigh
	e_weighs[v2][v1]=weigh
	g[v2].add(v1)
	g[v1].add(v2)
	for j in range(n):
		print(e_weighs[j], end='\n')
'''
g={ 	0:(1,7),
	1:(0,2,3),
	2:(1,3,5,6),
	3:(1,2,5,4),
	4:(3,5,8),
	5:(2,3,4,6,7),
	6:(2,5),
	7:(0,5,8),
	8:(4,7)}
'''
for i in range(n):
	for j in g[i]:
		if e_weighs[i][j]!=None or e_weighs[j][i]!=None:
			continue
		else:
			print("Enter weight of edge (",i,",",j,") : ", end='')
			w=int(input())
			assert w>=0
			e_weighs[i][j]=w
			e_weighs[j][i]=w
'''
e_weighs[0][1]=2
e_weighs[0][7]=15
e_weighs[1][2]=1
e_weighs[1][3]=5
e_weighs[2][3]=3
e_weighs[2][5]=2
e_weighs[2][6]=1
e_weighs[3][5]=4
e_weighs[3][4]=6
e_weighs[4][5]=7
e_weighs[4][8]=2
e_weighs[6][5]=1
e_weighs[7][5]=3
e_weighs[7][8]=12
for i in range(n):
	for j in range(n):
		if e_weighs[i][j]!=None:
			e_weighs[j][i]=e_weighs[i][j]
q=deque([0])
distances=[None]*n
distances[0]=0
parents=[None]*n
ways=[[] for i in range(n)]
while q:
	cv=q.popleft()
	for i in g[cv]:
		if distances[i]==None or distances[i]>(distances[cv]+e_weighs[cv][i]):
			distances[i]=distances[cv]+e_weighs[cv][i]
			parents[i]=cv
			q.append(i)
for i in range(n):
	print("The distance from 0 to",i,"is: ", distances[i])
	#print("The way to get from 0 to",i,": ")
	#print(ways[i])
	#cv=i
	#for j in g[cv]:
	#	if e_weighs[cv][j]!=None and distances[cv]>e_weighs[cv][j]:
	#		ways[cv].append(e_weighs[cv][j])
	#		cv=j
	#		continue		
cv=8
while cv!=0:
	for j in g[cv]:
		if e_weighs[cv][j]!=None and distances[cv]>e_weighs[cv][j]:
			ways[cv].append(e_weighs[cv][j])
			cv=j
			continue
		
print(ways)
input()