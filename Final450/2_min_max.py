lst = [2,16,7,10,14,1,8,2]

def min_max(lst):
    if(len(lst)==2):
        return (max(lst[0],lst[1]),min(lst[0],lst[1]))

    else:
        max1, min1 = min_max(lst[:len(lst)//2])
        max2, min2 = min_max(lst[len(lst)//2:])

    return (max(max1,max2), min(min1,min2))

print(min_max(lst))
