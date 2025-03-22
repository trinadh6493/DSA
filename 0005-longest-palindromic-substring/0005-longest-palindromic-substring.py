class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if len(s)<=1 or s==s[::-1]:
            return s
        ma=s[0]
        def funct(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(n-1):
            odd=funct(i,i)
            even=funct(i,i+1)

            if len(odd)>len(ma):
                ma=odd
            if len(even)>len(ma):
                ma=even
        return ma