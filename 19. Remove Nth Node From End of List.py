class Solution:
    def removeNthFromEnd(self,head,n):
        temp = head
        list1 = []
        b = n+1
        while temp != None:
            list1.append(temp)
            temp = temp.next
        if n<len(list1):
            prev = list1[-b]
            current = list1[-n]
            
            prev.next = current.next
        else:
            head = head.next
        return head