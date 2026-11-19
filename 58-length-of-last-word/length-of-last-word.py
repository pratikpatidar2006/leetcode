class Solution(object):
    def lengthOfLastWord(self, s):
       j=0 
       for i in range(len(s)-1,-1,-1):
           if s[i]!=" ":
               j+=1
           if i==0:
               return j    
           if s[i]!=" " and s[i-1]==" ":
               return j 

        