class Solution(object):

    def plusOne(self, digits):
        num = 0

        for i in digits:
            num = num * 10 + i

        num += 1
        return [int(i) for i in str(num)]

    