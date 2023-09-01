from random import randint
a=[12,2,2,6,12,23,65,77,98]
print(a)
def merge_sort(c:list):
    def merge(a:list, b:list):
        c=[0]*(len(a)+len(b))
        i=j=k=0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:
                c[k]=a[i];  i+=1
            else:
                c[k]=b[j];  j+=1
            k+=1
        while i<len(a):
            c[k]=a[i];  i+=1;   k+=1
        while j<len(b):
            c[k]=b[j];  j+=1;   k+=1
        return c
    if len(c)<=1:
        return
    middle=len(c)//2
    l=[c[i] for i in range(middle)]
    r=[c[i] for i in range(middle, len(c))]
    merge_sort(l)
    merge_sort(r)
    d=merge(l,r)
    for i in range(len(c)):
        c[i]=d[i]
merge_sort(a)
print(a)
val=int(input("Enter the searched value: "))
low=0
high=len(a)-1
mid=len(a)//2
while low<=high:
    if a[mid]==val:
        break
    if a[mid]<val:
        low=mid+1
    elif a[mid]>val:
        high=mid-1
    mid=(low+high)//2
if low>high:
    print("Not found")
else:
    if a[mid]==a[mid-1]:
        print("Id_1=", mid, "Id_2=", mid-1)
    elif a[mid]==a[mid+1]:
        print("Id_1=", mid, "Id_2=", mid+1)
    else:
        print("ID=", mid)
