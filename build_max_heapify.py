def max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(A):
    n = int((len(A) // 2)-1)
    for i in range(n, -1,-1):
        max_heapify(A, i)


A = [11,6,5,0,8,2,7]
build_max_heap(A)
print(A)
