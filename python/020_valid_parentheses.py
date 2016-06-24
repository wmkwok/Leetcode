# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#use a stack for the first half and pair up the rest as you go
class Solution(object):
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        openparens = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                openparens.append(s[i])
                print openparens
            elif s[i] == ')':
                if len(openparens) == 0 or openparens.pop() != '(':
                    return False
            elif s[i] == ']':
                if len(openparens) == 0 or openparens.pop() != '[':
                    return False
            else:
                if len(openparens) == 0 or openparens.pop() != '{':
                    return False
        return True

strang = "(({{}}[]))"
strung = "()(]{}"
sol = Solution()
print sol.isValid(strang)
print sol.isValid(strung)

"""
:type s: str
:rtype: bool
"""
        
