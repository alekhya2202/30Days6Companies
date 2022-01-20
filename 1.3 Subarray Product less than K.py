class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        cnt = 0
        left, right, prod = 0,0, 1
        
        while(right < len(a)):
            prod *= a[right]
            
            while(prod >= k):
                prod /= a[left]
                left += 1
                
            cnt += right - left + 1
            right += 1
            
        return cnt
