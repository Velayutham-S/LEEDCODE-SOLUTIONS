class Solution:
    def removeDuplicates(self, s):
        if len(s) == 1:
            return s
        stack = []
        stack.append(s[0])
        print(stack)
        for i in range(1,len(s)):
            if len(stack) > 0 and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
s1 = Solution()
print(s1.removeDuplicates("abbaca"))