#https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = n = len(str1)
        l = len(str2)
        while(i > 0):
            c1 = str1.count(str1[:i])
            if(c1*(i) == n):
                c1 = str2.count(str1[:i])
                if(c1*(i) == l):
                    return str1[:i]
            i-=1
            
        return ""
