def sort012(arr,n):
    low=0;mid=0;high=n-1
    while(mid<=high):
        if arr[mid]==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid+=1;
            low+=1;
            continue;
        elif arr[mid]==1:
            mid+=1;
            continue;
        elif arr[mid]==2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1;

    return arr

lst = [0,2,2,0,1]
print(sort012(lst, len(lst)))
