class Solution(object):
    def isValid(self, s):
        x = []
        for i in range(len(s)):
            if s[i] == "(":
                x.append(")")
            elif s[i] == "[":
                x.append("]")
            elif s[i] == "{":
                x.append("}")
            elif s[i] in ")]}":
                if x and x[-1] == s[i]:
                    x.pop()
                else:
                    return False
        return len(x) == 0

        