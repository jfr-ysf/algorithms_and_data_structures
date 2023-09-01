from collections import deque
'''
class Queue:
	def __init__()
'''
n,m = map(int, input().split())
g = {i:set() for i in range(n)} #graph
d=[None]*n #distances
stv=0 #start_vertex
d[stv]=0
parents = [None]*n 
q=deque([stv]) #queue
'''
for i in range(m):
	v1,v2 = map(int,input().split())
	g[v1].add(v2)
	g[v2].add(v1)	
'''
g ={0:{1,10,11,12},
	1:{0,7}, 2:{6}, 3:{11},
	4:{6,10}, 5:{13,8},
	6:{2,4,10}, 7:{1,13},
	8:{5,12}, 9:{11}, 10:{6,4,0},
	11:{0,3,9,12,14}, 12:{0,8,11},
	13:{5,7}, 14:{11}}
while q:
	cv = q.popleft() # current_vertex
	for i in g[cv]: # going through the neighbors of current_vertex in set g
		if d[i] is None:
			d[i] = d[cv]+1 # as the neigbor has the d=1 from cv
			parents[i]=cv 
			q.append(i)
ex=-1
while ex>=n or ex<0:
	ex = int(input("Enter the number of the final vertex: ")) # ex - end_vertex
	if ex<n and ex>=0:
		break
	else:
		print("WTF you are doing! Are you dumb? Number must be in range(0,n):")
	#else:
		#break
path=[ex] # Making the path from the end_vertex to reverse it later
parent = parents[ex]
while not parent is None:
	path.append(parent)
	parent = parents[parent]
path[::-1] # reverse of the list
print(path)
print(d) # gives the info 'bout the distances between 0_vertexes and other v-s
input()