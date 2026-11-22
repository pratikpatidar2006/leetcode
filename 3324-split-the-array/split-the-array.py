class Solution(object):
    def isPossibleToSplit(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

            if freq[i] > 2:
                return False

        return True