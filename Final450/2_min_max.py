lst = [2,16,7,10,14,1,8,2]

#General method, traversing through the list. Time Complexity - O(n)
def min_max1(lst):
    min=max=lst[0]
    for i in lst:
        if(i<min):
            min = i
        elif(i>max):
            max = i
    return min, max

#Another method following Divide and conquer, was able to acheive the result only when len(lst) is of order 2^n
def min_max2(lst):
    if(len(lst)==2):
        return (max(lst[0],lst[1]),min(lst[0],lst[1]))

    else:
        max1, min1 = min_max2(lst[:len(lst)//2])
        max2, min2 = min_max2(lst[len(lst)//2:])

    return (max(max1,max2), min(min1,min2))

print(min_max1(lst))
print(min_max2(lst))
