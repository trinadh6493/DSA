class Solution:
    def isValid(self, s: str) -> bool:
        if s=="()" or s=="{}" or s=="[]":
            return True
        elif len(s)<3:
            return False
        
        l=[]
        s4=('[','{','(')
        s5=(']','}',')')
        for i in range(len(s)):
            if s[i] in s5:
                if len(l)==0:
                    return False
                a=s5.index(s[i])
                
                if l[-1]!=s4[a]:
                    return False
                else:
                    l.pop()
            else:
                l.append(s[i])
        if len(l)!=0:
            return False
        return True