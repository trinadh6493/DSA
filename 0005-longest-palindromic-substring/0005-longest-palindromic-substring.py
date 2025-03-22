class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if len(s)<=1:
            return s
        ma=s[0]
        m=1
        for i in range(n-1):
            for j in range(i+1,n):
                if j-i+1>m and s[i:j+1]==s[i:j+1][::-1]:
                    ma=s[i:j+1]
                    m=j-i+1
        return ma