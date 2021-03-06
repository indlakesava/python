def negatives_oneside(lst,n):
    for i in range(n):
        if lst[i]>=0:
            lst.append(lst[i])
            lst.pop(i)

    return lst

lst = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(negatives_oneside(lst, len(lst)))
