class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums=[]
        for i in range(m):
            nums.append(nums1[i])
        for  j in range(n):
            nums.append(nums2[j])
        nums.sort()
        for i in range(len(nums)):
            nums1[i]=nums[i]  

