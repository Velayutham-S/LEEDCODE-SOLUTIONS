# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        res = []
        def getelements(root):
            temp = root
            while temp:
                res.append(temp.val)
                temp = temp.next
        getelements(head)
        result = [0] * len(res)
        stack = []
        for i in range(0,len(res)):
            while stack and res[stack[-1]] < res[i]:
                index = stack.pop()
                result[index] = res[i]
            stack.append(i)
        return result