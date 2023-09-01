def merge_sort(M:list):
    def merge(A:list, B:list):
            C=[0]*(len(A)+len(B))
            i=k=n=0
            while i<len(A) and k<len(B):
                if A[i]<=B[k]:   
                    C[n]=A[i]
                    i+=1
                else:
                    C[n] = B[k]
                    k+= 1
                n+=1
            while i<len(A):
                C[n]=A[i]
                i+=1
                n+=1
            while k<len(B):
                C[n]=B[k]
                k+=1
                n+=1
            return C
    def merge_sorting(M:list):
        if len(M)<=1:
            return
        middle=len(M)//2
        L=[M[i] for i in range(middle)]
        R=[M[i] for i in range(middle, len(M))]
        merge_sort(L)
        merge_sort(R)
        C=merge(L,R)
        for j in range(len(M)):
            M[j]=C[j]
        return M
def hoar_sort(A):
    '''алгоритм потребляет лишнюю память, равную длине массива'''
    if len(A)<=1:
        return'''то же что и return None'''
    barrier=A[0]
    same=[]
    less=[]
    more=[]
    for x in A:
        if x==barrier:
            same.append(x)
        elif x<barrier:
            less.append(x)
        else:
            more.append(x)
    k=0
    hoar_sort(less)
    hoar_sort(more)
    for x in less+same+more:
        A[k]=x; k+=1
def check_sorted(A, ascending=True):
    '''Проверка отсортированности массива А за O(len(A))'''
    flag=True;  s=2*int(ascending)-1
    for i in range(0, len(A)-1):
        if s*A[i]>s*A[i+1]:
            flag=False
            break
    return flag
A=[3,2,4,6,8,9]
B=[9,8,5,4,3,9,0,12]
print(A)
print("The list(array) is sorted:", check_sorted(A)) 
merge_sort(A)
print("Sorted by merge_sort algorithm:", A)
print("The list(array) is sorted:", check_sorted(A)) 
print("The list(array) is sorted:", check_sorted(B))
hoar_sort(B)
print("Sorted by hoar_sort algorithm:", B)
print("The list(array) is sorted:", check_sorted(B))
input()