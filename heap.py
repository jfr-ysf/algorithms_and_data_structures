class Heap:
	"""docs for Heap"""
	def __init__(self):
		self.v=[]# 'v' means 'values'
		self.size=0
	def mi(self, n):
		for i in range(self.size):
			if self.v[i]==n:
				return i
	def shift_up(self,i):
		while i!=0 and self.v[(i-1)//2]>=self.v[i]:
			self.v[(i-1)//2],self.v[i]=self.v[i],self.v[(i-1)//2]
			i=(i-1)//2
			print("New index", i, "for the obj ", self.v[i])
	def insert(self, x):
		self.v.append(x)
		self.size+=1
		self.shift_up(self.size-1)
	def shift_down(self, n):
		while 2*n+1<self.size:
			i=n
			if 2*i+2>=self.size and self.v[2*i+1]<self.v[i]:
				i=(2*i)+1
			if 2*i+2<self.size:
				a=min(self.v[2*i+1],self.v[2*i+2])
				b=self.mi(a)
				i=b
			if i==n:
				break
			self.v[n], self.v[i]=self.v[i], self.v[n]
			n=i
	def extract_min(self):
		if self.size==0:
			return None
		tmp=self.v[0]
		self.v[0]=self.v[-1]
		self.v.pop()
		self.size-=1
		self.shift_down(0)
		return tmp
	def is_heap(self):
		for i in range(self.size):
			if 2*i+1<self.size and self.v[2*i+1]<self.v[i]:
				return False
			if 2*i+2<self.size and self.v[2*i+2]<self.v[i]:
				return False
		return True
	def print_v(self):
		print(self.v)