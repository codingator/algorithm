def recursion(s, i):
    if len(s) > 1: return len(s)
    elif s[i] != s[(i+1)*-1]: return 0
    else: return recursion(s, i+1)

def isPalindrome(s):
    return recursion(s, 0)

print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))