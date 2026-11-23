class Solution(object):
    def mySqrt(self, x):
        i=0
        ch=0
        while i>=0:
            if i*i>x:
               return ch
            ch=i
            i+=1          