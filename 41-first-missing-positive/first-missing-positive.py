class Solution(object):
    def firstMissingPositive(self, nums):
        nums=set(nums)
        i=1
        while i>=0:
             if i not in nums:
                 return i 
             i+=1    
        