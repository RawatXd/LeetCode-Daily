import math 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       if str1 + str2 != str2 +str1:
           return ""
       
       gcd_length = math.gcd(len(str1),len(str2))

       return str1[:gcd_length]


sol = Solution() 
print(f'Test Case 1 : {sol.gcdOfStrings('ABCABC', 'ABC')}')

print(f'Test Case 2 : {sol.gcdOfStrings('ABABAB', 'ABAB')}')

print(f'Test Case 3 : {sol.gcdOfStrings('LEET', 'CODE')}')




