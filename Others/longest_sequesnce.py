def longest_sequence(num):
    lst_num = str(num)
    longest_seq = ''

    for i in range(len(lst_num)):
        temp_seq = ''
        for j in range(len(lst_num[i:-1])):
            if(int(lst_num[i+j]) == int(lst_num[i+j+1])-1):
                temp_seq = lst_num[i:i+j+2]
            else:
                break;
        if(len(temp_seq)>len(longest_seq)):
            longest_seq = temp_seq

    return longest_seq


print(longest_sequence(2438979892345678385735678123098789567))
