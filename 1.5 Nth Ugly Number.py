#https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1/#
class Solution:
	def getNthUglyNo(self,n):
		# code here
        ugly = [0] * n
        ugly[0] = 1
        
        p1 = p2 = p3 = 0
        
        nex_2 = 2
        nex_3 = 3
        nex_5 = 5
        
        for i in range(1, n):
            ugly[i] = min(nex_2, nex_3, nex_5)
            
            if ugly[i] == nex_2:
                p1 += 1
                nex_2 = ugly[p1] * 2
                
            if ugly[i] == nex_3:
                p2 += 1
                nex_3 = ugly[p2] * 3
                
            if ugly[i] == nex_5:
                p3 += 1
                nex_5 = ugly[p3] * 5
        
                
        return ugly[-1]
