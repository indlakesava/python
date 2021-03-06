def partition(lst, start, end):
    pos = start
    for i in range(start,end):
        if lst[i]<lst[end]:
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[end],lst[pos] = lst[pos],lst[end]
    return pos

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index
    r : ending index
    k : find kth smallest element
    '''
    if l<=r:
        pos = partition(arr, l, r)
        if(pos+1 == k):
            return arr[pos]
        elif(pos+1 > k):
            arr = arr[l:pos]
            return kthSmallest(arr, 0, len(arr)-1, k)
        else:
            arr = arr[pos+1:r+1]
            return kthSmallest(arr, 0, len(arr)-1, k-pos-1)


arr = [5,2,6,8,1,9,3,7,4]
print(kthSmallest(arr, 0, len(arr)-1, 5))
