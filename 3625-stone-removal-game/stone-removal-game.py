"""
class Solution(object):
    def canAliceWin(self, n):
        x=10
        i=2
        while n-x>=0:
              n=n-x
              x-=1
              i+=1
        if i%2==0:
             return False
        else:
            return True           


"""
class Solution(object):
    def canAliceWin(self, n):
        x = 10
        i = 0

        while n >= x:
            n -= x
            x -= 1
            i += 1

        return i % 2 == 1               


        