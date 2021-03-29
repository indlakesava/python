def Hangman(s):
    lst = ['_']*len(s)

    for i in range(10):
        a = input('Enter the character you guess:')[0]

        if a in s:
            for k in range(len(s)):
                if s[k] == a:
                    lst[k] = s[k]

        print('Your guess is:', ''.join(lst), '    :Chances left - ', len(s)-i-1)

        if '_' not in lst:
            print(''.join(lst))
            return "Success"

    return "Game Over"

print(Hangman('DATAMINING'))
