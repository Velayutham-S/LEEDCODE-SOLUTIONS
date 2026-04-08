class Solution:
    def calPoints(self, operations):
        stack = []
        for i in operations:
            if i.isdigit():
                stack.append(int(i))
            elif len(stack) > 0 and i == "C":
                stack.pop()
            elif len(stack) > 0 and i == "D":
                stack.append(stack[-1] * 2)
            elif len(stack) >= 2 and i == "+":
                stack.append(stack[-1]+stack[-2])
            elif int(i) <= 0:
                stack.append(int(i))
        return sum(stack)