# 선택 정렬
def selection_sort(A):
    n=len(A)
    for i in range(n-1):
        least=i
        for j in range(i+1, n):
            if (A[j]<A[least]):
                least=j
        A[i], A[least] = A[least], A[i]

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print("선택 정렬 전: ", data)
selection_sort(data)
print("선택 정렬 후: ", data)
print('')

# 삽입 정렬
def insertion_sort(A):
    n=len(A)
    for i in range(1, n):
        x=A[i]
        j=i-1
        while j>=0 and A[j]>x:
            A[j+1]=A[j]
            j-=1
        A[j+1]=x

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print("삽입 정렬 전: ", data)
insertion_sort(data)
print("삽입 정렬 후: ", data)
print('')


# 버블 정렬
def bubble_sort(A):
    n=len(A)
    for i in range(n-1, 0, -1):
        bChanged=False
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged=True
        if not bChanged:
            break

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print("버블 정렬 전: ", data)
bubble_sort(data)
print("버블 정렬 후: ", data)
