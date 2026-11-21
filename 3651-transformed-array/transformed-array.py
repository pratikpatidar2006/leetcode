class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        final = []
        
        for i in range(n):
            target_index = (i + nums[i]) % n
            final.append(nums[target_index])
            
        return final
                