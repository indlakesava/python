def rev1(lst):
    return lst[::-1]

def rev2(lst):
    lst1 = []
    for i in range(len(lst)-1,-1,-1):
        lst1.append(lst[i])
    return lst1

def rev3(lst):
    lst1 = []
    for i in range(len(lst)-1,-1,-1):
        lst1.append(lst[i])
    return lst1

lst = [34,56,2,4,332,5,23,54,56,25,64,98]
print(rev1(lst))
print(rev2(lst))
print(rev3(lst))
