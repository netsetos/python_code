def increase_key(arr,i,key):
    if key < arr[i]:
        print("Key should be greater")
    arr[i]=key
    while i>=0 and arr[int((i-1)/2)] < arr[i]:
        arr[i],arr[int((i-1)/2)] = arr[int((i-1)/2)],arr[i]
        i = int((i-1)/2)
    print(arr)

def insert_key(arr,key):
    arr.append(key)
    size=len(arr)
    i=size-1
    while i >= 0 and arr[int((i-1)/2)] < arr[i]:
        arr[i],arr[int((i-1)/2)] = arr[int((i-1)/2)],arr[i]
        i=int((i-1)/2)
    print(arr)



def delete_max(arr):
    size=len(arr)
    if size < 1:
        print("UnderFlow")
    max_root = arr[0]
    arr[0] = arr[size-1]
    size=size-1
    A = max_heapify(arr[0:size],0)
    print('Present element at root is ',A)
    return max_root





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
    return A

def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2

A=[48,35,42,15,7,18,24]
# print(delete_max(A))
# print(increase_key(A,4,70))
insert_key(A,51)