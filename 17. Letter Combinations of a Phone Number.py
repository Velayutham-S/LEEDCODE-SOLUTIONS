class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        i=0
        result = list(digit_to_letters[digits[i]])
        c=0
        while i<len(digits)-1:
            if c==0:
                i+=1
                c=len(result)
            while c>0:
                root=result.pop(0)
                for cc in digit_to_letters[digits[i]]:
                    result.append(root+cc)
                c-=1
        return result
        