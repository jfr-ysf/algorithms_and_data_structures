from collections import deque
def srch(a:int,b:list):
	for i in b:
		if i==a:
			return 1
	return 0
n=15
g={ 0:{1,10,11,12},
	1:{0,7}, 2:{6}, 3:{11},
	4:{6,10}, 5:{13,8},
	6:{2,4,10}, 7:{1,13},
	8:{5,12}, 9:{11}, 10:{6,4,0},
	11:{0,3,9,12,14}, 12:{0,8,11},
	13:{5,7}, 14:{11} }
parents = [None]*n
lps = []
arr=[]
m_v=[]#marked_vertexes
m_v.append(0)
q=deque([0])
parents[0]=0
while True:
	if not q:
		m_v.clear()
		q.clear()
		print('the end')
		break
	cv = q.popleft()
	for x in g[cv]:
		if srch(x,m_v)==0:
			print('adding vertex -',x)
			parents[x]=cv
			m_v.append(x)
			q.append(x)
		elif x!=parents[cv] and srch(x,m_v)==1:
			print('cycle_fnd')
			a=x;	b=cv;
			print('found a - neigbour and b - current_vertex',a,b)
			lps.append(a)
			lps.append(b)
			a=parents[a]
			b=parents[b]
			print('loops -',lps)
			#a1=0;	b1=-1;
			while True:
				print('this is a-',a,'and b-',b)
				if a!=b and (a*b)==0:
					c=min(a,b)
					c1=max(a,b)
					mid=len(lps)//2
					lps.append(c)
					lps.append(c1)
					lps[mid], lps[-2]=lps[-2], lps[mid]
					lps[mid+1], lps[-1]=lps[-1], lps[mid+1]
					c1=parents[c1]
				if a==b:
					mid=len(lps)//2
					lps.append(a)
					print('middle of array at_the_end-', mid)
					lps[mid], lps[-1]=lps[-1], lps[mid]
					print('loops ended cycle -',lps)
					arr.append(lps)
					print('fin arr',arr)
					lps.clear()
					break
				else:
					mid=len(lps)//2
					print('array-', lps)
					print('middle of array-', mid)
					lps.append(a)
					lps.append(b)
					lps[mid], lps[-2]=lps[-2], lps[mid]
					lps[mid+1], lps[-1]=lps[-1], lps[mid+1]
					a=parents[a]
					b=parents[b]
					#a1+=1;	b1-=1
print(arr)
print(lps)
''' #3-dimensional array
A=[[[] for i in range(n)] for i in range(n)]
A[0][0].append(5)
print(A)
print(A[0][0])
	#chess_horse_trajectories
numbs='12345678'
letrs='abcdefhg'
g=dict()
def add_edge(v1,v2):
	g[v2].add(v1)
	g[v1].add(v2)
for l in letrs:
	for n in numbs:
		g[n+l]=set()
for i in range(8):
	for j in range(8):
		v1=numbs[i]+letrs[j]
		#for x,y in (i+1,j+2),(i-1,j+2),(i+1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-1,j-2),(i-2,j-1):
		for x,y in (i+1,j+2),(i-1,j+2),(i+2,j+1),(i-2,j+1):
			if 0<=x<8 and 0<=y<8:
				v2=numbs[x]+letrs[y]
				add_edge(v1,v2)
sv=input("Enter the start_vertex: ") # sv - start_vertex
ev=input("Enter the end_vertex: ") # ev - end_vertex
d={v:None for v in g} #distances
d[sv]=0
parents = {v:None for v in g}
q=deque([sv]) #queue
while q:
	cv = q.popleft() # current_vertex
	for i in g[cv]: # going through the neighbors of current_vertex in set g
		if d[i] is None:
			d[i] = d[cv]+1 # as the neigbor has the d=1 from cv
			parents[i]=cv 
			q.append(i)

path=[ev] # Making the path from the end_vertex to reverse it later
parent = parents[ev]
while not parent is None:
	path.append(parent)
	parent = parents[parent]
path[::-1] # reverse of the list
print(path[::-1])
for i in g:
	print(i, g[i]) '''
input()