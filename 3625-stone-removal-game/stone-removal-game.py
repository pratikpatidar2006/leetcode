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


               


        