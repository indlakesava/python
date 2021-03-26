def longestPalindrome(s):
        def palindrome(ss):
            for i in range(len(ss)//2):
                if(ss[i] != ss[len(ss)-i-1]):
                    return False
            return True

        if(len(s)==1):
            return s

        max_str = ''
        for i in range(len(s)):
            for j in range(len(s)-len(s[i:])+1):
                if palindrome(s[j:j+len(s[i:])]):
                    return s[j:j+len(s[i:])]

print(longestPalindrome("bcaba"))
