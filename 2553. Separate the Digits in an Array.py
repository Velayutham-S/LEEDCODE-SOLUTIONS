class Solution:
    def separateDigits(self, nums):
        list1 = []
        for i in nums:
            if len(str(i)) == 1:
                list1.append(i)
            else:
                n = i
                demo = []
                while n > 0:
                    demo.append(n % 10)
                    n = n //10
                list1.extend(demo[::-1])
        return list1