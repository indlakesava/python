def cyclic_shift(lst, n):
    if((n)>len(lst)):
        n = (n)%len(lst)
    return lst[n:]+lst[:n]

lst = [1, 2, 3, 4, 5]
print(cyclic_shift(lst, 4))
