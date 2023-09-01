from heap import Heap    
def heapify(a:list):
	h=Heap()
	for i in a:
		h.insert(i)
	print(h.is_heap())
	return h
def heap_sort(a:list):
	b=heapify(a)
	print(b.v)
	print(b.is_heap())
	a1=[]
	for i in range(b.size):
		print(a1)
		a1.append(b.extract_min())
		print(a1)
	print("Result: ")
	print(a1)
	return a1
arr=[45,15,3,4,21,4,79,61]
print(heap_sort(arr))
input()