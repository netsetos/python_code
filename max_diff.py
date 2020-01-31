def max_diff_ele(arr):
    arr=sorted(arr)
    size=len(arr)

    diff = - 999*999

    for i in range(size-1):
        if(arr[i+1]-arr[i]>diff):
            diff=arr[i+1]-arr[i]
    return diff

arr=[ 5 , 32 , 45 , 4 , 12 , 18 , 25 ]
print("Maximum difference between array elements is",max_diff_ele(arr))








