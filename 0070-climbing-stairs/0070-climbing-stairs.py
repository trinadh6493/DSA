class Solution:
    def climbStairs(self, n: int) -> int:
        fib1=1
        fib2=2
        if n<4:
            return n
        m=3
        i=4
        while i<=n:
            m=m+fib2
            t=fib2
            fib2=fib1+fib2
            fib1=t
            i+=1
        return m
            


