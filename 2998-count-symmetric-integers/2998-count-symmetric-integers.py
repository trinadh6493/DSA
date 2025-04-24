class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        if high<=10:
            return 0
        if low<=10:
            low=11
        for i in range(low,high+1):
            s=str(i)
            if len(s)%2==1:
                continue
            n=len(s)//2
            co=0
            for j in range(n):
                co+=int(s[j])
            co1=0
            for j in range(n,len(s)):
                co1+=int(s[j])
            if co==co1:
                print(i)
                c+=1
        return c