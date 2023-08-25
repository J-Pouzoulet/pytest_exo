class Solution:
        def __init__(self, input : int):
            self.input = input
            self.output = self.solution(self.input)

        def solution(self, input):
            roman = {1:'I', 4: 'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50: 'L', 90:'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
            output = ''
            while input != 0:    
                val = max([i for i in list(roman.keys()) if i <= input])
                input -= val
                output += roman[val] 
            return output