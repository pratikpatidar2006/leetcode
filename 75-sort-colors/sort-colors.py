class Solution(object):
    def sortColors(self, nums):
        x = nums.count(0)
        y = nums.count(1)
        z = nums.count(2)

        for i in range(len(nums)):
            if i < x:
                nums[i] = 0
            elif i < x + y:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums